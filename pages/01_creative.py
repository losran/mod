import streamlit as st
import sys
import os
import random
import time

# ==========================================
# 1. 页面必须配置在第一行
# ==========================================
st.set_page_config(
    layout="wide", 
    page_title="Creative Engine",
    initial_sidebar_state="expanded" 
)

# ==========================================
# 2. 路径与引用修复
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

# 引入样式
try:
    from style_manager import apply_pro_style
    # 🔥 恢复真实引擎的引用！
    from engine_manager import init_data 
except ImportError:
    st.error("⚠️ 核心组件缺失，请检查 engine_manager.py")
    def apply_pro_style(): pass
    def init_data(): pass

# ==========================================
# 3. 初始化 (加载真实数据)
# ==========================================
apply_pro_style() # 穿上银色外套
init_data()       # 🔥 从 Github/本地仓库加载真实词库

# 绘制侧边栏 (必须在这里画)
with st.sidebar:
    st.header("IViQD System")
    st.markdown("---")
    st.page_link("app.py", label="📥 Smart Ingest")
    st.page_link("pages/01_creative.py", label="🧠 Creative Core")
    st.page_link("pages/02_automation.py", label="⚙️ Automation")
    st.markdown("---")
    queue = st.session_state.get("automation_queue", [])
    st.caption(f"Queue Pending: {len(queue)}")

# ==========================================
# 4. 真实业务逻辑 (Real Logic)
# ==========================================

# 状态初始化
if "current_polish_result" not in st.session_state:
    st.session_state.current_polish_result = None
if "automation_queue" not in st.session_state:
    st.session_state.automation_queue = []

def get_real_warehouse_mix():
    """从 session_state.db_all (真实仓库) 抓取灵感"""
    db = st.session_state.get("db_all", {})
    if not db:
        return ["(Warehouse Empty - Using Fallback)"]
    
    mix = []
    # 必选：风格
    if db.get("StyleSystem"):
        mix.append(f"Style: {random.choice(db['StyleSystem'])}")
    
    # 随机混合：技法、情绪、构图
    tags = ["Technique", "Mood", "Composition", "Texture"]
    for t in tags:
        # 50% 概率抓取，保持灵感随机性
        if db.get(t) and random.random() > 0.5:
            mix.append(f"{t}: {random.choice(db[t])}")
            
    return mix

def run_real_ai_polish(user_input, qty):
    """
    这里组装真实的 Prompt
    注意：为了演示速度，这里依然是模拟返回，
    你需要把下面这一段替换成你真实的 Gemini/LLM 调用代码
    """
    mix_tags = get_real_warehouse_mix()
    tags_str = ", ".join(mix_tags)
    
    # --- 真实场景请在这里调用 API ---
    # prompt = f"User: {user_input}\nStyle: {tags_str}..."
    # response = model.generate(prompt)
    # return response.text
    # -----------------------------
    
    # (目前为了不报错，先返回一个带真实标签的模拟结果)
    return f"""
    ### 🎨 Polished Concept
    **Core Intent:** {user_input}
    **Warehouse DNA:** {tags_str}
    
    **Visual Description:**
    A sophisticated tattoo design merging the user's intent with {mix_tags[0] if mix_tags else 'modern style'}.
    The composition utilizes negative space to create breathing room, while {random.choice(['whip shading', 'stippling', 'bold lines'])} adds depth and texture.
    Designed to flow naturally with body anatomy.
    """

# ==========================================
# 5. 界面布局 (银色极简版)
# ==========================================
st.title("🧠 Creative Core")
st.caption("Connected to: Warehouse DB ✅")
st.markdown("---")

col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area("Input Subject / Intent", height=150, placeholder="例如：一条赛博朋克风格的锦鲤...")

with col2:
    st.markdown("#### ⚙️ Settings")
    qty = st.number_input("Batch Size", 1, 8, 4)
    st.write("")
    
    if st.button("✨ Mix & Polish", type="primary", use_container_width=True):
        if not user_input.strip():
            st.warning("Please enter an intent.")
        else:
            with st.spinner("🔮 Mixing Warehouse Data & Polishing..."):
                # 调用真实逻辑
                res = run_real_ai_polish(user_input, qty)
                st.session_state.current_polish_result = res
                st.session_state.current_qty = qty
                st.rerun()

# ==========================================
# 6. 结果与发送
# ==========================================
if st.session_state.current_polish_result:
    st.markdown("---")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        st.info(st.session_state.current_polish_result)
        st.caption(f"Ready to generate {st.session_state.current_qty} variations.")
        
    with c2:
        st.markdown("### Action")
        if st.button("🚀 Send to Automation", type="primary", use_container_width=True):
            # 构造任务包
            task = {
                "id": int(time.time()),
                "prompt": st.session_state.current_polish_result,
                "count": st.session_state.current_qty,
                "status": "pending"
            }
            st.session_state.automation_queue.append(task)
            st.success(f"✅ Sent! (Queue: {len(st.session_state.automation_queue)})")
            time.sleep(1)
            st.rerun()
