import streamlit as st

def apply_pro_style():
    # 依然引入字体，保证其他地方好看
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* ==============================
           1. 全局字体配置
           ============================== */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}

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
           3. 按钮容器：核弹级消音 (The Nuclear Option)
           ============================== */
        /* 针对这两个特定的按钮 ID */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            /* 1. 基础盒子样式 */
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 36px !important;
            height: 36px !important;
            position: relative !important; /* 关键：给箭头做定位基准 */
            z-index: 100000 !important;
            transition: all 0.2s ease !important;
            margin-top: 0px !important;

            /* 2. 核心消音逻辑：强制父容器无字 */
            color: transparent !important;   /* 文字变透明 */
            font-size: 0 !important;         /* 字号变0，物理消失 */
            line-height: 0 !important;       /* 行高变0 */
            text-indent: -9999px !important; /* 把文字踢出屏幕外 */
            overflow: visible !important;    /* 允许我们的自定义箭头露出来 */
        }}

        /* 双重保险：把里面的 svg/span 也全隐藏 */
        [data-testid="stHeader"] button svg, 
        [data-testid="stHeader"] button span {{
            display: none !important;
            opacity: 0 !important;
        }}


        /* ==============================
           4. 纯 CSS 箭头：重新显形
           由于父容器 font-size 是 0，这里不用 content 字符，而是用 border 画图
           ============================== */
        
        /* 箭头的通用骨架 */
        [data-testid="stHeader"] button::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            
            /* 强制定位到盒子正中心 */
            top: 50% !important;
            left: 50% !important;
            
            /* 画一个 8px 的直角 */
            width: 8px !important;
            height: 8px !important;
            border-top: 2px solid #888 !important;   /* 上边框 */
            border-right: 2px solid #888 !important; /* 右边框 */
            
            /* 即使父元素 text-indent 飞了，我们把它拉回来 */
            text-indent: 0 !important; 
            box-sizing: content-box !important;
            transition: all 0.2s ease !important;
        }}

        /* ---> 状态 A: 侧边栏收起 (画右箭头 >) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{
            /* 居中 (-65%, -50%) + 旋转 45度 */
            transform: translate(-65%, -50%) rotate(45deg) !important; 
        }}

        /* <--- 状态 B: 侧边栏展开 (画左箭头 <) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{
            /* 居中 (-35%, -50%) + 旋转 -135度 */
            transform: translate(-35%, -50%) rotate(-135deg) !important;
        }}

        /* Hover 高亮 */
        [data-testid="stHeader"] button:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
        }}
        [data-testid="stHeader"] button:hover::after {{
            border-color: #fff !important;
        }}


        /* ==============================
           5. 其他去噪
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
