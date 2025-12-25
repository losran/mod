import streamlit as st
import sys
import os
import random
from openai import OpenAI

# ==========================================
# 0. 环境与依赖检查
# ==========================================
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from style_manager import apply_pro_style
    from engine_manager import init_data, render_sidebar
except ImportError:
    st.error("⚠️ 核心组件丢失，请检查 engine_manager.py")
    st.stop()

# ==========================================
# 1. 页面初始化
# ==========================================
st.set_page_config(layout="wide", page_title="Creative Engine", initial_sidebar_state="collapsed")

# 加载样式 & 数据
apply_pro_style()
render_sidebar()
init_data()

# 初始化 AI
try:
    client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
except Exception:
    st.warning("⚠️ 请配置 DEEPSEEK_KEY")

# 初始化状态
if "final_solutions" not in st.session_state:
    st.session_state.final_solutions = []

# ==========================================
# 2. 核心引擎 (100% 还原原版精密组装)
# ==========================================

def smart_pick_ingredient(category):
    """模拟原版的高混沌模式：从指定仓库分类中抽取灵感"""
    db = st.session_state.get("db_all", {})
    if category in db and db[category]:
        return random.choice(db[category])
    return ""

def assemble_core_logic(user_intent):
    """
    【核心逻辑堡垒】
    Sequence: Intent -> Subject -> Style -> Tech -> Color -> Texture -> Comp -> Action -> Mood -> (Accent) -> Usage
    """
    # 1. 备料
    sub     = smart_pick_ingredient("Subject")
    s_sys   = smart_pick_ingredient("StyleSystem")
    s_tech  = smart_pick_ingredient("Technique")
    s_col   = smart_pick_ingredient("Color")
    s_tex   = smart_pick_ingredient("Texture")
    s_comp  = smart_pick_ingredient("Composition")
    act     = smart_pick_ingredient("Action")
    mood    = smart_pick_ingredient("Mood")
    usage   = smart_pick_ingredient("Usage")
    
    # 2. 组装
    parts = [
        user_intent.strip(), 
        sub,                 
        s_sys,               
        s_tech,              
        s_col,               
        s_tex,               
        s_comp,              
        act,                 
        mood                 
    ]

    # 3. 混沌点缀 (40%概率)
    if random.random() > 0.4:
        s_acc = smart_pick_ingredient("Accent")
        if s_acc: parts.append(s_acc)

    # 4. 生成生肉
    raw_chain = "，".join([p for p in parts if p])
    if usage:
        raw_chain += f"，纹在{usage}"
        
    return raw_chain

def run_creative_pipeline(start_intent, count):
    """
    流水线控制器：组装 -> 润色 -> 格式化
    """
    results = []
    
    for i in range(count):
        current_idx = i + 1
        
        # --- Step A: 组装骨架 ---
        raw_bone = assemble_core_logic(start_intent)
        
        # --- Step B: AI 润色 (严格 Prompt 适配 automation 正则) ---
        sys_prompt = "你是一位资深刺青策展人。请将提供的关键词组合润色为极具艺术感的纹身描述。每段必须出现'纹身'二字。"
        user_prompt = f"""
        【原始骨架】：{raw_bone}
        
        【指令】：
        1. 必须严格保留骨架中的风格、颜色、部位等关键信息。
        2. 必须严格以 "**方案{current_idx}：**" 开头 (双星号+冒号)。这是自动化识别的锚点。
        3. 输出一段 50-80 字的完整视觉描述。
        """

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.85 
            )
            results.append(response.choices[0].message.content)
        except Exception as e:
            results.append(f"**方案{current_idx}：** 生成失败 ({str(e)})")
            
    return results

# ==========================================
# 3. 极简 UI 交互层
# ==========================================
st.markdown("## 🧠 Creative Engine")
st.caption("Auto-Assembly -> AI Polish -> Batch Handoff")
st.markdown("---")

# --- 输入区 ---
user_input = st.text_area(
    "Core Idea / Subject", 
    height=120, 
    placeholder="在此输入核心创意...\n🎲 留空则进入【盲盒模式】，系统将自动抽取核心主体并完成全套组装！"
)

# --- 操作区 ---
col_num, col_btn, col_blank = st.columns([1, 2, 3])

with col_num:
    qty = st.number_input("Batch Size", min_value=1, max_value=8, value=4)

with col_btn:
    st.write("") # Layout spacer
    
    is_blind_mode = not user_input.strip()
    btn_text = "✨ Generate (Blind Box)" if is_blind_mode else "✨ Generate Concepts"
    
    if st.button(btn_text, type="primary", use_container_width=True):
        
        # 确定起始意图
        final_intent = user_input.strip()
        if is_blind_mode:
            final_intent = smart_pick_ingredient("Subject") or "神秘图腾"
            st.toast(f"🎲 盲盒已开启！核心主体：{final_intent}", icon="🎁")
        
        with st.spinner(f"正在组装 {qty} 组方案 (Core Logic Running)..."):
            st.session_state.final_solutions = run_creative_pipeline(final_intent, qty)
            st.rerun()

# ==========================================
# 4. 结果交付区 (一键投递到 Automation)
# ==========================================
if st.session_state.final_solutions:
    st.markdown("---")
    st.subheader("💎 Polished Concepts")
    
    # 显示所有方案
    for sol in st.session_state.final_solutions:
        with st.container(border=True):
            st.markdown(sol) # 包含 "**方案N：**"

    st.markdown("---")
    c_send, c_clear = st.columns([3, 1])
    
    # --- 核心修改：批量投递按钮 ---
    with c_send:
        if st.button("🚀 Send ALL to Automation", type="primary", use_container_width=True):
            # 1. 将列表合并成一个长字符串，用换行符分隔
            # 02_automation.py 会通过正则 "**方案N：" 自动识别分割
            combined_text = "\n\n".join(st.session_state.final_solutions)
            
            # 2. 存入 session_state (适配 02 页面的读取逻辑)
            st.session_state.polished_text = combined_text
            st.session_state.auto_input_cache = combined_text # 双重保险
            
            # 3. 跳转页面
            st.switch_page("pages/02_automation.py")
            
    with c_clear:
        if st.button("Clear All", use_container_width=True):
            st.session_state.final_solutions = []
            st.rerun()
