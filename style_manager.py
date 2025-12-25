import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           🚑 1. 侧边栏按钮终极拯救 (悬浮固定)
           (不管Header怎么变，强制把这个按钮钉在左上角)
        ================================================== */
        [data-testid="stSidebarCollapsedControl"] {{
            display: flex !important;
            visibility: visible !important;
            z-index: 9999999 !important; /* 层级拉满 */
            
            /* 强制固定在左上角 */
            position: fixed !important;
            top: 20px !important;
            left: 20px !important;
            
            /* 样式美化：深灰色方块，确保能看见 */
            background-color: #222 !important;
            color: #fff !important;
            border: 1px solid #555 !important;
            border-radius: 8px !important;
            width: 44px !important;
            height: 44px !important;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5) !important;
        }}
        
        /* 鼠标移上去变亮 */
        [data-testid="stSidebarCollapsedControl"]:hover {{
            background-color: #444 !important;
            border-color: #fff !important;
            transform: scale(1.05);
            cursor: pointer !important;
        }}
        
        /* 确保里面的图标也是白的 */
        [data-testid="stSidebarCollapsedControl"] * {{
            color: #ffffff !important;
        }}

        /* ==================================================
           2. 🙈 顶部清理 (Header)
        ================================================== */
        /* Header 透明，且不阻挡点击 */
        header[data-testid="stHeader"] {{ 
            background: transparent !important; 
            border: none !important;
            pointer-events: none !important; /* 让鼠标穿透 Header */
        }}
        
        /* 隐藏右上角菜单 */
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{ 
            display: none !important; 
        }}

        /* ==================================================
           3. ⚪ 银色滑块 & 按钮交互
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}
        
        /* 按钮 - 普通 */
        .stButton > button[kind="secondary"] {{
            border: 1px solid #333 !important; background: #111 !important; color: #888 !important;
        }}
        .stButton > button[kind="secondary"]:hover {{ border-color: #666 !important; color: #ccc !important; }}
        
        /* 按钮 - 高亮 (Primary) */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000000 !important;
            border: 1px solid #FFFFFF !important;
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.4) !important;
            font-weight: 700 !important;
        }}

        /* ==================================================
           4. 基础样式
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
