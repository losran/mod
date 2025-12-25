import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 基础全局样式与翻译插件禁用 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        
        /* 核心：禁止翻译插件改动图标区域 */
        .notranslate, [data-testid*="Sidebar"] {{
            translate: no !important;
        }}

        .stApp {{ background-color: #000000; }}

        /* 2. 侧边栏与头部：解决顶部重叠 */
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a !important; 
            border-right: 1px solid #1a1a1a !important; 
            z-index: 99998 !important; 
        }}
        
        /* 增加侧边栏顶部垫片，防止内容顶到按钮 */
        [data-testid="stSidebarUserContent"] {{ 
            padding-top: 5rem !important; 
        }}

        /* 隐藏顶部装饰条和状态栏 */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ 
            display: none !important; 
        }}

        header[data-testid="stHeader"] {{ 
            background-color: rgba(0,0,0,0.85) !important; 
            border-bottom: 1px solid #1a1a1a !important; 
            height: 3.5rem !important;
            z-index: 99999 !important;
        }}

        /* 3. 彻底杀掉那个 keybo... 乱码文字 */
        /* 针对收起/展开按钮的所有后代元素进行物理抹除 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] * {{
            display: none !important;
            visibility: hidden !important;
            font-size: 0 !important;
            opacity: 0 !important;
        }}

        /* 4. 重塑左上角控制按钮 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            width: 34px !important;
            height: 34px !important;
            border-radius: 4px !important;
            position: relative !important;
            margin-left: 10px !important;
            z-index: 100000 !important;
        }}

        /* 5. 纯几何绘制箭头 (不受翻译插件影响) */
        [data-testid="stHeader"] button[data-testid*="Sidebar"]::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            width: 7px !important;
            height: 7px !important;
            border-top: 2px solid #aaa !important;
            border-right: 2px solid #aaa !important;
            transition: all 0.2s ease !important;
        }}

        /* 右箭头 (收起时) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{ 
            transform: translate(-65%, -50%) rotate(45deg) !important; 
        }}
        /* 左箭头 (展开时) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{ 
            transform: translate(-35%, -50%) rotate(-135deg) !important; 
        }}

        /* 6. 核心布局对齐：锁死高度与适配 */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}

        /* 锁死数字框和按钮高度为 42px */
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stButton"] button {{
            height: 42px !important;
            min-height: 42px !important;
            box-sizing: border-box !important;
        }}

        div[data-testid="stNumberInput"] label {{ display: none !important; }}
        div[data-testid="stNumberInput"] input {{ height: 42px !important; padding: 0 10px !important; }}
        div[data-testid="stButton"] button p {{ line-height: 42px !important; margin: 0 !important; font-size: 14px !important; }}

        /* 7. 平板与手机端响应式适配 */
        @media (max-width: 1024px) {{
            /* 平板端允许换行，防止 image_0a066c 中的重叠 */
            [data-testid="stHorizontalBlock"] {{
                flex-wrap: wrap !important;
                gap: 12px !important;
            }}
            [data-testid="column"] {{
                flex: 1 1 auto !important;
                min-width: 140px !important;
            }}
        }}

        @media (max-width: 768px) {{
            /* 手机端全宽堆叠 */
            [data-testid="stHorizontalBlock"] {{
                flex-direction: column !important;
            }}
            [data-testid="column"], div[data-testid="stNumberInput"], div[data-testid="stButton"] {{
                width: 100% !important;
                max-width: 100% !important;
            }}
        }}

        /* 基础组件配色 */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; }}
    </style>
    """, unsafe_allow_html=True)
