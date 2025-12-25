import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           🚑 1. 侧边栏“越狱”按钮 (The Jailbreak Arrow)
           我们不信任 Streamlit 的默认位置，直接强制固定。
        ================================================== */
        
        /* 针对最外层容器 */
        [data-testid="stSidebarCollapsedControl"] {{
            position: fixed !important;
            top: 12px !important;
            left: 12px !important;
            z-index: 1000002 !important; /* 比 Header 高 */
            display: block !important;
            pointer-events: auto !important; /* 强制允许点击 */
            transition: all 0.3s ease;
        }}

        /* 针对里面的 Button 元素 (关键！有时候点不到是因为没覆盖这个) */
        [data-testid="stSidebarCollapsedControl"] button {{
            pointer-events: auto !important;
            background-color: rgba(20, 20, 20, 0.8) !important; /* 深色圆底，防隐形 */
            color: #ffffff !important;
            border: 1px solid #444 !important;
            border-radius: 50% !important; /* 圆形 */
            width: 36px !important;
            height: 36px !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.5) !important;
        }}
        
        /* 鼠标移上去 */
        [data-testid="stSidebarCollapsedControl"] button:hover {{
            background-color: #ffffff !important; /* 变白 */
            color: #000000 !important;          /* 黑箭头 */
            transform: scale(1.1);
        }}

        /* 强制箭头图标本身变色 */
        [data-testid="stSidebarCollapsedControl"] svg, 
        [data-testid="stSidebarCollapsedControl"] i {{
            color: inherit !important;
        }}

        /* ==================================================
           2. Header 透明化 (隐形力场消除)
        ================================================== */
        header[data-testid="stHeader"] {{
            background: transparent !important;
            border-bottom: none !important;
            height: auto !important; /* 防止它占据过多高度 */
            pointer-events: none !important; /* 让鼠标彻底穿透 Header */
        }}
        
        /* 这里的 trick 是：让 Header 穿透，但让 Header 里的某些子元素恢复点击 */
        header[data-testid="stHeader"] > div:first-child {{
            pointer-events: none !important;
        }}

        /* 隐藏右上角工具栏 */
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* ==================================================
           3. 基础样式 (银色主题)
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ background-color: #0a0a0a; border-right: 1px solid #1a1a1a; }}
        
        /* 按钮和输入框样式 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000000 !important;
            font-weight: 700 !important;
        }}
        .stButton > button[kind="secondary"] {{
            background: #111 !important; color: #888 !important; border: 1px solid #333 !important;
        }}
        
        div[role="slider"] {{ background-color: #FFF !important; border: 1px solid #C0C0C0 !important; }}
        h1, h2, h3, p, span, div {{ font-family: 'Poppins', sans-serif !important; color: #d0d0d0; }}
        
        .material-icons {{ font-family: 'Material Icons' !important; }}
    </style>
    """, unsafe_allow_html=True)
