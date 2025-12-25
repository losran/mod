import streamlit as st

def apply_pro_style():
    """
    纯粹的样式注入函数。
    绝对不包含 st.set_page_config 或 st.sidebar 逻辑。
    """
    
    # 引入字体
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. 侧边栏样式 (确保可见性)
        ================================================== */
        [data-testid="stSidebar"] {{
            background-color: #0e0e0e !important;
            border-right: 1px solid #333 !important;
            min-width: 240px !important;
        }}
        
        /* 强制侧边栏内所有文字为亮色 */
        [data-testid="stSidebar"] *, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] div,
        [data-testid="stSidebar"] a {{
            color: #d0d0d0 !important;
        }}
        
        /* 选中链接的高亮样式 */
        [data-testid="stSidebar"] a[aria-current="page"] {{
            background-color: #222 !important;
            border-left: 3px solid #C0C0C0 !important;
            color: #fff !important;
        }}

        /* 恢复 Streamlit 原生的侧边栏开关箭头 (不做任何隐藏) */
        [data-testid="stSidebarCollapsedControl"] {{
            display: block !important;
            color: #ffffff !important;
        }}

        /* ==================================================
           2. 顶部 Header (保持原样，不透明，防误触)
        ================================================== */
        header[data-testid="stHeader"] {{
            background-color: transparent !important;
            /* 如果想要完全透明且穿透，解开下面这行，但要小心按钮点不到 */
            /* pointer-events: none !important; */
        }}

        /* ==================================================
           3. 银色主题 (Silver Theme)
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stApp {{ background-color: #000000; }}
        
        /* 按钮 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000 !important;
            border: 1px solid #fff !important;
            font-weight: 600 !important;
        }}
        .stButton > button[kind="secondary"] {{
            background: #1a1a1a !important;
            color: #aaa !important;
            border: 1px solid #444 !important;
        }}
        
        /* 字体 */
        h1, h2, h3, p, div {{
            font-family: 'Poppins', sans-serif !important;
        }}
    </style>
    """, unsafe_allow_html=True)
