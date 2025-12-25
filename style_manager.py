import streamlit as st

def apply_pro_style():
    # 1. 引入字体
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    icon_url = "https://fonts.googleapis.com/icon?family=Material+Icons"

    st.markdown(f"""
    <style>
        @import url('{font_url}');
        @import url('{icon_url}');

        /* ==================================================
           1. 🧠 核弹级隐藏：彻底消灭顶部栏和它的背景色
        ================================================== */
        /* 隐藏工具栏内容 (Share, Star, Menu) */
        [data-testid="stToolbar"] {{
            visibility: hidden !important;
            display: none !important;
        }}
        
        /* 隐藏顶部彩虹装饰线 */
        [data-testid="stDecoration"] {{
            display: none !important;
        }}
        
        /* 🔥🔥🔥 关键新增：让整个顶部容器透明消失 🔥🔥🔥 */
        [data-testid="stHeader"] {{
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            /* 如果觉得顶部还有空白占位，可以把下面这行注释解开，强制高度为0 */
            /* height: 0px !important; */
        }}
        /* 🔥🔥🔥 局部修正：强制把顶部背景变成透明 🔥🔥🔥 */
        header[data-testid="stHeader"] {
            background: transparent !important;
            background-color: transparent !important; 
        }
        
        /* 顺手把顶部装饰线也藏掉 */
        div[data-testid="stDecoration"] {
            visibility: hidden;
            display: none;
        }

        /* ==================================================
           2. 🩹 修复左上角图标乱码
        ================================================== */
        .material-icons, .material-icons-outlined, .material-icons-two-tone, 
        .material-icons-round, .material-icons-sharp {{
            font-family: 'Material Icons' !important;
        }}

        /* ==================================================
           3. 🎨 滑块与暗黑主题美化
        ================================================== */
        /* 滑块轨道 (深灰) */
        div[data-baseweb="slider"] div {{ background-color: #333 !important; }}
        /* 选中条 (亮银色) */
        div[data-baseweb="slider"] div[class*="css"] {{ background-color: #e0e0e0 !important; }}
        /* 圆点 (纯白发光) */
        div[role="slider"] {{
            background-color: #ffffff !important;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
            border: none !important;
        }}
        /* 数值框 */
        div[data-testid="stThumbValue"] {{
            background-color: #000 !important;
            color: #fff !important;
            border: 1px solid #fff !important;
        }}

        /* 全局背景 */
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
        
        /* 输入框 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        
        /* 按钮 */
        .stButton > button {{
            border-radius: 4px !important;
            border: 1px solid #444 !important;
            background: linear-gradient(180deg, #3a3a3a 0%, #222222 100%) !important;
            color: #ffffff !important;
        }}
    </style>
    """, unsafe_allow_html=True)
