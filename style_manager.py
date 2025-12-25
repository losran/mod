import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 全局字体基础 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        .stApp {{ background-color: #000000; }}

        /* 2. 侧边栏与头部基础 */
        [data-testid="stSidebar"] {{ background-color: #0a0a0a !important; border-right: 1px solid #1a1a1a !important; }}
        [data-testid="stSidebarUserContent"] {{ padding-top: 5rem !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.8) !important; border-bottom: 1px solid #1a1a1a !important; }}
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}

        /* =======================================================
           🔥🔥🔥 定向手术：只修左边乱码，不碰右边菜单 🔥🔥🔥
           ======================================================= */
        
        /* 针对左边那个会显示 keyboard_... 的按钮进行定点清理 */
        button[data-testid="stSidebarCollapsedControl"],
        button[data-testid="stSidebarExpandedControl"] {{
            color: transparent !important;
            font-size: 0 !important;
            border: 1px solid #333 !important;
            background-color: #111 !important;
            width: 34px !important;
            height: 34px !important;
            position: relative !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}

        /* 屏蔽左边按钮内部的所有原生文字/图标标签 */
        button[data-testid="stSidebarCollapsedControl"] *,
        button[data-testid="stSidebarExpandedControl"] * {{
            display: none !important;
        }}

        /* 在左边按钮上画出我们专属的三条杠 */
        button[data-testid="stSidebarCollapsedControl"]::after,
        button[data-testid="stSidebarExpandedControl"]::after {{
            content: "" !important;
            position: absolute !important;
            width: 18px !important;
            height: 2px !important;
            background-color: #888 !important;
            box-shadow: 0 -6px 0 #888, 0 6px 0 #888 !important;
            display: block !important;
        }}

        /* 💡 关键：右边的原生菜单 (stAppViewBlockContainer 等) 不要被伪元素覆盖 */
        /* 我们这里不需要写额外代码，因为上面的选择器已经通过 testid 限制在左边按钮了 */

        /* =======================================================
           3. 核心对齐锁死 (42px)
           ======================================================= */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stButton"] button {{
            height: 42px !important;
            min-height: 42px !important;
        }}
        div[data-testid="stNumberInput"] label {{ display: none !important; }}
        div[data-testid="stNumberInput"] input {{ height: 42px !important; }}
        div[data-testid="stButton"] button p {{ line-height: 42px !important; margin: 0 !important; }}

        /* 响应式适配 */
        @media (max-width: 1024px) {{
            [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; gap: 10px !important; }}
            [data-testid="column"] {{ flex: 1 1 auto !important; min-width: 130px !important; }}
        }}

        :root {{ --primary-color: #C0C0C0 !important; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; }}
    </style>
    """, unsafe_allow_html=True)
    """, unsafe_allow_html=True)
