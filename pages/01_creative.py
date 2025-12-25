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

# 加载样式 & 数据 (保留你原版的数据同步逻辑)
apply_pro_style()
render_sidebar()
init_data()

# 初始化 AI
try:
    client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
except Exception:
    st.warning("请检查 .streamlit/secrets.toml 中的 DEEPSEEK_KEY")

# 初始化状态容器
if "final_solutions" not in st.session_state:
    st.session_state.final_solutions = []

# ==========================================
# 2. 核心引擎 (100% 还原原版配方)
# ==========================================

def smart_pick_ingredient(category):
    """
    模拟原版的高混沌模式：从指定仓库分类中抽取灵感
    """
    db = st.session_state.get("db_all", {})
    if category in db and db[category]:
        return random.choice(db[category])
    return ""

def assemble_core_logic(user_intent):
    """
    【核心逻辑堡垒】
    这里严格复刻了你原代码的组装顺序。
    Sequence: Intent -> Subject -> Style -> Tech -> Color -> Texture -> Comp -> Action -> Mood -> (Accent) -> Usage
    """
    # 1. 备料：从仓库抓取所有维度的配料
    sub     = smart_pick_ingredient("Subject")
    s_sys   = smart_pick_ingredient("StyleSystem")
    s_tech  = smart_pick_ingredient("Technique")
    s_col   = smart_pick_ingredient("Color")
    s_tex   = smart_pick_ingredient("Texture")
    s_comp  = smart_pick_ingredient("Composition")
    act     = smart_pick_ingredient("Action")
    mood    = smart_pick_ingredient("Mood")
    usage   = smart_pick_ingredient("Usage")
    
    # 2. 组装：还原原版列表结构
    parts = [
        user_intent.strip(), # 用户意图
        sub,                 # 随机主体 (作为补充)
        s_sys,               # 风格系统
        s_tech,              # 技法
        s_col,               # 颜色
        s_tex,               # 质感
        s_comp,              # 构图
        act,                 # 动态
        mood                 # 情绪
    ]

    # 3. 混沌点缀：还原原版 chaos > 60 的逻辑 (40%概率触发)
    if random.random() > 0.4:
        s_acc = smart_pick_ingredient("Accent")
        if s_acc: parts.append(s_acc)

    # 4. 生成生肉 (Raw Prompt)
    # 过滤空值并用逗号连接
    raw_chain = "，".join([p for p in parts if p])
    
    # 还原 "纹在..." 逻辑
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
        
        # --- Step A: 组装骨架 (调用上方核心逻辑) ---
        raw_bone = assemble_core_logic(start_intent)
        
        # --- Step B: AI 润色 (严格 Prompt) ---
        sys_prompt = "你是一位资深刺青策展人。请将提供的关键词组合润色为极具艺术感的纹身描述。每段必须出现'纹身'二字。"
        user_prompt = f"""
        【原始骨架】：{raw_bone}
        
        【指令】：
        1. 必须严格保留骨架中的风格、颜色、部位等关键信息，不可随意丢弃。
        2. 必须严格以 "**方案{current_idx}：**" 开头 (注意是双星号)。
        3. 输出一段 50-80 字的完整视觉描述，语言要简练、高级。
        """

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.85 # 保持高创造力
            )
            results.append(response.choices[0].message.content)
        except Exception as e:
            results.append(f"**方案{current_idx}：** 生成失败 ({str(e)})")
            
    return results

# ==========================================
# 3. 极简 UI 交互层
# ==========================================
st.markdown("## 🧠 Creative Engine")
st.caption("Auto-Assembly (Original Logic) -> AI Polish -> Automation Pipeline")
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
    
    # 智能判断按钮文案
    is_blind_mode = not user_input.strip()
    btn_text = "✨ Generate (Blind Box)" if is_blind_mode else "✨ Generate Concepts"
    
    if st.button(btn_text, type="primary", use_container_width=True):
        
        # 确定起始意图
        final_intent = user_input.strip()
        if is_blind_mode:
            # 盲盒模式：从 Subject 库抽一个作为核心
            final_intent = smart_pick_ingredient("Subject") or "神秘图腾"
            st.toast(f"🎲 盲盒已开启！核心主体：{final_intent}", icon="🎁")
        
        with st.spinner(f"正在组装方案 (Core Logic: {final_intent} + Style + Tech + Color...)..."):
            st.session_state.final_solutions = run_creative_pipeline(final_intent, qty)
            st.rerun()

# ==========================================
# 4. 结果交付区 (产线对接)
# ==========================================
if st.session_state.final_solutions:
    st.markdown("---")
    st.subheader("💎 Polished Concepts")
    
    # 遍历显示结果
    for idx, solution in enumerate(st.session_state.final_solutions):
        with st.container(border=True):
            # 渲染文案 (保持 Markdown 格式)
            st.markdown(solution)
            
            # 对接自动化队列
            if st.button("🚀 Automate", key=f"auto_btn_{idx}"):
                task = {
                    "prompt": solution,       # 包含 **方案N：** 的完整文本
                    "count": 1,               # 单次执行
                    "status": "pending",
                    "source": "Creative_Engine_Optimized"
                }
                
                # 写入队列
                if "automation_queue" not in st.session_state:
                    st.session_state.automation_queue = []
                st.session_state.automation_queue.append(task)
                
                st.toast("已加入自动化产线队列", icon="✅")

    # 一键清空
    if st.button("Clear All", use_container_width=True):
        st.session_state.final_solutions = []
        st.rerun()
