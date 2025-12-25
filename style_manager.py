import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. ⚪ 银色滑块 (Silver Slider)
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}
        div[data-testid="stThumbValue"] {{ background-color: #1a1a1a !important; border: 1px solid #555 !important; }}

        /* ==================================================
           2. 🖱️ 按钮交互系统 (重点看这里!)
        ================================================== */
        
        /* A. 【未选中】普通按钮 (Secondary) - 暗色 */
        .stButton > button[kind="secondary"] {{
            border: 1px solid #333 !important;
            background: #111 !important;
            color: #888 !important;
            transition: all 0.2s ease-in-out !important;
        }}
        /* 鼠标移上去：变亮 */
        .stButton > button[kind="secondary"]:hover {{
            border-color: #fff !important;
            color: #fff !important;
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.4) !important;
            transform: translateY(-1px);
        }}

        /* B. 【已选中】高亮按钮 (Primary) - 永久亮银色！ */
        /* 只要你在 Python 里写 type="primary"，它就长这样，永久发光 */
        .stButton > button[kind="primary"] {{
            background: #E0E0E0 !important;   /* 亮银底色 */
            color: #000000 !important;        /* 黑字 (对比度最高) */
            border: 1px solid #FFFFFF !important;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.5) !important; /* 强烈光晕 */
            font-weight: 600 !important;
            transform: scale(1.02) !important; /* 稍微大一点，凸显选中 */
        }}
        /* 选中状态下鼠标移上去：保持高亮 */
        .stButton > button[kind="primary"]:hover {{
            background: #FFFFFF !important;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.8) !important;
        }}

        /* C. 【临时补救】点击后的聚焦状态 */
        /* 让你刚点完还没移开鼠标时也能保持亮着 */
        .stButton > button:focus:not(:active) {{
            border-color: #C0C0C0 !important;
            color: #fff !important;
        }}

        /* ==================================================
           3. 🙈 顶部清理 & 基础样式
        ================================================== */
        header[data-testid="stHeader"] {{ background: transparent !important; }}
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
        .material-icons, .material-icons-outlined {{ font-family: 'Material Icons' !important; }}
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ background-color: #0a0a0a; border-right: 1px solid #1a1a1a; }}
        h1, h2, h3, p, span, label, div {{ font-family: 'Poppins', 'Noto Sans SC', sans-serif !important; color: #d0d0d0; }}
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important; border: 1px solid #333333 !important; color: #e0e0e0 !important;
        }}
    </style>
    """, unsafe_allow_html=True)v
