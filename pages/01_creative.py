import streamlit as st
import sys
import os
import random

# ==========================================
# 🚑 路径修复
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

try:
    from style_manager import apply_pro_style
    from engine_manager import init_data, render_sidebar 
except ImportError:
    st.error("⚠️ 依赖缺失，请检查目录结构")
    def apply_pro_style(): pass
    def init_data(): pass
    def render_sidebar(): pass

# ==========================================
# 🔒 1. 强制展开侧边栏 (因为没有按钮了，必须默认开)
# ==========================================
st.set_page_config(
    layout="wide", 
    page_title="Creative Engine", 
    initial_sidebar_state="expanded" # 👈 这一句是关键！
)

apply_pro_style() 
render_sidebar()
init_data()

# 初始化状态
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []
if "current_qty" not in st.session_state:
    st.session_state.current_qty = 4

# ==========================================
# 2. 核心逻辑 (隐形混合)
# ==========================================
def get_random_ingredients():
    if "db_all" not in st.session_state or not st.session_state.db_all:
        return []
    db = st.session_state.db_all
    ingredients = []
    if "StyleSystem" in db and db["StyleSystem"]:
        ingredients.append(f"Style: {random.choice(db['StyleSystem'])}")
    chance = 0.5 
    categories = ["Technique", "Mood", "Composition", "Texture", "Color"]
    for cat in categories:
        if cat in db and db[cat] and random.random() < chance:
            ingredients.append(f"{cat}: {random.choice(db[cat])}")
    return ingredients

def ai_polish_logic(user_input):
    ingredients = get_random_ingredients()
    raw_mix = ", ".join(ingredients)
    simulated_result = f"【AI Concept】Based on '{user_input}' & [{raw_mix}]\n" \
                       f"Visual: A deconstructed composition featuring the subject with flowing organic lines. " \
                       f"Texture: utilizing {random.choice(['stippling', 'whip shading', 'solid black'])} for depth."
    return simulated_result

# ==========================================
# 3. 界面布局
# ==========================================
st.markdown("## 🧠 Creative Core")
st.caption("Warehouse Mix (Auto) -> AI Polish -> Automation Pipeline")
st.markdown("---")

col_input, col_action = st.columns([3, 1])

with col_input:
    user_input = st.text_area(
        "Subject / Core Idea", 
        height=180, 
        placeholder="输入核心主体..."
    )

with col_action:
    st.markdown("#### ⚙️ Settings")
    qty = st.number_input("Batch Size (Max 8)", min_value=1, max_value=8, value=4, step=1)
    st.write("")
    if st.button("✨ Mix & Polish", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("⚠️ 请输入内容")
        else:
            with st.spinner("Processing..."):
                result = ai_polish_logic(user_input)
                st.session_state.current_polish_result = result
                st.session_state.current_qty = qty
                st.rerun()

# ==========================================
# 4. 结果确认区
# ==========================================
if st.session_state.current_polish_result:
    st.markdown("---")
    with st.container():
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown("### 💎 Polished Result")
            st.info(st.session_state.current_polish_result)
            st.caption(f"Batch Configuration: {st.session_state.current_qty} variations will be generated.")
        with c2:
            st.markdown("### Action")
            if st.button("🚀 Send to Automation", type="primary", use_container_width=True):
                task = {
                    "prompt": st.session_state.current_polish_result,
                    "count": st.session_state.current_qty,
                    "status": "pending"
                }
                st.session_state.automation_queue.append(task)
                st.success(f"✅ Sent! Queue: {len(st.session_state.automation_queue)}")
