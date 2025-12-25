import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
    @import url('{font_url}');
    @import url('{icon_url}');

    /* ===============================
       1. 顶部 & 工具栏清理
    =============================== */
    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}
    [data-testid="stDecoration"],
    [data-testid="stToolbar"] {{
        display: none !important;
    }}

    /* ===============================
       2. 全局暗黑基调
    =============================== */
    .stApp {{
        background-color: #000000;
    }}

    [data-testid="stSidebar"] {{
        background-color: #0a0a0a;
        border-right: 1px solid #1a1a1a;
    }}

    h1, h2, h3, p, span, label, div, button {{
        font-family: 'Poppins','Noto Sans SC',sans-serif !important;
        color: #d0d0d0;
    }}

    /* ===============================
       3. 输入控件
    =============================== */
    .stTextArea textarea,
    .stTextInput input {{
        background-color: #111111 !important;
        border: 1px solid #333333 !important;
        color: #e0e0e0 !important;
        border-radius: 4px !important;
    }}

    /* ===============================
       4. 按钮
    =============================== */
    .stButton > button {{
        border-radius: 4px !important;
        border: 1px solid #444 !important;
        background: linear-gradient(180deg,#3a3a3a 0%,#222222 100%) !important;
        color: #ffffff !important;
    }}

    /* =====================================================
       5. 🔥 Slider 专项优化（只改滑块，结构安全）
    ===================================================== */

    /* 未选中轨道 */
    div[data-baseweb="slider"] > div {{
        background-color: #2a2a2a !important;
    }}

    /* 已选中轨道 */
    div[data-baseweb="slider"] div[aria-hidden="true"] {{
        background-color: #ff4b4b !important;
    }}

    /* 滑块圆点 */
    div[data-baseweb="slider"] [role="slider"] {{
        background-color: #ff4b4b !important;
        border: 2px solid #000000 !important;
        box-shadow: 0 0 6px rgba(255,75,75,0.6);
    }}

    /* 数值显示 */
    div[data-baseweb="slider"] output {{
        color: #ff4b4b !important;
        font-weight: 600;
    }}

    </style>
    """, unsafe_allow_html=True)
