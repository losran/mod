import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');
             /* ===== 隐藏 sidebar toggle 的文字标签，只保留点击功能 ===== */
        [data-testid="stToolbar"] span {{
            font-size: 0 !important;
            line-height: 0 !important;
        }}
    
        /* 防止 material icon 名称 fallback 成文字 */
        [data-testid="stToolbar"] .material-icons {{
            font-size: 0 !important;
        }}
        :root {{
            --primary-color: #C0C0C0 !important;
            --text-color: #E0E0E0 !important;
        }}

        /* ===== Slider ===== */
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255,255,255,0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}

        div[data-testid="stThumbValue"] {{
            background-color: #1a1a1a !important;
            border: 1px solid #555 !important;
        }}

        /* ===== Button ===== */
        .stButton > button {{
            border-radius: 6px !important;
            border: 1px solid #333 !important;
            background: #111 !important;
            color: #888 !important;
            transition: all 0.2s ease-in-out !important;
        }}

        .stButton > button:hover {{
            border-color: #FFFFFF !important;
            color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255,255,255,0.4) !important;
            background: #1a1a1a !important;
            transform: translateY(-1px);
        }}

        .stButton > button:active,
        .stButton > button:focus {{
            border-color: #C0C0C0 !important;
            background: #222 !important;
            color: #fff !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5) !important;
        }}

        /* ===== Header / Sidebar Toggle SAFE ===== */
        header[data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0.6) !important;
            border-bottom: 1px solid #1a1a1a !important;
        }}

        [data-testid="stToolbar"] {{
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
        }}

        [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* ===== App & Sidebar ===== */
        .stApp {{
            background-color: #000000;
        }}

        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}

        h1, h2, h3, p, span, label, div {{
            font-family: 'Poppins','Noto Sans SC',sans-serif !important;
            color: #d0d0d0;
        }}

        .stTextArea textarea,
        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}

        .stTextArea textarea:focus,
        .stTextInput input:focus {{
            border-color: #888 !important;
            box-shadow: 0 0 5px rgba(255,255,255,0.2) !important;
        }}
    </style>
    """, unsafe_allow_html=True)
