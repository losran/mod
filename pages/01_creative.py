import streamlit as st
import sys
import os

# 🔥 关键修复：把上级目录加入路径，这样才能找到 style_manager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from style_manager import apply_pro_style
    # 假设 engine_manager 也在根目录
    from engine_manager import init_data 
except ImportError:
    # 如果还是找不到，就在页面上打印提示，而不是直接崩掉
    st.error("⚠️ 找不到 style_manager.py，请检查文件是否在根目录！")
    def apply_pro_style(): pass
    def init_data(): pass

# ==========================================
# 1. 核心配置 & 样式
# ==========================================
st.set_page_config(layout="wide", page_title="Creative Engine")
apply_pro_style() 
init_data()

# ==========================================
# 2. 界面布局 (极简版)
# ==========================================
st.markdown("## ✨ One-Click Creative")
st.caption("直接生成最终润色方案，无需筛选，一步到位。")

st.markdown("---")

# --- 输入区域 ---
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Inspiration / Subject", height=120, placeholder="输入你的核心想法，例如：一只赛博朋克风格的猫...")

with col2:
    quantity = st.slider("Quantity", 1, 4, 2, key="qty")
    chaos = st.slider("Chaos Level", 0, 100, 80, key="chaos")
    style_pref = st.selectbox("Style", ["Random Mix", "Blackwork", "Japanese", "Minimalist"], index=0)

st.markdown("---")

# ==========================================
# 3. 核心逻辑：一键生成
# ==========================================
def generate_final_results(prompt, qty, chaos_val, style):
    # 模拟生成结果
    dummy_results = [
        f"🌌 **Cyber-Void Concept**\n\n新未来主义构图，结合了{style}风格。主体解构，皮肤呈现半透明纹理。建议位置：前臂内侧。",
        f"⚔️ **Soul Echo**\n\n黑灰写实风格。流动的烟雾线条表现无我境界，细节丰富。建议位置：小腿或肩胛骨。",
        f"🌿 **Organic Flow**\n\n极简抽象风格。植物生长的动态曲线，模仿肌肉走向。建议位置：侧腰。"
    ]
    return dummy_results[:qty]

if st.button("🚀 Generate Final Concepts", type="primary", use_container_width=True):
    if not user_input.strip():
        st.warning("⚠️ 请输入想法...")
    else:
        with st.spinner("⚡ AI 正在生成最终方案..."):
            results = generate_final_results(user_input, quantity, chaos, style_pref)
            st.success("✅ 生成完毕")
            
            for idx, res in enumerate(results):
                with st.container():
                    st.markdown(f"### 🎨 Concept {idx+1}")
                    st.info(res)
                    st.code(res, language="text")
                    st.markdown("---")
