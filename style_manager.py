import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           🚑 1. 侧边栏按钮 - 原生风格修复
           (不去改变它的位置和形状，只确保它变白、能点击)
        ================================================== */
        [data-testid="stSidebarCollapsedControl"] {{
            /* 1. 确保在最上层 */
            z-index: 9999999 !important;
            
            /* 2. 核心修复：允许鼠标点击 (破解 pointer-events: none) */
            pointer-events: auto !important; 
            cursor: pointer !important;
            
            /* 3. 视觉修复：强制变白，背景透明 */
            color: #ffffff !important;
            background-color: transparent !important; /* 去掉灰色方块背景 */
            border: none !important;                  /* 去掉边框 */
        }}
        
        /* 鼠标移上去稍微有点反应，但不突兀 */
        [data-testid="stSidebarCollapsedControl"]:hover {{
            color: #C0C0C0 !important; /* 微微变银色 */
            background-color: rgba(255,255,255,0.1) !important; /* 极淡的背景 */
        }}

        /* 强制图标变白 */
        [data-testid="stSidebarCollapsedControl"] svg, 
        [data-testid="stSidebarCollapsedControl"] i {{
            color: #ffffff !important;
            fill: #ffffff !important;
        }}

        /* ==================================================
           2. Header 透明化
        ================================================== */
        header[data-testid="stHeader"] {{ 
            background: transparent !important; 
            border: none !important;
            /* 让鼠标穿透 Header 区域，这样不会挡住页面内容 */
            pointer-events: none !important; 
        }}

        /* 隐藏右上角菜单 */
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{ 
            display: none !important; 
        }}

        /* ==================================================
           3. 银色滑块 & 按钮样式 (保持不变)
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        
        /* 按钮 - 普通 */
        .stButton > button[kind="secondary"] {{
            border: 1px solid #333 !important; background: #111 !important; color: #888 !important;
        }}
        
        /* 按钮 - 高亮 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000000 !important;
            border: 1px solid #FFFFFF !important;
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.4) !important;
            font-weight: 700 !important;
        }}

        /* ==================================================
           4. 基础全局样式
        ================================================== */
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a; 
            border-right: 1px solid #1a1a1a; 
        }}
        h1, h2, h3, p, span, label, div {{ font-family: 'Poppins', 'Noto Sans SC', sans-serif !important; color: #d0d0d0; }}
        .material-icons {{ font-family: 'Material Icons' !important; }}
    </style>
    """, unsafe_allow_html=True)
