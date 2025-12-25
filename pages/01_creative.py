import streamlit as st
import sys
import os
import random
import time

# ==========================================
# 0. 核心规则：set_page_config 必须是第一个命令
# ==========================================
st.set_page_config(
    layout="wide", 
    page_title="Creative Engine",
    initial_sidebar_state="expanded" # 默认展开，防止看不见
)

# ==========================================
# 1. 路径与引用 (只引入纯函数，不引入页面逻辑)
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

# 显式引入样式函数
try:
    from style_manager import apply_pro_style
    # 假设 engine_manager 只负责数据，不负责 UI，如果它也负责 UI，请暂时注释掉
    from engine_manager import init_data 
except ImportError:
    st.error("⚠️ 模块缺失，请检查 style_manager.py 是否在根目录")
    def apply_pro_style(): pass
    def init_data(): pass

# ==========================================
# 2. 执行 UI 渲染
# ==========================================
# A. 应用样式 (CSS)
apply_pro_style()

# B. 初始化数据
init_data()

# C. 绘制侧边栏 (在这里绘制，保证只绘制一次)
with st.sidebar:
    st.header("IViQD System")
    st.markdown("---")
    
    # 导航区
    st.page_link("app.py", label="📥 Smart Ingest")
    st.page_link("pages/01_creative.py", label="🧠 Creative Core")
    st.page_link("pages/02_automation.py", label="⚙️ Automation")
    
    st.markdown("---")
    
    # 状态区
    queue = st.session_state.get("automation_queue", [])
    st.caption(f"Queue: {len(queue)} tasks")

# ==========================================
# 3. 页面业务逻辑
# ==========================================

# 状态初始化
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []
if "current_qty" not in st.session_state:
    st.session_state.current_qty = 4

# 模拟 AI 逻辑
def ai_logic(text):
    return f"【Polished Concept】\nSubject: {text}\nStyle: Silver Chrome & Cyberpunk\nVisual: High contrast, negative space usage."

# --- 主界面布局 ---
st.title("🧠 Creative Core")
st.caption("Fix: Sidebar Visibility & Structure")
st.markdown("---")

col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area("Input", height=150, placeholder="Type something...")

with col2:
    st.markdown("#### Settings")
    qty = st.number_input("Batch", 1, 8, 4)
    st.write("")
    if st.button("✨ Generate", type="primary", use_container_width=True):
        if user_input:
            with st.spinner("Processing..."):
                time.sleep(0.5)
                st.session_state.current_polish_result = ai_logic(user_input)
                st.session_state.current_qty = qty
                st.rerun()

# --- 结果展示 ---
if st.session_state.current_polish_result:
    st.markdown("---")
    st.info(st.session_state.current_polish_result)
    
    if st.button("🚀 Send to Queue", type="primary"):
        st.session_state.automation_queue.append("Task")
        st.success("Sent!")
        time.sleep(1)
        st.rerun()
