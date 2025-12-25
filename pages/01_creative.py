import streamlit as st
import sys
import os
import random
import time

# ==========================================
# 🚑 0. 环境自检与路径修复 (防报错)
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

# 尝试引入样式，如果失败也不要崩，直接跳过
try:
    from style_manager import apply_pro_style
    # 我们只从 engine_manager 拿数据初始化，不拿 sidebar，防止引用错误
    from engine_manager import init_data 
except ImportError:
    def apply_pro_style(): pass
    def init_data(): pass

# ==========================================
# 1. 页面初始化 (功能优先)
# ==========================================
st.set_page_config(
    layout="wide", 
    page_title="Creative Engine",
    initial_sidebar_state="expanded" # 强制展开，方便调试
)

# 确保数据已加载
init_data()
apply_pro_style()

# ==========================================
# 🛠️ 2. 内置导航栏 (确保侧边栏绝不是黑的)
# ==========================================
def draw_safe_sidebar():
    with st.sidebar:
        st.title("IViQD")
        st.markdown("---")
        
        # 使用原生组件，保证绝对能点
        st.page_link("app.py", label="📥 Smart Ingest")
        st.page_link("pages/01_creative.py", label="🧠 Creative Core")
        st.page_link("pages/02_automation.py", label="⚙️ Automation")
        
        st.markdown("---")
        
        # 显示当前队列状态，增加实用性
        queue_len = len(st.session_state.get("automation_queue", []))
        st.caption(f"Queue Status: {queue_len} tasks pending")

draw_safe_sidebar()

# ==========================================
# 3. 状态初始化 (防止刷新后变量丢失)
# ==========================================
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []
if "current_qty" not in st.session_state:
    st.session_state.current_qty = 4

# ==========================================
# 4. 核心业务逻辑 (仓库混合 + 润色)
# ==========================================
def get_warehouse_mix():
    """从 session_state.db_all 里抓取灵感"""
    db = st.session_state.get("db_all", {})
    if not db:
        return ["(No Data in Warehouse)"]
    
    mix = []
    # 必选风格
    if db.get("StyleSystem"):
        mix.append(f"Style: {random.choice(db['StyleSystem'])}")
    
    # 随机抓取其他维度
    tags = ["Technique", "Mood", "Composition", "Color"]
    for t in tags:
        if db.get(t) and random.random() > 0.4:
            mix.append(f"{t}: {random.choice(db[t])}")
            
    return mix

def run_creative_engine(user_intent):
    """模拟 AI 润色过程"""
    ingredients = get_warehouse_mix()
    raw_str = " + ".join(ingredients)
    
    # 模拟结果
    return f"""
    【Creative Concept】
    **Core Intent:** {user_intent}
    **Warehouse Mix:** {raw_str}
    
    **Visual Execution:**
    A highly detailed composition utilizing negative space to emphasize the subject. 
    Lines flow naturally with the body's anatomy. Contrast is achieved through heavy blackwork paired with fine dotwork shading.
    """

# ==========================================
# 5. 界面布局 (极简生产模式)
# ==========================================
st.markdown("## 🧠 Creative Core")
st.caption("Input Intent -> Warehouse Mix (Auto) -> Polish -> Queue")
st.markdown("---")

# 布局：左输入，右控制
col_main, col_ctrl = st.columns([3, 1])

with col_main:
    user_input = st.text_area(
        "Subject / Intent", 
        height=150, 
        placeholder="输入核心想法... (例如: 赛博朋克风格的猫)"
    )

with col_ctrl:
    st.markdown("#### Settings")
    # 数量控制
    qty = st.number_input("Batch Size", min_value=1, max_value=8, value=4)
    
    st.write("")
    # 生成按钮
    if st.button("✨ Generate", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("Please input subject first.")
        else:
            with st.spinner("Mixing & Polishing..."):
                time.sleep(0.5) # 假装思考一下
                result = run_creative_engine(user_input)
                st.session_state.current_polish_result = result
                st.session_state.current_qty = qty
                st.rerun()

# ==========================================
# 6. 结果确认与发送
# ==========================================
if st.session_state.current_polish_result:
    st.markdown("---")
    
    res_col, act_col = st.columns([3, 1])
    
    with res_col:
        st.info(st.session_state.current_polish_result)
        st.caption(f"Ready to generate {st.session_state.current_qty} variations.")
        
    with act_col:
        # 发送按钮
        if st.button("🚀 Send to Automation", type="primary", use_container_width=True):
            # 构造任务数据
            task = {
                "id": int(time.time()),
                "prompt": st.session_state.current_polish_result,
                "count": st.session_state.current_qty,
                "status": "pending"
            }
            st.session_state.automation_queue.append(task)
            st.success(f"✅ Sent! (Queue: {len(st.session_state.automation_queue)})")
            # 稍微停顿让你看到成功提示
            time.sleep(1)
            st.rerun()
