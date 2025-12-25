import streamlit as st
import random
from style_manager import apply_pro_style
from engine_manager import init_data  # 假设你还需要读取随机词库

# ==========================================
# 1. 核心配置 & 样式
# ==========================================
st.set_page_config(layout="wide", page_title="Creative Engine")
apply_pro_style() # 加载你的银色主题和隐藏顶部栏
init_data()       # 加载词库数据 (如果你还需要随机读取风格)

# ==========================================
# 2. 界面布局
# ==========================================
st.markdown("## ✨ One-Click Creative")
st.caption("直接生成最终润色方案，无需筛选，一步到位。")

st.markdown("---")

# --- 输入区域 ---
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Inspiration / Subject", height=120, placeholder="输入你的核心想法，例如：一只赛博朋克风格的猫，或者简单的'自由'...")

with col2:
    # 数量滑块
    quantity = st.slider("Quantity", 1, 4, 2, key="qty")
    
    # 混沌度 (控制随机风格的介入程度)
    chaos = st.slider("Chaos Level", 0, 100, 80, key="chaos")
    
    # 风格倾向 (可选，如果想完全随机可以不选)
    style_pref = st.selectbox("Style Preference", ["Random Mix", "Blackwork", "Japanese", "Minimalist", "Old School"], index=0)

st.markdown("---")

# ==========================================
# 3. 核心逻辑：一键生成 (One-Click Logic)
# ==========================================

# 这是一个模拟 LLM 调用的函数 (请替换为你真实的 API 调用代码)
def generate_final_results(prompt, qty, chaos_val, style):
    # 这里是你组装 Prompt 的地方
    # 逻辑：直接告诉 AI "请扮演资深纹身师，直接跳过草稿，给我生成 X 个完美的最终方案"
    
    final_prompt = f"""
    Role: Senior Tattoo Artist & Creative Director.
    Task: Create {qty} unique, highly detailed, and polished tattoo concepts.
    Subject: {prompt}
    Chaos Level: {chaos_val}% (Higher means more unexpected combinations).
    Style Direction: {style}.
    
    Requirement:
    1. Do NOT output drafts. Direct to final polished version.
    2. Focus on visual impact, composition, flow on body, and artistic nuance.
    3. Use professional terminology (e.g., negative space, whip shading, bold lines).
    
    Output Format:
    Return ONLY the content, separated by "###".
    """
    
    # ⚠️ 真实环境请在这里调用你的 Gemini/GPT 接口
    # response = model.generate_content(final_prompt)
    # return response.text
    
    # 👇 (仅演示用) 这是一个假装的返回结果，让你看到界面效果
    dummy_results = [
        f"🌌 **Cyber-Void Cat**\n\n一种新未来主义构图。主体是一只解构的斯芬克斯猫，皮肤呈现半透明的电路板纹理。眼睛使用高饱和度的青色点刺 (dotwork) 强调。背景结合了神圣几何线条与故障艺术 (glitch art) 效果，象征有机生命与数字永生的冲突。建议位置：前臂内侧。",
        
        f"⚔️ **Samurai Soul**\n\n黑灰写实风格 (Black & Grey Realism)。武士头盔的特写，但头盔内部不是人脸，而是一团用流动线条表现的烟雾，寓意无我。盔甲细节极其丰富，带有做旧的金属质感。周围环绕着几片飘落的樱花，使用极细的单针线条 (fine line) 勾勒，形成刚柔对比。建议位置：小腿或肩胛骨。",
        
        f"🌿 **Organic Flow**\n\n极简抽象风格。没有具体的物体，完全由植物生长的动态曲线构成。线条从粗到细流畅过渡，模仿肌肉的走向。并在关键转折处加入少量的泼墨 (ink splash) 效果，增加透气感。这不仅仅是一个图案，更像是身体的一部分自然生长出来的图腾。"
    ]
    
    # 根据数量返回
    return dummy_results[:qty]


# --- 按钮与执行 ---
if st.button("🚀 Generate Final Concepts", type="primary", use_container_width=True):
    if not user_input.strip():
        st.warning("⚠️ 请先输入一点想法...")
    else:
        with st.spinner("⚡ AI 正在疯狂混合灵感并进行最终润色..."):
            # 1. 直接调用生成
            results = generate_final_results(user_input, quantity, chaos, style_pref)
            
            # 2. 直接展示结果 (不需要任何 Session State 记录，也不需要历史)
            st.success("✅ 生成完毕")
            
            # 使用漂亮的布局展示结果
            for idx, res in enumerate(results):
                with st.container():
                    st.markdown(f"### 🎨 Concept {idx+1}")
                    # 给每个结果一个漂亮的框
                    st.info(res) 
                    
                    # 只有复制按钮，没有"润色"按钮了，因为已经是最终版
                    st.code(res, language="text") 
                    st.markdown("---")
