import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 全局字体及基础设定 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}

        /* 2. 【核心修复】侧边栏内容垫片 */
        /* 增加顶部内边距，确保侧边栏展开后，里面的内容不会钻到按钮下面去 */
        [data-testid="stSidebarUserContent"] {{
            padding-top: 4.5rem !important; 
        }}
        
        /* 侧边栏背景与边框 */
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a !important; 
            border-right: 1px solid #1a1a1a !important;
            z-index: 99998 !important; 
        }}

        /* 3. 【核心修复】按钮定向爆破 */
        /* 选中收起/展开按钮，将其内部所有原生标签（文字、图标）彻底抹除 */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"] *,
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] * {{
            display: none !important;
            visibility: hidden !important;
            font-size: 0 !important;
        }}

        /* 按钮容器基础样式 */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 38px !important;
            height: 38px !important;
            position: relative !important;
            z-index: 100000 !important;
            margin-top: 0px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
        }}

        /* 4. 纯 CSS 画箭头 (不依赖文字，不受 display:none 影响) */
        [data-testid="stHeader"] button::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            width: 9px !important;
            height: 9px !important;
            border-top: 2px solid #888 !important;
            border-right: 2px solid #888 !important;
            transition: all 0.2s ease !important;
        }}

        /* 收起状态 -> 画右箭头 > (旋转45度) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{
            transform: translate(-70%, -50%) rotate(45deg) !important;
        }}

        /* 展开状态 -> 画左箭头 < (旋转-135度) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{
            transform: translate(-30%, -50%) rotate(-135deg) !important;
        }}

        /* 悬停高亮 */
        [data-testid="stHeader"] button:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
        }}
        [data-testid="stHeader"] button:hover::after {{
            border-color: #fff !important;
        }}

        /* 5. 顶部导航栏美化 */
        header[data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0.8) !important;
            border-bottom: 1px solid #1a1a1a !important;
            height: 3.5rem !important;
        }}

        /* 移除干扰元素 */
        [data-testid="stToolbarActions"], 
        [data-testid="stStatusWidget"], 
        [data-testid="stDecoration"] {{ 
            display: none !important; 
        }}

        /* 基础配色 */
        .stApp {{ background-color: #000000; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; }}
    </style>
    """, unsafe_allow_html=True)
