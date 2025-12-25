import streamlit as st

def apply_pro_style():
    # 1. 引入字体
    # Material Icons: 必须引入这个，否则左上角的收起按钮会显示成 "keyboard_double_arrow_right"
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. 🎯 精准打击：只隐藏右上角工具栏
           (Share, Star, Git, Menu 都在这里)
        ================================================== */
        [data-testid="stToolbar"] {{
            visibility: hidden !important;
            display: none !important;
        }}
        
        /* 隐藏顶部那条彩色的装饰线 */
        [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* ==================================================
           2. 🩹 修复左上角图标乱码
        ================================================== */
        /* 强制让这些类名使用图标字体，这样 keyboard_double_arrow_right 就会变回漂亮的箭头图标 */
        .material-icons, .material-icons-outlined, .material-icons-two-tone, 
        .material-icons-round, .material-icons-sharp {{
            font-family: 'Material Icons' !important;
        }}

        /* ==================================================
           3. ⚠️ 关键修正：我把隐藏左侧导航的代码删掉了！
           现在左侧的默认导航栏 (App/Creative/Automation) 会正常显示出来。
        ================================================== */
        /* [data-testid="stSidebarNav"] {{
            display: none !important; 
        }} 
        */

        /* ==================================================
           4. 🎨 滑块与暗黑主题美化 (保留)
        ================================================== */
        /* 滑块轨道 (深灰) */
        div[data-baseweb="slider"] div {{ background-color: #333 !important; }}
        /* 选中条 (亮银色) */
        div[data-baseweb="slider"] div[class*="css"] {{ background-color: #e0e0e0 !important; }}
        /* 圆点 (纯白发光) */
        div[role="slider"] {{
            background-color: #ffffff !important;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
            border: none !important;
        }}
        /* 数值框 */
        div[data-testid="stThumbValue"] {{
            background-color: #000 !important;
            color: #fff !important;
            border: 1px solid #fff !important;
        }}

        /* 全局背景 */
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}
        
        /* 字体颜色 */
        h1, h2, h3, p, span, label, div, button {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        
        /* 输入框 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        
        /* 按钮 */
        .stButton > button {{
            border-radius: 4px !important;
            border: 1px solid #444 !important;
            background: linear-gradient(180deg, #3a3a3a 0%, #222222 100%) !important;
            color: #ffffff !important;
        }}
    </style>
    """, unsafe_allow_html=True)
