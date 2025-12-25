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
           1. ⚪ 银色滑块 (Silver Slider)
        ================================================== */
        :root {{
            --primary-color: #C0C0C0 !important;
            --text-color: #E0E0E0 !important;
        }}
        
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}
        
        div[data-testid="stThumbValue"] {{
            background-color: #1a1a1a !important;
            border: 1px solid #555 !important;
        }}

        /* ==================================================
           2. 🖱️ 按钮交互：边缘高亮特效 (你要的反馈在这里!)
        ================================================== */
        /* 默认状态：深灰背景，微弱边框 */
        .stButton > button {{
            border-radius: 6px !important;
            border: 1px solid #333 !important;
            background: #111 !important; /* 纯黑底色，突显高亮 */
            color: #888 !important;
            transition: all 0.2s ease-in-out !important; /* 丝滑过渡动画 */
        }}

        /* 🔥 鼠标悬停 (Hover)：边缘变亮白 + 发光 + 文字变白 */
        .stButton > button:hover {{
            border-color: #FFFFFF !important; /* 边缘变成纯白 */
            color: #FFFFFF !important;        /* 文字变成纯白 */
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.4) !important; /* 银色光晕 */
            background: #1a1a1a !important;   /* 背景稍微提亮 */
            transform: translateY(-1px);      /* 微微上浮，增加点击欲望 */
        }}

        /* ✨ 点击中 (Active)：按下时的反馈 */
        .stButton > button:active, .stButton > button:focus {{
            border-color: #C0C0C0 !important;
            background: #222 !important;
            color: #fff !important;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5) !important;
        }}

        /* ==================================================
           3. 🙈 顶部清理 & 基础样式
        ================================================== */
        /* 顶部透明 */
        header[data-testid="stHeader"] {{
            background: transparent !important;
            background-color: rgba(0,0,0,0) !important;
            border: none !important;
        }}
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* 图标修复 */
        .material-icons, .material-icons-outlined, .material-icons-two-tone, 
        .material-icons-round, .material-icons-sharp {{
            font-family: 'Material Icons' !important;
        }}
        
        /* 全局背景 */
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}
        
        /* 字体颜色 */
        h1, h2, h3, p, span, label, div {{
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
        /* 输入框获得焦点时也要高亮 */
        .stTextArea textarea:focus, .stTextInput input:focus {{
            border-color: #888 !important;
            box-shadow: 0 0 5px rgba(255, 255, 255, 0.2) !important;
        }}
    </style>
    """, unsafe_allow_html=True)
