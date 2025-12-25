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

with center:
    st.markdown("## ⚡ 智能入库")
    st.session_state.input_text = st.text_area(
        "输入灵感描述",
        st.session_state.input_text,
        height=220,
        placeholder="例如：一只赛博朋克风格的猫，霓虹灯背景，正在喝咖啡..."
    )

    if st.button("🚀 开始 AI 拆分", use_container_width=True):
        if not st.session_state.input_text:
            st.warning("⚠️ 请先输入一点内容！")
        else:
            # 引入 json 库（Python自带，不用额外安装）
            import json
            import re
            
            with st.spinner("DeepSeek 正在精准分类..."):
                # 🔥 升级版 Prompt：强制 JSON 格式，专治“乱归类”
                prompt = f"""
                任务：将纹身描述文本拆解为结构化关键词。
                
                【重要规则】
                1. 请务必区分：
                   - Subject (主体): 具体的物体、生物 (如: 猫, 骷髅, 玫瑰)
                   - StyleSystem (风格): 艺术流派 (如: 赛博朋克, Old School, 水墨)
                   - Mood (情绪): 氛围感受 (如: 压抑, 欢快, 神圣)
                   - Action (动作): 动态 (如: 奔跑, 燃烧, 缠绕)
                2. 不要把风格和情绪全塞进 Subject！
                
                【输出格式】
                请直接返回纯 JSON 数据，不要包含 ```json 代码块标记。格式如下：
                {{
                    "Subject": ["词1", "词2"],
                    "Action": ["词1"],
                    "Mood": ["词1"],
                    "StyleSystem": ["词1"],
                    "Usage": ["词1"]
                }}
                
                可用Key: Subject, Action, Mood, Usage, StyleSystem, Technique, Color, Texture, Composition, Accent

                输入文本：{st.session_state.input_text}
                """
                
                try:
                    res_obj = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.1
                    )
                    res = res_obj.choices[0].message.content
                    
                    parsed = []
                    
                    # 🔥 尝试 JSON 解析 (最稳的方法)
                    try:
                        # 1. 清理一下 AI 可能带的 Markdown 标记
                        clean_json = res.replace("```json", "").replace("```", "").strip()
                        data = json.loads(clean_json)
                        
                        # 2. 遍历 JSON 转为我们的格式
                        for cat, words in data.items():
                            # 模糊匹配 Key (防止 AI 写成 subjects 小写等)
                            target_key = None
                            for k in WAREHOUSE:
                                if k.lower() == cat.lower() or k.lower() in cat.lower():
                                    target_key = k
                                    break
                            
                            if target_key and isinstance(words, list):
                                for w in words:
                                    if w and isinstance(w, str):
                                        parsed.append({"cat": target_key, "val": w.strip()})
                                        
                    except json.JSONDecodeError:
                        # 🚑 兜底方案：如果 JSON 解析失败，回退到原来的文本切割
                        st.warning("⚠️ JSON 解析失败，尝试强制切割...")
                        clean_res = res.replace("：", ":").replace("\n", "|").replace("，", ",")
                        for block in clean_res.split("|"):
                            if ":" in block:
                                parts = block.split(":", 1)
                                if len(parts) == 2:
                                    cat, words = parts
                                    cat = cat.strip()
                                    target_key = None
                                    for k in WAREHOUSE:
                                        if k.lower() in cat.lower(): 
                                            target_key = k
                                            break
                                    if target_key:
                                        for w in words.split(","):
                                            w = w.strip()
                                            if w: parsed.append({"cat": target_key, "val": w})

                    st.session_state.ai_results = parsed

                    # 调试信息：如果还是空的，把原因显示出来
                    if not parsed:
                        st.error("❌ 提取结果为空！AI 可能拒绝了回答或格式错乱。")
                        with st.expander("查看 AI 原始回复"):
                            st.text(res)

                except Exception as e:
                    st.error(f"❌ 请求失败: {e}")

    # 显示拆分结果
    if st.session_state.ai_results:
        st.success(f"✅ 成功提取 {len(st.session_state.ai_results)} 个关键词")
        st.markdown("### 🧠 拆分结果")
        
        # 结果显示区域
        selected = []
        cols = st.columns(3)
        for i, item in enumerate(st.session_state.ai_results):
            with cols[i % 3]:
                # 默认勾选
                if st.checkbox(f'**{item["cat"]}** · {item["val"]}', key=f'chk_{i}', value=True):
                    selected.append(item)
        
        st.divider()

        if st.button("📥 确认入库", type="primary", use_container_width=True):
            changed_cats = set()
            # 确保 db_all 存在
            if "db_all" not in st.session_state:
                try:
                    # 尝试重新初始化
                    from engine_manager import init_data
                    init_data()
                except:
                    st.error("无法连接数据库")
                    st.stop()
                
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
                    # 引入保存函数
                    from engine_manager import save_data, WAREHOUSE
                    for cat in changed_cats:
                        save_data(WAREHOUSE[cat], st.session_state.db_all[cat])
                
                st.success(f"🎉 已更新分类: {', '.join(changed_cats)}")
                st.session_state.ai_results = [] # 清空结果
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.info("没有新的词需要入库 (可能已经存在了)")
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
