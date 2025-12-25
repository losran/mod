import streamlit as st

def apply_pro_style():
    # 保持字体加载
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 全局字体基础 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}

        /* 2. 侧边栏布局与防遮挡 */
        [data-testid="stSidebar"] {{ background-color: #0a0a0a !important; border-right: 1px solid #1a1a1a !important; z-index: 99998 !important; }}
        [data-testid="stSidebarUserContent"] {{ padding-top: 3.5rem !important; }}
        [data-testid="stLogo"] {{ height: auto !important; z-index: 99999 !important; }}

        /* =======================================================
           🔥🔥🔥 定向清除鬼魂文字 (keyboard_...) 🔥🔥🔥
           ======================================================= */
        
        /* 核心修复：直接抹除按钮内部的所有原生内容 */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"] *,
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] * {{
            display: none !important;      /* 抹除所有内部标签 */
            font-size: 0 !important;       /* 强制字号归零 */
            color: transparent !important; /* 强制透明 */
            width: 0 !important;
            height: 0 !important;
        }}

        /* 3. 按钮容器本身 (作为画板) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 36px !important;
            height: 36px !important;
            position: relative !important;
            z-index: 100000 !important;
            margin-top: 0px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}

        /* =======================================================
           4. 纯 CSS 几何绘制箭头 (伪元素不受 display:none 影响)
           ======================================================= */
        
        /* 箭头骨架 */
        [data-testid="stHeader"] button::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            width: 8px !important;
            height: 8px !important;
            border-top: 2px solid #888 !important;   /* 上边框 */
            border-right: 2px solid #888 !important; /* 右边框 */
            transition: all 0.2s ease !important;
        }}

        /* 收起状态：右箭头 > (旋转45度) */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{
            transform: translate(-65%, -50%) rotate(45deg) !important; 
        }}

        /* 展开状态：左箭头 < (旋转-135度) */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{
            transform: translate(-35%, -50%) rotate(-135deg) !important;
        }}
        /* ==============================
           6. 局部对齐补丁 (f-string 双括号版)
           ============================== */
        /* ==============================
           7. 终极对齐补丁 (强制高度一致)
           ============================== */
        
        /* 1. 强制设定所有列容器为底部对齐 */
        [data-testid="column"] {{
            display: flex !important;
            flex-direction: column !important;
            justify-content: flex-end !important;
        }}

        /* 2. 暴力重写 Number Input (左边的数字框) 的高度 */
        div[data-testid="stNumberInput"] div[data-baseweb="input"] {{
            height: 45px !important;       /* 强制高度 */
            min-height: 45px !important;
            border-radius: 6px !important; /* 圆角与按钮一致 */
            overflow: hidden !important;
            border: 1px solid #333 !important;
            background-color: #111 !important;
        }}

        /* 1. 强制列容器内的所有元素高度撑满并居中对齐 */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}

        /* 2. 强制锁定数字输入框容器的高度 */
        div[data-testid="stNumberInput"] div[data-baseweb="input"] {{
            height: 40px !important;       /* 核心：定死高度 */
            min-height: 40px !important;
            display: flex !important;
            align-items: center !important;
        }}

        /* 3. 强制锁定按钮的高度与输入框一致 */
        div[data-testid="stButton"] button {{
            height: 40px !important;       /* 核心：必须与上面一致 */
            min-height: 40px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            padding-top: 0px !important;
            padding-bottom: 0px !important;
            line-height: 1 !important;
        }}
        
        /* 修正数字框里的输入文字位置，保证居中 */
        div[data-testid="stNumberInput"] input {{
            height: 45px !important;
            line-height: 45px !important;
            padding-top: 0px !important;
            padding-bottom: 0px !important;
            color: #fff !important;
        }}

        /* 3. 暴力重写 Button (右边的按钮) 的高度 */
        div[data-testid="stButton"] button {{
            height: 45px !important;       /* 必须与上面保持一致 */
            min-height: 45px !important;
            line-height: 45px !important;  /* 文字垂直居中 */
            padding-top: 0px !important;
            padding-bottom: 0px !important;
            border: 1px solid #333 !important;
            border-radius: 6px !important;
            margin-top: 0px !important;    /* 防止按钮自带的 margin 捣乱 */
        }}

        /* 4. 再次确保去掉数字框的标题占位 */
        div[data-testid="stNumberInput"] label {{
            display: none !important;
            height: 0 !important;
            margin: 0 !important;
        }}
        /* 强制让列容器内的组件底部对齐 */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}

        /* 彻底移除 number_input 的标题占位和底部边距 */
        div[data-testid="stNumberInput"] label {{
            display: none !important;
        }}
        
        div[data-testid="stNumberInput"] {{
            margin-bottom: 0px !important;
            padding-bottom: 0px !important;
        }}

        /* 统一输入框高度，确保与按钮严丝合缝 */
        [data-testid="stNumberInput"] input {{
            height: 42px !important;
        }}
        /* Hover 反馈 */
        [data-testid="stHeader"] button:hover {{ border-color: #fff !important; background-color: #222 !important; }}
        [data-testid="stHeader"] button:hover::after {{ border-color: #fff !important; }}

        /* 其他去噪处理 */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.6) !important; border-bottom: 1px solid #1a1a1a !important; height: 3.5rem !important; }}
        
        /* 通用组件样式 */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stApp {{ background-color: #000000; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; color: #888 !important; border-radius: 6px !important; }}
        .stButton > button:hover {{ border-color: #FFFFFF !important; color: #FFFFFF !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; color: #e0e0e0 !important; }}
    </style>
    """, unsafe_allow_html=True)
