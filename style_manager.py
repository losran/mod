import streamlit as st

def apply_pro_style():
    # 1. 引入字体
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    # 🔥 注意：所有的样式代码必须写在这个三引号 """ 里面！
    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. 🎯 修复顶部：去除蓝色背景块 & 隐藏装饰线
        ================================================== */
        /* 强制顶部 Header 透明，解决“蓝色色块”问题 */
        header[data-testid="stHeader"] {{
            background: transparent !important;
            background-color: transparent !important;
        }}
        
        /* 隐藏顶部那条彩色的装饰线 */
        [data-testid="stDecoration"] {{
            visibility: hidden;
            display: none;
        }}

        /* 隐藏右上角工具栏 (Share, Star, Menu) */
        [data-testid="stToolbar"] {{
            visibility: hidden !important;
            display: none !important;
        }}

        /* ==================================================
           2. 🔴 红色滑块 (最简版)
        ================================================== */
        /* 只要这一行，系统就会自动把滑块变成红色 */
        :root {{
            --primary-color: #ff4b4b !important;
        }}
        
        /* ⚠️ 我已经删除了导致滑块崩坏的 div[data-baseweb="slider"] 代码 */


        /* ==================================================
           3. 🩹 修复图标文字乱码
        ================================================== */
        .material-icons, .material-icons-outlined, .material-icons-two-tone, 
        .material-icons-round, .material-icons-sharp {{
            font-family: 'Material Icons' !important;
        }}

        /* ==================================================
           4. 🌑 全局暗黑基调
        ================================================== */
        .stApp {{ background-color: #000000; }}
        
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}
        
        /* 字体颜色 */
        h1, h2, h3, p, span, label, div, button {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        
        /* 输入框优化 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        
        /* 按钮样式 */
        .stButton > button {{
            border-radius: 4px !important;
            border: 1px solid #444 !important;
            background: linear-gradient(180deg, #3a3a3a 0%, #222222 100%) !important;
            color: #ffffff !important;
        }}
    </style>
    """, unsafe_allow_html=True)
