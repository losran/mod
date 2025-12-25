# app.py
import streamlit as st
from openai import OpenAI

# 1. 基础配置
st.set_page_config(layout="wide", page_title="Creative Engine")

# 2. 尝试引入通用模块
try:
    from engine_manager import render_sidebar, WAREHOUSE, save_data, init_data
    # 渲染侧边栏
    render_sidebar()
except ImportError as e:
    st.error(f"❌ 缺少必要文件: engine_manager.py。请检查文件是否存在。错误信息: {e}")
    st.stop()

# 3. 初始化 OpenAI
try:
    client = OpenAI(
        api_key=st.secrets["DEEPSEEK_KEY"],
        base_url="https://api.deepseek.com"
    )
except Exception:
    st.warning("⚠️ DeepSeek Key 未配置，AI 功能将不可用。")

# 4. 初始化 Session 数据
if "ai_results" not in st.session_state:
    st.session_state.ai_results = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# 5. 页面布局
center, right = st.columns([4, 2])

# --- 中间列：智能入库 ---
with center:
    st.markdown("## ⚡ 智能入库")
    st.session_state.input_text = st.text_area(
        "输入灵感描述",
        st.session_state.input_text,
        height=220
    )

    if st.button("🚀 开始 AI 拆分", use_container_width=True):
        if not st.session_state.input_text:
            st.warning("请输入内容")
        else:
            with st.spinner("DeepSeek 正在分析..."):
                prompt = f"""
                将下列内容拆分为最小中文关键词。
                分类：Subject / Action / Mood / Usage / StyleSystem / Technique / Color / Texture / Composition / Accent
                用 | 分隔分类，用逗号分隔词。
                内容：{st.session_state.input_text}
                """
                try:
                    res = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.1
                    ).choices[0].message.content

                    parsed = []
                    clean = res.replace("：", ":").replace("\n", "|")
                    for block in clean.split("|"):
                        if ":" in block:
                            cat, words = block.split(":", 1)
                            for k in WAREHOUSE:
                                if k.lower() in cat.lower():
                                    for w in words.split(","):
                                        w = w.strip()
                                        if w:
                                            parsed.append({"cat": k, "val": w})
                    st.session_state.ai_results = parsed
                except Exception as e:
                    st.error(f"AI 请求失败: {e}")

    if st.session_state.ai_results:
        st.markdown("### 🧠 拆分结果")
        selected = []
        # 使用列布局显示 Checkbox，更整齐
        cols = st.columns(3)
        for i, item in enumerate(st.session_state.ai_results):
            with cols[i % 3]:
                if st.checkbox(f'{item["cat"]} · {item["val"]}', key=f'{item["cat"]}_{item["val"]}_{i}', value=True):
                    selected.append(item)

        if st.button("📥 确认入库", type="primary"):
            # 批量处理入库
            changed_cats = set()
            for item in selected:
                cat = item["cat"]
                val = item["val"]
                current_list = st.session_state.db_all.get(cat, [])
                
                if val not in current_list:
                    current_list.append(val)
                    st.session_state.db_all[cat] = current_list # 更新本地缓存
                    changed_cats.add(cat)
            
            # 同步到 GitHub
            if changed_cats:
                with st.spinner("正在同步到 GitHub..."):
                    for cat in changed_cats:
                        save_data(WAREHOUSE[cat], st.session_state.db_all[cat])
                
                st.success(f"已更新分类: {', '.join(changed_cats)}")
                st.session_state.ai_results = [] # 清空结果
                st.rerun() # 刷新页面更新侧边栏

# --- 右侧列：仓库查看 ---
with right:
    st.markdown("## 📦 仓库")
    cat = st.selectbox("分类", list(WAREHOUSE.keys()))
    
    # 直接从 Session 读数据
    words = st.session_state.db_all.get(cat, [])

    with st.container(height=500):
        if not words:
            st.caption("暂无数据")
        for w in words:
            c1, c2 = st.columns(
