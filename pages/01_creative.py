import streamlit as st
import sys
import os
import random
import time

# 1. 核心配置 (必须第一行)
st.set_page_config(layout="wide", page_title="Creative Engine", initial_sidebar_state="expanded")

# 2. 路径修复：确保能找到根目录的 engine_manager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from style_manager import apply_pro_style
from engine_manager import render_sidebar, init_data

# 3. 装载 UI 和 数据
apply_pro_style()  # 穿衣服
render_sidebar()   # 呼叫你那个“完整版”的侧边栏 (实时库存显示)
init_data()        # 初始化仓库数据

# 4. 业务逻辑：仓库取词混合
def run_mix_logic(user_input):
    db = st.session_state.get("db_all", {})
    # 自动从你 WAREHOUSE 里的各个 TXT 分类里抽词
    tags = []
    for key in ["StyleSystem", "Technique", "Mood", "Composition"]:
        if db.get(key):
            tags.append(random.choice(db[key]))
    
    tags_str = ", ".join(tags)
    return f"【Final Concept】\nInput: {user_input}\nElements: {tags_str}\n\nVisual: A polished design focusing on {user_input} with a {tags[0] if tags else 'unique'} approach. Flow and anatomy are optimized."

# 5. 极简布局：左输入 | 右控制
st.title("🧠 Creative Core")
st.markdown("---")

col_left, col_right = st.columns([3, 1])

with col_left:
    user_input = st.text_area("Intent Input", height=180, placeholder="输入核心想法...")

with col_right:
    st.markdown("### ⚙️ Settings")
    qty = st.number_input("Batch Size (Max 8)", 1, 8, 4)
    st.write("")
    if st.button("✨ Mix & Polish", type="primary", use_container_width=True):
        if user_input:
            with st.spinner("Processing..."):
                time.sleep(0.5)
                st.session_state.current_result = run_mix_logic(user_input)
                st.session_state.current_qty = qty
                st.rerun()

# 6. 确认与移交
if st.session_state.get("current_result"):
    st.markdown("---")
    res_col, act_col = st.columns([3, 1])
    with res_col:
        st.info(st.session_state.current_result)
    with act_col:
        st.write("")
        if st.button("🚀 Send to Automation", type="primary", use_container_width=True):
            if "automation_queue" not in st.session_state:
                st.session_state.automation_queue = []
            st.session_state.automation_queue.append({
                "prompt": st.session_state.current_result,
                "count": st.session_state.current_qty
            })
            st.success("✅ Success")
            time.sleep(1)
            st.rerun()
