import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');
        
        /* 1. 全局配置 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}

        /* 2. 侧边栏布局基础 */
        [data-testid="stSidebar"] {{ background-color: #0a0a0a !important; border-right: 1px solid #1a1a1a !important; z-index: 99998 !important; }}
        [data-testid="stSidebarUserContent"] {{ padding-top: 3.5rem !important; }}
        [data-testid="stLogo"] {{ height: auto !important; z-index: 99999 !important; }}


        /* =======================================================
           🔥🔥🔥 核心修复：定向清除按钮内部的所有子元素 🔥🔥🔥
           ======================================================= */
        
        /* 选中那两个按钮的所有 [直接子元素] */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"] > *,
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] > * {{
            display: none !important; /* 彻底隐藏原本的 Icon/Span/SVG */
        }}

        /* 3. 按钮容器本身 (父亲) - 保持可见，作为载体 */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 36px !important;
            height: 36px !important;
            position: relative !important;
            z-index: 100000 !important;
            transition: all 0.2s ease !important;
            margin-top: 0px !important;
        }}

        /* =======================================================
           4. 重新绘制箭头 (伪元素不受 > *display:none 的影响)
           ======================================================= */
        
        /* 通用箭头骨架 */
        [data-testid="stHeader"] button::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            width: 8px !important;
            height: 8px !important;
            border-top: 2px solid #888 !important;
            border-right: 2px solid #888 !important;
            box-sizing: content-box !important;
            transition: all 0.2s ease !important;
        }}

        /* ---> 状态 A: 侧边栏收起 (右箭头 >) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{
            transform: translate(-65%, -50%) rotate(45deg) !important; 
        }}

        /* <--- 状态 B: 侧边栏展开 (左箭头 <) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{
            transform: translate(-35%, -50%) rotate(-135deg) !important;
        }}

        /* Hover 高亮 */
        [data-testid="stHeader"] button:hover {{ border-color: #fff !important; background-color: #222 !important; }}
        [data-testid="stHeader"] button:hover::after {{ border-color: #fff !important; }}

        /* 其他去噪 */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.6) !important; border-bottom: 1px solid #1a1a1a !important; height: 3.5rem !important; }}
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        .stApp {{ background-color: #000000; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; border-radius: 6px !important; }}
        .stButton > button:hover {{ border-color: #FFFFFF !important; color: #FFFFFF !important; background: #1a1a1a !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; color: #e0e0e0 !important; }}
    </style>
    """, unsafe_allow_html=True)
