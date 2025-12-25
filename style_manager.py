import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==============================
           1. 字体系统修复 (核心修复)
           ============================== */
        /* 不要对 span/div 使用 !important，否则会破坏图标字体 */
        html, body, [class*="css"] {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif;
            color: #d0d0d0;
        }}
        
        /* 确保图标字体拥有最高优先级，不被上面的规则覆盖 */
        .material-icons {{
            font-family: 'Material Icons' !important;
            font-weight: normal;
            font-style: normal;
            font-size: 24px; /* 确保图标有大小 */
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
        }}

        /* ==============================
           2. 界面颜色定义
           ============================== */
        :root {{
            --primary-color: #C0C0C0 !important;
            --text-color: #E0E0E0 !important;
        }}

        /* ==============================
           3. 组件样式 (Slider, Button, Input)
           ============================== */
        /* Slider */
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255,255,255,0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}
        div[data-testid="stThumbValue"] {{
            background-color: #1a1a1a !important;
            border: 1px solid #555 !important;
        }}

        /* Button */
        .stButton > button {{
            border-radius: 6px !important;
            border: 1px solid #333 !important;
            background: #111 !important;
            color: #888 !important;
            transition: all 0.2s ease-in-out !important;
            font-family: 'Poppins', sans-serif !important; /* 按钮文字强制用品牌字体 */
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

        /* Inputs (TextArea, TextInput, Selectbox) */
        .stTextArea textarea,
        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
        }}
        .stTextArea textarea:focus,
        .stTextInput input:focus {{
            border-color: #888 !important;
            box-shadow: 0 0 5px rgba(255,255,255,0.2) !important;
        }}

        /* ==============================
           4. 布局与背景 (Header, Sidebar, App)
           ============================== */
        /* Header 透明化 */
        header[data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0.6) !important;
            border-bottom: 1px solid #1a1a1a !important;
        }}
        
        /* 确保 Toolbar 可见，箭头恢复 */
        [data-testid="stToolbar"] {{
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
            right: 2rem; /*稍微往左一点，防止贴边太紧 */
        }}
        
        /* 隐藏右上角那个彩色的 Streamlit 装饰条 */
        [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* 背景色 */
        .stApp {{
            background-color: #000000;
        }}
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}

        /* ==============================
           5. 强制恢复 Toolbar 按钮样式
           ============================== */
        [data-testid="stToolbar"] button {{
            border: none !important;
            background: transparent !important;
            display: inline-flex !important;
            color: #888 !important; /* 箭头的颜色 */
        }}
        [data-testid="stToolbar"] button:hover {{
            color: #fff !important; /* hover 变白 */
            box-shadow: none !important;
        }}
    </style>
    """, unsafe_allow_html=True)
