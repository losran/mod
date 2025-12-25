# style_manager.py
import streamlit as st

def apply_pro_style():
    # 保持 Google Fonts 引入，字体还是要好看
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"

    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* =========================
           1. 核心配色：黑白灰 (Monochrome)
        ========================= */
        :root {{
            --primary-color: #9e9e9e; /* 覆盖默认红色为中性灰 */
            --background-color: #0f1014;
            --secondary-background-color: #16171d;
            --text-color: #e0e0e0;
        }}

        /* ⚪ 滑块 (Slider) - 银灰色质感 */
        div[data-baseweb="slider"] div[class*="css"] {{
            background-color: #666666 !important; /* 轨道颜色 */
        }}
        div[data-testid="stThumbValue"] {{
            background-color: #444444 !important; /* 数值框背景 */
            color: #ffffff !important;
        }}
        div[role="slider"] {{
            background-color: #e0e0e0 !important; /* 滑块头：亮银色 */
            border: 2px solid #ffffff !important;  /* 加个白边，更清晰 */
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
        }}

        /* 🔘 单选框/复选框 (Radio/Checkbox) */
        div[data-baseweb="radio"] div[class*="css"], 
        div[data-baseweb="checkbox"] div[class*="css"] {{
            background-color: #888888 !important; /* 选中时的灰色 */
            border-color: #888888 !important;
        }}
        /* 未选中的框框 */
        div[data-baseweb="checkbox"] div[class*="css"] {{
            border-color: #444444 !important; 
        }}
        /* 选中时的文字高亮：纯白 */
        div[data-baseweb="radio"] label, div[data-baseweb="checkbox"] label {{
            color: #ffffff !important;
        }}

        /* =========================
           2. 按钮 (工业风)
        ========================= */
        .stButton > button {{
            border-radius: 6px !important;
            font-weight: 500 !important;
            transition: all 0.2s ease;
        }}
        
        /* ⚫ 主按钮 (Primary) - 深灰渐变 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(180deg, #4a4a4a 0%, #2b2b2b 100%); /* 经典的按钮立体感 */
            border: 1px solid #555555;
            color: #ffffff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        }}
        .stButton > button[kind="primary"]:hover {{
            background: linear-gradient(180deg, #5a5a5a 0%, #3b3b3b 100%);
            border-color: #777777;
            color: #ffffff;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
        }}
        .stButton > button[kind="primary"]:active {{
            background: #222222;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
        }}

        /* ⚫ 次要按钮 (Secondary) - 隐形 */
        .stButton > button[kind="secondary"] {{
            background-color: transparent;
            border: 1px solid #333333;
            color: #888888;
        }}
        .stButton > button[kind="secondary"]:hover {{
            border-color: #666666;
            color: #ffffff;
            background-color: #1a1a1a;
        }}

        /* =========================
           3. 全局暗黑优化
        ========================= */
        /* 背景色 */
        .stApp {{ background-color: #0d0d0d; }} /* 比之前更黑一点点，增加对比度 */
        
        html, body, [class*="css"] {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            -webkit-font-smoothing: antialiased;
        }}

        /* 侧边栏 */
        [data-testid="stSidebar"] {{
            background-color: #121212; /* 纯正的深灰黑 */
            border-right: 1px solid #222222;
        }}
        
        /* 隐藏顶部红线 */
        header[data-testid="stHeader"] {{ background: transparent; }}
        header[data-testid="stHeader"] > .decoration {{ display: none; }}

        /* 标题文字：稍微降低一点纯白，用灰白更护眼 */
        h1, h2, h3 {{
            color: #eeeeee !important;
            letter-spacing: 0.5px;
        }}
        p, span, label {{
            color: #a0a0a0 !important;
        }}

        /* 输入框：极简黑 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #1a1a1a !important;
            border: 1px solid #333333 !important;
            color: #d0d0d0 !important;
            border-radius: 6px !important;
        }}
        .stTextArea textarea:focus, .stTextInput input:focus {{
            border-color: #888888 !important; /* 聚焦变成亮灰 */
            box-shadow: none !important;
        }}

        /* 标签：黑底灰字 */
        code {{
            background-color: #222222;
            color: #bbbbbb;
            border: 1px solid #333333;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Consolas', monospace !important;
        }}
        
        /* 链接颜色 (如果有) */
        a {{
            color: #bbbbbb !important;
            text-decoration: underline;
        }}
    </style>
    """, unsafe_allow_html=True)
