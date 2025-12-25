import streamlit as st
import sys
import os
import random
import time

# ==========================================
# 1. 核心配置：必须在第一行
# ==========================================
st.set_page_config(
    layout="wide", 
    page_title="Creative Engine",
    initial_sidebar_state="expanded" # 🔥 默认展开，配合 CSS 隐藏按钮 = 永久展开
)

# ==========================================
# 2. 依赖检查
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

try:
    from style_manager import apply_pro_style
    from engine_manager import init_data 
except ImportError:
    st.error("⚠️ 依赖缺失，请确保 style_manager.py 在根目录")
    def apply_pro_style(): pass
    def init_data(): pass

# ==========================================
# 3. 页面装载
# ==========================================
apply_pro_style() # 加载“焊死侧边栏 + 隐藏丑菜单”的样式
init_data()       # 加载数据

# 🔥 手动绘制干净的菜单 (只显示这些，不显示 app/creative)
with st.sidebar:
    st.header("IViQD System")
    st.markdown("---")
    
    # 你的自定义导航
    st.page_link("app.py", label="Smart Ingest", icon="📥")
    st.page_link("pages/01_creative.py", label="Creative Core", icon="🧠")
    st.page_link("pages/02_automation.py", label="Automation", icon="⚙️")
    
    st.markdown("---")
    # 状态栏
    q_len = len(st.session_state.get("automation_queue", []))
    st.caption(f"Queue Status: {q_len} tasks pending")

# ==========================================
# 4. 业务逻辑 (保持不变)
# ==========================================
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []

def run_ai_logic(user_input, qty):
    # 模拟真实数据调用
    db = st.session_state.get("db_all", {})
    styles = db.get("StyleSystem", ["Cyberpunk", "Ukiyo-e", "Blackwork"])
    style = random.choice(styles) if styles else "Mixed"
    
    return f"""
    ### 🎨 Polished Concept
    **Intent:** {user_input}
    **Style Injection:** {style}
    
    **Visual:**
    A striking composition featuring the subject matter intertwined with geometric elements. 
    High contrast shading ({random.choice(['whip shading', 'stippling'])}) creates depth.
    """

# ==========================================
# 5. 主界面
# ==========================================
st.title("🧠 Creative Core")
st.caption("Fix: Clean Sidebar & Silver Theme")
st.markdown("---")

c1, c2 = st.columns([3, 1])

with c1:
    user_input = st.text_area("Input Subject", height=150, placeholder="Type something...")

with c2:
    st.markdown("#### Settings")
    qty = st.number_input("Batch Size", 1, 8, 4)
    st.write("")
    if st.button("✨ Generate", type="primary", use_container_width=True):
        if user_input:
            with st.spinner("Processing..."):
                time.sleep(0.5)
                res = run_ai_logic(user_input, qty)
                st.session_state.current_polish_result = res
                st.session_state.current_qty = qty
                st.rerun()

# 结果展示
if st.session_state.current_polish_result:
    st.markdown("---")
    c_res, c_act = st.columns([3, 1])
    with c_res:
        st.info(st.session_state.current_polish_result)
    with c_act:
        st.write("") # 占位
        if st.button("🚀 Send to Queue", type="primary", use_container_width=True):
            st.session_state.automation_queue.append("Task")
            st.success("✅ Sent!")
            time.sleep(1)
            st.rerun()
