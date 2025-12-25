import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    # =================================================================
    # 🎨 纯代码绘制图标 (SVG Data URI) - 左右箭头版
    # =================================================================
    
    # 1. 右箭头 (→) 用于 [收起状态]，提示展开
    # Path: M5 12h14 (横线) + M12 5l7 7-7 7 (箭头头)
    icon_right_gray = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12h14'%3E%3C/path%3E%3Cpath d='M12 5l7 7-7 7'%3E%3C/path%3E%3C/svg%3E\")"
    icon_right_white = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12h14'%3E%3C/path%3E%3Cpath d='M12 5l7 7-7 7'%3E%3C/path%3E%3C/svg%3E\")"

    # 2. 左箭头 (←) 用于 [展开状态]，提示收回
    # Path: M19 12H5 (横线) + M12 19l-7-7 7-7 (箭头头)
    icon_left_gray = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'%3E%3C/path%3E%3Cpath d='M12 19l-7-7 7-7'%3E%3C/path%3E%3C/svg%3E\")"
    icon_left_white = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M19 12H5'%3E%3C/path%3E%3Cpath d='M12 19l-7-7 7-7'%3E%3C/path%3E%3C/svg%3E\")"


    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 全局字体 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        .material-icons {{ font-family: 'Material Icons' !important; }}

        /* ==============================
           核心布局修复 (防止遮挡)
           ============================== */
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a !important; 
            border-right: 1px solid #1a1a1a !important;
            z-index: 99998 !important; 
        }}
        /* 侧边栏内容下移 */
        [data-testid="stSidebarUserContent"] {{
            padding-top: 3.5rem !important; 
        }}
        /* Logo 区域 */
        [data-testid="stLogo"] {{
            height: auto !important;
            z-index: 99999 !important;
        }}

        /* ==============================
           按钮样式重置
           ============================== */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 36px !important;
            height: 36px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            opacity: 1 !important;
            z-index: 100000 !important;
            transition: all 0.2s ease !important;
            margin-top: 0px !important;
            color: transparent !important; /* 隐藏原始图标 */
        }}
        [data-testid="stHeader"] button svg {{ display: none !important; }}


        /* ==============================
           状态 A: 侧边栏关闭时 -> 显示 [右箭头 →]
           ============================== */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"] {{
            background-image: {icon_right_gray} !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-size: 20px !important;
        }}
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
            background-image: {icon_right_white} !important;
        }}


        /* ==============================
           状态 B: 侧边栏打开时 -> 显示 [左箭头 ←]
           ============================== */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            background-image: {icon_left_gray} !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-size: 20px !important;
        }}
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
            background-image: {icon_left_white} !important;
        }}


        /* ==============================
           其他去噪
           ============================== */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.6) !important; border-bottom: 1px solid #1a1a1a !important; height: 3.5rem !important; }}
        
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        .stApp {{ background-color: #000000; }}
        
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; border-radius: 6px !important; }}
        .stButton > button:hover {{ border-color: #FFFFFF !important; color: #FFFFFF !important; background: #1a1a1a !important; }}
        
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; color: #e0e0e0 !important; }}
    </style>
    """, unsafe_allow_html=True)
