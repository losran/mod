import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 字体与背景 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        .stApp {{ background-color: #000000; }}

        /* 2. 侧边栏与导航栏纯净化 */
        [data-testid="stSidebar"] {{ background-color: #0a0a0a !important; border-right: 1px solid #1a1a1a !important; z-index: 99998 !important; }}
        [data-testid="stSidebarUserContent"] {{ padding-top: 3.5rem !important; }}
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.6) !important; border-bottom: 1px solid #1a1a1a !important; height: 3.5rem !important; }}

        /* 3. 核弹级清除：抹除顶部收起按钮内的 ghost 文字 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] * {{
            display: none !important;
            font-size: 0 !important;
        }}

        /* 4. 重新绘制左上角箭头 (纯 CSS) */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            width: 36px !important;
            height: 36px !important;
            position: relative !important;
        }}
        [data-testid="stHeader"] button[data-testid*="Sidebar"]::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            width: 8px !important;
            height: 8px !important;
            border-top: 2px solid #888 !important;
            border-right: 2px solid #888 !important;
        }}
        /* 右箭头 (收起时) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{ transform: translate(-65%, -50%) rotate(45deg) !important; }}
        /* 左箭头 (展开时) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{ transform: translate(-35%, -50%) rotate(-135deg) !important; }}

        /* =======================================================
           5. 终极对齐锁死 (输入框 + 按钮)
           ======================================================= */
        
        /* 强制底边对齐 */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}

        /* 统一高度：把数字框和按钮强行锁死在 42px */
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stButton"] button {{
            height: 42px !important;
            min-height: 42px !important;
            box-sizing: border-box !important;
        }}

        /* 彻底干掉数字框的标题占位 */
        div[data-testid="stNumberInput"] label {{
            display: none !important;
            height: 0 !important;
            margin: 0 !important;
        }}

        /* 输入框内部文字垂直居中 */
        div[data-testid="stNumberInput"] input {{
            height: 42px !important;
            padding: 0 10px !important;
        }}

        /* 按钮内部文字垂直居中 */
        div[data-testid="stButton"] button p {{
            line-height: 42px !important;
            margin: 0 !important;
        }}

        /* 基础组件配色 */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; }}
        .stButton > button:hover {{ border-color: #FFFFFF !important; color: #FFFFFF !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; color: #e0e0e0 !important; }}
    </style>
    """, unsafe_allow_html=True)
