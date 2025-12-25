import streamlit as st
import sys
import os
import random
import time

# ==========================================
# 🚑 0. 路径修复
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

# ==========================================
# 🔍 1. 显式引入 (不隐藏报错)
# ==========================================
# 如果这里报错，屏幕上会直接显示红色错误信息，方便我们知道是缺少了哪个文件
from style_manager import apply_pro_style
from engine_manager import init_data 

# ==========================================
# 🛠️ 2. 页面配置与导航
# ==========================================
st.set_page_config(
    layout="wide", 
    page_title="Creative Engine",
    initial_sidebar_state="expanded" # 默认展开
)

# 加载数据和样式
init_data()
apply_pro_style()

# 🔥 手动绘制侧边栏 (不依赖外部文件)
def draw_sidebar_local():
    with st.sidebar:
        st.header("IViQD System")
        st.success("✅ Sidebar Active") # 调试用：如果你看到这个绿条，说明侧边栏没挂
        st.markdown("---")
        
        # 导航链接
        st.page_link("app.py", label="📥 Smart Ingest", icon="📥")
        st.page_link("pages/01_creative.py", label="🧠 Creative Core", icon="🧠")
        st.page_link("pages/02_automation.py", label="⚙️ Automation", icon="⚙️")
        
        st.markdown("---")
        # 队列状态
        q_len = len(st.session_state.get("automation_queue", []))
        st.info(f"Queue Pending: {q_len}")

draw_sidebar_local()

# ==========================================
# 3. 状态管理
# ==========================================
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []
if "current_qty" not in st.session_state:
    st.session_state.current_qty = 4

# ==========================================
# 4. 业务逻辑 (模拟 AI 润色)
# ==========================================
def run_creative_logic(intent):
    # 模拟从 engine_manager 拿数据
    db = st.session_state.get("db_all", {})
    styles = db.get("StyleSystem", ["Cyberpunk", "Traditional", "Minimalist"])
    random_style = random.choice(styles) if styles else "Mixed"
    
    return f"""
    ### 🎨 Concept: {intent}
    **Style Injection:** {random_style}
    
    **Visual Description:**
    A sophisticated composition focusing on the '{intent}'. 
    The design utilizes negative space and flow to complement the body's natural lines.
    High contrast blackwork is used for the main subject, softened by stippling shading.
    """

# ==========================================
# 5. 主界面布局
# ==========================================
st.title("🧠 Creative Core")
st.markdown("---")

col_main, col_settings = st.columns([3, 1])

with col_main:
    user_input = st.text_area("Input Subject / Intent", height=150, placeholder="例如：一只机械风格的蝴蝶...")

with col_settings:
    st.subheader("Settings")
    qty = st.number_input("Batch Size", 1, 8, 4)
    st.write("")
    if st.button("✨ Generate Ideas", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("Please enter a subject.")
        else:
            with st.spinner("Processing..."):
                time.sleep(0.5)
                res = run_creative_logic(user_input)
                st.session_state.current_polish_result = res
                st.session_state.current_qty = qty
                st.rerun()

# ==========================================
# 6. 结果展示区
# ==========================================
if st.session_state.current_polish_result:
    st.markdown("---")
    st.subheader("💎 Result")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        st.info(st.session_state.current_polish_result)
    
    with c2:
        st.write("") # Spacer
        if st.button("🚀 Send to Automation", type="primary", use_container_width=True):
            st.session_state.automation_queue.append({
                "prompt": st.session_state.current_polish_result,
                "count": st.session_state.current_qty,
                "status": "pending"
            })
            st.success("✅ Sent to Queue!")
            time.sleep(1)
            st.rerun()
