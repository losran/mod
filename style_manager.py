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

   /* ===============================
   🎚 Slider · 银色金属版
=============================== */

/* 底轨（未选中） */
div[data-baseweb="slider"] > div {{
    background-color: #2a2a2a !important;
    height: 4px !important;
    border-radius: 999px !important;
}}

/* 已选中轨道 */
div[data-baseweb="slider"] div[aria-hidden="true"] {{
    background: linear-gradient(
        90deg,
        #bfc3c7 0%,
        #e6e8ea 50%,
        #b3b7bb 100%
    ) !important;
    height: 4px !important;
    border-radius: 999px !important;
}}

/* 滑块圆点 */
div[data-baseweb="slider"] [role="slider"] {{
    width: 14px !important;
    height: 14px !important;
    background: radial-gradient(
        circle at 30% 30%,
        #ffffff 0%,
        #d9d9d9 40%,
        #9a9a9a 100%
    ) !important;
    border: 1px solid #555 !important;
    border-radius: 50% !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.6) !important;
    transform: translateY(-5px);
}}

/* hover 微光（很克制） */
div[data-baseweb="slider"] [role="slider"]:hover {{
    box-shadow:
        0 0 0 6px rgba(200,200,200,0.08),
        0 1px 2px rgba(0,0,0,0.6) !important;
}}

/* 数值文字 */
div[data-baseweb="slider"] output {{
    color: #9a9a9a !important;
    font-size: 12px;
    font-weight: 500;
}}
