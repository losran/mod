import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 全局字体与背景：强制禁用翻译插件干扰 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        .stApp {{ background-color: #000000; }}

        /* 2. 侧边栏布局：增加顶部垫片防止 Logo 冲撞 */
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a !important; 
            border-right: 1px solid #1a1a1a !important; 
        }}
        [data-testid="stSidebarUserContent"] {{ 
            padding-top: 5rem !important; 
        }}

        /* 3. 头部纯净化：隐藏干扰元素 */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ 
            display: none !important; 
        }}
        header[data-testid="stHeader"] {{ 
            background-color: rgba(0,0,0,0.8) !important; 
            border-bottom: 1px solid #1a1a1a !important; 
        }}

        /* 4. 彻底杀掉乱码文字 (精准定点爆破) */
        /* 强制隐藏按钮里所有原本的文字、图标，防止 keyboard_... 显现 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] * {{
            display: none !important;
            font-size: 0 !important;
            color: transparent !important;
            text-indent: -9999px !important;
        }}

        /* 5. 画“三条杠”：不用代码词，绝对不产生乱码 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            width: 36px !important;
            height: 36px !important;
            position: relative !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}
        [data-testid="stHeader"] button[data-testid*="Sidebar"]::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: 18px !important;
            height: 2px !important;
            background-color: #888 !important;
            /* 使用阴影画出上下两杠 */
            box-shadow: 0 -6px 0 #888, 0 6px 0 #888 !important;
            transition: all 0.2s ease !important;
        }}
        [data-testid="stHeader"] button:hover::after {{
            background-color: #fff !important;
            box-shadow: 0 -6px 0 #fff, 0 6px 0 #fff !important;
        }}

        /* 6. 核心对齐锁死：42px 绝对对齐 */
        /* 强制底边对齐容器 */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}
        /* 统一数字框和按钮的物理厚度 */
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stButton"] button {{
            height: 42px !important;
            min-height: 42px !important;
            box-sizing: border-box !important;
        }}
        /* 移除标题占位 */
        div[data-testid="stNumberInput"] label {{ display: none !important; }}
        div[data-testid="stNumberInput"] input {{ height: 42px !important; }}
        /* 按钮文字居中 */
        div[data-testid="stButton"] button p {{ line-height: 42px !important; margin: 0 !important; }}

        /* 7. 平板与手机适配：解决重叠 */
        @media (max-width: 1024px) {{
            [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; gap: 10px !important; }}
            [data-testid="column"] {{ flex: 1 1 auto !important; min-width: 130px !important; }}
        }}
        @media (max-width: 768px) {{
            [data-testid="stHorizontalBlock"] {{ flex-direction: column !important; }}
            [data-testid="column"], div[data-testid="stNumberInput"], div[data-testid="stButton"] {{
                width: 100% !important;
                max-width: 100% !important;
            }}
        }}

        /* 8. 其他组件配色 */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; }}
    </style>
    """, unsafe_allow_html=True)
