import streamlit as st

def apply_pro_style():
    """
    视觉管理：隐藏原生导航、焊死侧边栏、银色主题
    """
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. 🧹 侧边栏大扫除 (关键！)
        ================================================== */
        /* 🔥 核心：隐藏 Streamlit 自带的那一坨文件名导航 (app, creative...) */
        [data-testid="stSidebarNav"] {{
            display: none !important;
        }}

        /* 🔥 核心：隐藏折叠按钮 (把门焊死，不许收起) */
        [data-testid="stSidebarCollapsedControl"] {{
            display: none !important;
        }}
        
        /* 移动端也不许收起 */
        section[data-testid="stSidebar"] > div:first-child {{
             /* 保持默认宽度 */
        }}

        /* ==================================================
           2. 🎨 侧边栏美化 (银色高级感)
        ================================================== */
        /* 背景色：深灰黑，增加质感 */
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a !important;
            border-right: 1px solid #222 !important;
            min-width: 260px !important; /* 稍微宽一点，更大气 */
        }}
        
        /* 强制侧边栏文字变白/银 */
        [data-testid="stSidebar"] *, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] div {{
            color: #d0d0d0 !important;
        }}
        
        /* 选中链接的高亮：银色左边框 + 深背景 */
        [data-testid="stSidebar"] a[aria-current="page"] {{
            background-color: #1a1a1a !important;
            border-left: 4px solid #C0C0C0 !important; /* 银条 */
            color: #ffffff !important;
            padding-left: 1rem !important;
            transition: all 0.2s ease;
        }}
        
        /* 鼠标悬停 */
        [data-testid="stSidebar"] a:hover {{
            background-color: #111 !important;
            color: #fff !important;
        }}

        /* ==================================================
           3. 🛠️ 全局银色主题
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stApp {{ background-color: #000000; }}
        
        /* 按钮：亮银色 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000 !important;
            border: 1px solid #fff !important;
            font-weight: 700 !important;
            box-shadow: 0 0 10px rgba(255,255,255,0.2) !important;
        }}
        
        /* 输入框背景 */
        .stTextInput input, .stTextArea textarea, .stNumberInput input {{
            background-color: #111 !important;
            border: 1px solid #333 !important;
            color: #eee !important;
        }}
        
        h1, h2, h3 {{ font-family: 'Poppins', sans-serif !important; color: #fff !important; }}
    </style>
    """, unsafe_allow_html=True)
