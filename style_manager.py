import streamlit as st

def apply_pro_style():
    # 1. 引入字体
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. ⚪ 银色滑块 (Silver Slider) - 独家定制
        ================================================== */
        /* 核心：把系统主色调改成“银灰色” */
        :root {{
            --primary-color: #C0C0C0 !important; /* 银色 */
            --text-color: #E0E0E0 !important;    /* 文字也是银白 */
        }}

        /* 优化：让滑块的圆点(把手)更亮、发光，像金属一样 */
        div[role="slider"] {{
            background-color: #FFFFFF !important; /* 纯白圆点 */
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important; /* 发光光晕 */
            border: 1px solid #C0C0C0 !important;
        }}
        
        /* 修复：稍微加深一点滑块数值的背景，让它看得清 */
        div[data-testid="stThumbValue"] {{
            background-color: #1a1a1a !important;
            border: 1px solid #555 !important;
        }}

        /* ==================================================
           2. 🙈 顶部清理 (你之前的要求)
        ================================================== */
        /* 顶部 Header 透明化，去除蓝色色块 */
        header[data-testid="stHeader"] {{
            background: transparent !important;
            background-color: rgba(0,0,0,0) !important;
            border: none !important;
        }}
        
        /* 隐藏右上角工具栏 */
        [data-testid="stToolbar"] {{
            visibility: hidden !important;
            display: none !important;
        }}
        
        /* 隐藏装饰线 */
        [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* ==================================================
           3. 🛠️ 基础修复 (图标与暗黑模式)
        ================================================== */
        .material-icons, .material-icons-outlined, .material-icons-two-tone, 
        .material-icons-round, .material-icons-sharp {{
            font-family: 'Material Icons' !important;
        }}
        
        .stApp {{ background-color: #000000; }}
        
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}
        
        h1, h2, h3, p, span, label, div, button {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        
        .stButton > button {{
            border-radius: 4px !important;
            border: 1px solid #444 !important;
            background: linear-gradient(180deg, #3a3a3a 0%, #222222 100%) !important;
            color: #ffffff !important;
        }}
    </style>
    """, unsafe_allow_html=True)
