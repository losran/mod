import streamlit as st
import sys
import os
import random

# 路径修复 & 模块引入
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from style_manager import apply_pro_style
    from engine_manager import init_data, render_sidebar 
except ImportError:
    st.error("⚠️ 依赖丢失，请检查 engine_manager.py 和 style_manager.py")

# ==========================================
# 1. 页面初始化
# ==========================================
# 👇 加上 initial_sidebar_state="expanded"
st.set_page_config(layout="wide", page_title="Creative Engine", initial_sidebar_state="expanded")
apply_pro_style() 
render_sidebar()
init_data()

# 初始化 session_state
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []
if "current_qty" not in st.session_state:
    st.session_state.current_qty = 4

# ==========================================
# 2. 核心逻辑 (隐形混沌)
# ==========================================

def get_random_ingredients():
    """
    内部默认混沌度 (Fixed Chaos Level = 50%)
    不再需要用户调整，系统自动保持适度的随机性
    """
    if "db_all" not in st.session_state or not st.session_state.db_all:
        return []
    
    db = st.session_state.db_all
    ingredients = []
    
    # 必选：随机取一个风格
    if "StyleSystem" in db and db["StyleSystem"]:
        ingredients.append(f"Style: {random.choice(db['StyleSystem'])}")
    
    # 其他元素：固定 50% 概率随机抓取
    chance = 0.5 
    categories = ["Technique", "Mood", "Composition", "Texture", "Color"]
    for cat in categories:
        if cat in db and db[cat] and random.random() < chance:
            ingredients.append(f"{cat}: {random.choice(db[cat])}")
            
    return ingredients

def ai_polish_logic(user_input):
    """用户意图 + 隐形仓库词 -> AI 润色"""
    # 1. 自动抓取原料
    ingredients = get_random_ingredients()
    raw_mix = ", ".join(ingredients)
    
    # 2. 模拟 AI 润色 (Prompting)
    # 真实场景请替换为: response = model.generate_content(...)
    simulated_result = f"【AI Concept】Based on '{user_input}' & [{raw_mix}]\n" \
                       f"Visual: A deconstructed composition featuring the subject with flowing organic lines. " \
                       f"Texture: utilizing {random.choice(['stippling', 'whip shading', 'solid black'])} for depth. " \
                       f"Placement flow aligned with body muscle structure."
    
    return simulated_result

# ==========================================
# 3. 界面布局 (左输入 | 右控制)
# ==========================================
st.markdown("## 🧠 Creative Core")
st.caption("Warehouse Mix (Auto) -> AI Polish -> Automation Pipeline")

st.markdown("---")

# 布局：左边给 3 份宽度(输入)，右边给 1 份宽度(操作)
col_input, col_action = st.columns([3, 1])

# --- 左侧：意图输入 ---
with col_input:
    user_input = st.text_area(
        "Subject / Core Idea", 
        height=180, # 稍微加高一点，显得更重要
        placeholder="输入核心主体，例如：一只燃烧的蝴蝶，赛博朋克风格..."
    )

# --- 右侧：数量 & 生成 ---
with col_action:
    st.markdown("#### ⚙️ Settings")
    
    # 1. 数量控制 (Number Input)
    # min=1, max=8, step=1 (点击上下箭头调整)
    qty = st.number_input(
        "Batch Size (Max 8)", 
        min_value=1, 
        max_value=8, 
        value=4, 
        step=1,
        help="生成批次数量"
    )
    
    st.write("") # 加一点空隙
    
    # 2. 生成按钮
    if st.button("✨ Mix & Polish", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("⚠️ 请输入内容")
        else:
            with st.spinner("Processing..."):
                # 运行逻辑
                result = ai_polish_logic(user_input)
                # 存结果
                st.session_state.current_polish_result = result
                # 存数量 (发送到自动化时要用)
                st.session_state.current_qty = qty
                st.rerun()

# ==========================================
# 4. 结果确认区
# ==========================================
if st.session_state.current_polish_result:
    st.markdown("---")
    
    # 显示结果容器
    with st.container():
        c1, c2 = st.columns([3, 1])
        
        with c1:
            st.markdown("### 💎 Polished Result")
            st.info(st.session_state.current_polish_result)
            st.caption(f"Batch Configuration: {st.session_state.current_qty} variations will be generated.")
            
        with c2:
            st.markdown("### Action")
            # 这里的数量直接读取刚才设置的 current_qty
            if st.button("🚀 Send to Automation", type="primary", use_container_width=True):
                # 构造任务包
                task = {
                    "prompt": st.session_state.current_polish_result,
                    "count": st.session_state.current_qty,
                    "status": "pending"
                }
                # 加入队列
                st.session_state.automation_queue.append(task)
                
                st.success(f"✅ Sent! Queue: {len(st.session_state.automation_queue)}")
