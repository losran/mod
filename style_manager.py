import streamlit as st

def apply_pro_style():
    # 1. 引入字体库
    # Noto Sans SC: 优化中文显示
    # Material Icons: 🔥 专门修复那个 'keyboard_double_arrow_right' 乱码问题
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* =========================
           1. 🙈 全局隐藏：右上角工具栏 & 顶部红线
           (这就解决了你说的“切换页面它还在”的问题)
        ========================= */
        [data-testid="stToolbar"] {{
            visibility: hidden !important;
            display: none !important;
        }}
        
        [data-testid="stDecoration"] {{
            display: none !important;
        }}
        
        [data-testid="stHeader"] {{
            background: transparent !important;
        }}

        /* =========================
           2. 🛠️ 修复图标显示为文字的问题
        ========================= */
        /* 强制指定图标字体，解决 keyboard_double_arrow_right 问题 */
        .material-icons, .material-icons-outlined, .material-icons-two-tone, 
        .material-icons-round, .material-icons-sharp {{
            font-family: 'Material Icons' !important;
        }}

        /* =========================
           3. ⚪ 全局滑块 (Slider) 亮白化
           (不用在每个页面单独写了，这里写一次，全站生效)
        ========================= */
        /* 轨道背景 (深灰) */
        div[data-baseweb="slider"] div {{ background-color: #333 !important; }}
        /* 选中条 (亮银色) */
        div[data-baseweb="slider"] div[class*="css"] {{ background-color: #e0e0e0 !important; }}
        /* 圆点 (纯白发光) */
        div[role="slider"] {{
            background-color: #ffffff !important;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
            border: none !important;
        }}
        /* 数值框 (黑底白字) */
        div[data-testid="stThumbValue"] {{
            background-color: #000 !important;
            color: #fff !important;
            border: 1px solid #fff !important;
        }}

        /* =========================
           4. 🌑 全局暗黑主题 & 字体
        ========================= */
        .stApp {{ background-color: #000000; }}
        
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}
        
        /* 隐藏左上角的默认页面导航 (app/creative/automation) */
        [data-testid="stSidebarNav"] {{
            display: none !important;
        }}

        /* 全局字体 */
        h1, h2, h3, p, span, label, div, button {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        
        /* 输入框优化 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        .stTextArea textarea:focus {{
            border-color: #ffffff !important;
            box-shadow: 0 0 0 1px #ffffff !important;
        }}
        
        /* 按钮通用样式 */
        .stButton > button {{
            border-radius: 4px !important;
            font-weight: 500 !important;
            border: 1px solid #444 !important;
            background: linear-gradient(180deg, #3a3a3a 0%, #222222 100%) !important;
            color: #ffffff !important;
        }}
        .stButton > button:hover {{
            border-color: #888 !important;
            color: #fff !important;
        }}
    </style>
    """, unsafe_allow_html=True)
