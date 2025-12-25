import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           🔒 1. 侧边栏“焊死”模式 (No Collapse)
           直接隐藏侧边栏的开关按钮，让它看起来像是永久固定的。
        ================================================== */
        [data-testid="stSidebarCollapsedControl"] {{
            display: none !important;
        }}
        
        /* 以防万一，把移动端的关闭按钮也藏了 */
        section[data-testid="stSidebar"] button {{
            display: none !important;
        }}

        /* ==================================================
           2. Header 透明化
        ================================================== */
        header[data-testid="stHeader"] {{
            background: transparent !important;
            border: none !important;
            pointer-events: none !important;
        }}
        
        /* 隐藏右上角工具栏 */
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* ==================================================
           3. 银色主题 & 交互
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a; 
            border-right: 1px solid #1a1a1a; 
            /* 确保侧边栏宽度合适，显得像固定布局 */
            min-width: 250px !important; 
        }}

        /* 按钮高亮逻辑 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000000 !important;
            border: 1px solid #FFFFFF !important;
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.4) !important;
            font-weight: 700 !important;
        }}
        .stButton > button[kind="secondary"] {{
            background: #111 !important; color: #888 !important; border: 1px solid #333 !important;
        }}
        
        /* 滑块 */
        div[role="slider"] {{ background-color: #FFF !important; border: 1px solid #C0C0C0 !important; }}
        
        /* 字体 */
        h1, h2, h3, p, span, div {{ font-family: 'Poppins', sans-serif !important; color: #d0d0d0; }}
        .material-icons {{ font-family: 'Material Icons' !important; }}
    </style>
    """, unsafe_allow_html=True)
