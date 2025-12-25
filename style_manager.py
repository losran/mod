import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. 侧边栏基础修复 (确保绝对可见)
        ================================================== */
        /* 背景色：深灰，不是纯黑，防止和背景融为一体 */
        [data-testid="stSidebar"] {{
            background-color: #111111 !important;
            border-right: 1px solid #333 !important;
        }}
        
        /* 强制侧边栏里所有文字变白 */
        [data-testid="stSidebar"] *, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] div {{
            color: #ffffff !important;
        }}
        
        /* 侧边栏链接样式 */
        [data-testid="stSidebar"] a {{
            color: #e0e0e0 !important;
        }}

        /* ❌ 删除所有隐藏侧边栏开关的代码，恢复 Streamlit 原生箭头 */
        [data-testid="stSidebarCollapsedControl"] {{
            display: block !important;
            color: #ffffff !important;
        }}

        /* ==================================================
           2. 顶部 Header (恢复默认，确保不遮挡)
        ================================================== */
        /* 暂时取消透明效果，确保功能正常 */
        header[data-testid="stHeader"] {{
            background-color: #000000 !important;
            opacity: 1 !important;
        }}

        /* ==================================================
           3. 银色主题配色
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; }}
        
        .stApp {{ background-color: #000000; }}
        
        /* 按钮样式 */
        .stButton > button[kind="primary"] {{
            background: #e0e0e0 !important;
            color: #000 !important;
            border: 1px solid #fff !important;
            font-weight: bold !important;
        }}
        
        .stButton > button[kind="secondary"] {{
            background: #222 !important;
            color: #aaa !important;
            border: 1px solid #444 !important;
        }}
        
        h1, h2, h3, p, span {{
            font-family: 'Poppins', sans-serif !important;
            color: #e0e0e0;
        }}
    </style>
    """, unsafe_allow_html=True)
