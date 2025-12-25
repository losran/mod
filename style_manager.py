import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* ==============================
           1. 全局配置
           ============================== */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        .material-icons {{ font-family: 'Material Icons' !important; }}

        /* ==============================
           2. 核心布局修复 (防止遮挡)
           ============================== */
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a !important; 
            border-right: 1px solid #1a1a1a !important;
            z-index: 99998 !important; 
        }}
        [data-testid="stSidebarUserContent"] {{
            padding-top: 3.5rem !important; 
        }}
        [data-testid="stLogo"] {{
            height: auto !important;
            z-index: 99999 !important;
        }}

        /* ==============================
           3. 按钮容器基础样式
           ============================== */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 36px !important;
            height: 36px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            opacity: 1 !important;
            z-index: 100000 !important;
            transition: all 0.2s ease !important;
            margin-top: 0px !important;
            
            /* 关键：隐藏掉原本的 "keyboard_double_arrow..." 文字 */
            color: transparent !important; 
            font-size: 0 !important;
        }}
        
        /* 再次确保原本的 svg 和 span 彻底消失 */
        [data-testid="stHeader"] button svg,
        [data-testid="stHeader"] button span {{ 
            display: none !important; 
        }}


        /* ==============================
           4. 纯 CSS 画箭头 (Geometrical Construction)
           原理：画一个正方形的 上边框 和 右边框，然后旋转
           ============================== */

        /* 通用箭头样式 */
        [data-testid="stHeader"] button::after {{
            content: "" !important;
            display: inline-block !important;
            width: 8px !important;   /* 箭头大小 */
            height: 8px !important;
            border-style: solid !important;
            border-width: 2px 2px 0 0 !important; /* 只保留上和右边框 */
            border-color: #888 !important; /* 默认灰色 */
            transition: all 0.2s ease !important;
            vertical-align: middle !important;
        }}

        /* ---> 状态 A: 侧边栏收起 (画右箭头 >) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{
            transform: rotate(45deg) !important; /* 旋转45度变成 > */
            margin-left: -2px !important; /* 视觉微调居中 */
        }}

        /* <--- 状态 B: 侧边栏展开 (画左箭头 <) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{
            transform: rotate(-135deg) !important; /* 旋转-135度变成 < */
            margin-left: 2px !important; /* 视觉微调居中 */
        }}

        /* Hover 高亮状态 (变白) */
        [data-testid="stHeader"] button:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
        }}
        [data-testid="stHeader"] button:hover::after {{
            border-color: #fff !important; /* 边框变白 */
        }}


        /* ==============================
           5. 其他去噪与配色
           ============================== */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.6) !important; border-bottom: 1px solid #1a1a1a !important; height: 3.5rem !important; }}
        
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        .stApp {{ background-color: #000000; }}
        
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; border-radius: 6px !important; }}
        .stButton > button:hover {{ border-color: #FFFFFF !important; color: #FFFFFF !important; background: #1a1a1a !important; }}
        
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; color: #e0e0e0 !important; }}
    </style>
    """, unsafe_allow_html=True)
