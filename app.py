import streamlit as st
from openai import OpenAI

# 1. 基础配置
st.set_page_config(layout="wide", page_title="Creative Engine")

# 2. 引入通用模块
# ⚠️ 如果这里报错 ImportError，说明你还没创建 engine_manager.py 文件
try:
    from engine_manager import render_sidebar, WAREHOUSE, save_data, init_data
    render_sidebar()
except ImportError as e:
    st.error(f"❌ 严重错误: 找不到 engine_manager.py。请在项目根目录新建该文件！\n错误详情: {e}")
    st.stop()

# 3. 初始化 OpenAI
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_KEY"],
    base_url="https://api.deepseek.com"
)

# 4. 初始化 Session
if "ai_results" not in st.session_state:
    st.session_state.ai_results = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# 5. 页面布局
center, right = st.columns([4, 2])

# ===========================
# 左侧：智能拆分区域
# ===========================
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
                            cat = cat.strip()
                            target_key = None
                            # 模糊匹配分类 key
                            for k in WAREHOUSE:
                                if k.lower() in cat.lower():
                                    target_key = k
                                    break
                            
                            if target_key:
                                for w in words.split(","):
                                    w = w.strip()
                                    if w:
                                        parsed.append({"cat": target_key, "val": w})
                    st.session_state.ai_results = parsed
                except Exception as e:
                    st.error(f"AI 请求失败: {e}")

    # 显示拆分结果
    if st.session_state.ai_results:
        st.markdown("### 🧠 拆分结果")
        selected = []
        cols = st.columns(3)
        for i, item in enumerate(st.session_state.ai_results):
            with cols[i % 3]:
                if st.checkbox(f'{item["cat"]} · {item["val"]}', key=f'chk_{i}', value=True):
                    selected.append(item)

        if st.button("📥 确认入库", type="primary"):
            changed_cats = set()
            # 确保数据已初始化
            if "db_all" not in st.session_state:
                init_data()
                
            for item in selected:
                cat = item["cat"]
                val = item["val"]
                current_list = st.session_state.db_all.get(cat, [])
                
                if val not in current_list:
                    current_list.append(val)
                    st.session_state.db_all[cat] = current_list
                    changed_cats.add(cat)
            
            if changed_cats:
                with st.spinner("正在同步到 GitHub..."):
                    for cat in changed_cats:
                        save_data(WAREHOUSE[cat], st.session_state.db_all[cat])
                st.success(f"已更新分类: {', '.join(changed_cats)}")
                st.session_state.ai_results = []
                st.rerun()

# ===========================
# 右侧：仓库管理区域
# ===========================
with right:
    st.markdown("## 📦 仓库")
    cat = st.selectbox("分类", list(WAREHOUSE.keys()))
    
    if "db_all" not in st.session_state:
        init_data()
        
    words = st.session_state.db_all.get(cat, [])

    with st.container(height=500):
        if not words:
            st.caption("暂无数据")
        for w in words:
            # ✅ 这里就是刚才报错的地方，已经修复：
            c1, c2 = st.columns([4, 1]) 
            with c1:
                if st.button(w, key=f"add_{w}", use_container_width=True):
                    st.session_state.input_text += f" {w}"
            with c2:
                if st.button("✕", key=f"del_{cat}_{w}"):
                    new_list = [i for i in words if i != w]
                    st.session_state.db_all[cat] = new_list
                    save_data(WAREHOUSE[cat], new_list)
                    st.rerun()
