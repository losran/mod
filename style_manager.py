import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           🚑 1. 侧边栏按钮终极拯救方案 (Fixed Position)
           (不管Header怎么变，强制把这个按钮钉在左上角)
        ================================================== */
        [data-testid="stSidebarCollapsedControl"] {{
            display: flex !important;
            visibility: visible !important;
            align-items: center;
            justify-content: center;
            
            /* 🔥 关键：脱离文档流，强制固定位置 */
            position: fixed !important; 
            top: 15px !important;
            left: 15px !important;
            z-index: 9999999 !important; /* 层级拉满 */
            
            /* 样式美化：让它看起来像个独立的悬浮按钮 */
            background-color: #222222 !important;
            color: #ffffff !important;
            width: 40px !important;
            height: 40px !important;
            border-radius: 50% !important; /* 变成圆形 */
            border: 1px solid #444 !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
            transition: all 0.3s ease !important;
        }}

        /* 鼠标移上去发光 */
        [data-testid="stSidebarCollapsedControl"]:hover {{
            background-color: #ffffff !important;
            color: #000000 !important;
            transform: scale(1.1);
            cursor: pointer !important;
        }}
        
        /* 确保里面的图标也是对的颜色 */
        [data-testid="stSidebarCollapsedControl"] * {{
            color: inherit !important;
        }}

        /* ==================================================
           2. 🙈 顶部清理 (Header)
        ================================================== */
        /* Header 依然透明，但不会再挡住上面的 Fixed 按钮了 */
        header[data-testid="stHeader"] {{ 
            background: transparent !important; 
            border: none !important;
            pointer-events: none !important; /* 让鼠标穿透 Header 区域 */
        }}
        /* 隐藏掉右上角的菜单和彩虹条 */
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{ 
            display: none !important; 
        }}

        /* ==================================================
           3. ⚪ 银色滑块 (Silver Slider)
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}
        div[data-testid="stThumbValue"] {{ background-color: #1a1a1a !important; border: 1px solid #555 !important; }}

        /* ==================================================
           4. 🖱️ 按钮交互
        ================================================== */
        /* 普通按钮 */
        .stButton > button[kind="secondary"] {{
            border: 1px solid #333 !important; background: #111 !important; color: #888 !important;
            transition: all 0.2s ease-in-out !important;
        }}
        .stButton > button[kind="secondary"]:hover {{ border-color: #666 !important; color: #ccc !important; }}

        /* 高亮按钮 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000000 !important;
            border: 1px solid #FFFFFF !important;
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.4) !important;
            font-weight: 700 !important;
            transform: scale(1.02);
        }}
        .stButton > button[kind="primary"]:hover {{
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.7) !important;
        }}

        /* ==================================================
           5. 基础样式
        ================================================== */
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ background-color: #0a0a0a; border-right: 1px solid #1a1a1a; }}
        h1, h2, h3, p, span, label, div {{ font-family: 'Poppins', 'Noto Sans SC', sans-serif !important; color: #d0d0d0; }}
        .material-icons, .material-icons-outlined {{ font-family: 'Material Icons' !important; }}
        
        /* 修复左侧导航可能的文字问题 */
        .stPageLink a {{ font-weight: 500 !important; }}
    </style>
    """, unsafe_allow_html=True)
