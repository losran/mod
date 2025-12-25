import streamlit as st

def apply_pro_style():
    # 引入字体：Poppins (英文), Noto Sans SC (中文)
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        /* 1. 引入字体资源 */
        @import url('{font_url}');

        /* ==============================
           2. 字体强制覆盖 (修复字体不显示问题)
           ============================== */
        
        /* 关键：把 h1-h6, p, button, input 等所有标签都带上，防止 Streamlit 默认样式覆盖 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}

        /* 保护 Material Icons 不被上面的字体覆盖 (否则图标会变成方块) */
        .material-icons {{
            font-family: 'Material Icons' !important;
        }}
        
        /* ==============================
           3. 界面纯净模式 (隐藏右上角)
           ============================== */
        
        /* 隐藏右上角的三点菜单、Deploy 按钮、Github 图标等 */
        [data-testid="stToolbarActions"] {{
            display: none !important;
            visibility: hidden !important;
        }}

        /* 隐藏右上角的运行状态（跑动的小人/连接状态） */
        [data-testid="stStatusWidget"] {{
            display: none !important;
            visibility: hidden !important;
        }}

        /* 隐藏顶部的彩虹装饰条 */
        [data-testid="stDecoration"] {{
            display: none !important;
        }}

        /* 确保 Header 容器本身还在 (为了放我们自定义的左上角按钮)，但背景透明 */
        header[data-testid="stHeader"] {{
            background-color: rgba(0,0,0,0.6) !important;
            border-bottom: 1px solid #1a1a1a !important;
            z-index: 999 !important;
        }}

        /* ==============================
           4. 左上角菜单按钮 (保持你的汉堡按钮设计)
           ============================== */
        [data-testid="stHeader"] button {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 36px !important;
            height: 36px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            opacity: 1 !important;
            z-index: 99999 !important;
            transition: all 0.2s ease !important;
        }}

        /* 隐藏原图标，绘制新图标 */
        [data-testid="stHeader"] button span, 
        [data-testid="stHeader"] button svg {{ display: none !important; }}
        
        [data-testid="stHeader"] button::after {{
            content: "☰";
            font-size: 18px !important;
            color: #888 !important;
            font-family: sans-serif !important; /* 图标必须用系统字体，否则乱码 */
            line-height: 1 !important;
        }}
        
        [data-testid="stHeader"] button:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
        }}
        [data-testid="stHeader"] button:hover::after {{ color: #fff !important; }}


        /* ==============================
           5. 组件配色与细节 (Button, Input, Slider)
           ============================== */
        :root {{
            --primary-color: #C0C0C0 !important;
            --text-color: #E0E0E0 !important;
        }}
        
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a; 
            border-right: 1px solid #1a1a1a; 
        }}

        /* 按钮 */
        .stButton > button {{
            border-radius: 6px !important;
            border: 1px solid #333 !important;
            background: #111 !important;
            color: #888 !important;
            font-family: 'Poppins', sans-serif !important;
        }}
        .stButton > button:hover {{
            border-color: #FFFFFF !important;
            color: #FFFFFF !important;
            background: #1a1a1a !important;
        }}

        /* 输入框 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        
        /* 滑块 */
        div[role="slider"] {{ background-color: #FFFFFF !important; border: 1px solid #C0C0C0 !important; }}
        div[data-testid="stThumbValue"] {{ background-color: #1a1a1a !important; }}

    </style>
    """, unsafe_allow_html=True)
