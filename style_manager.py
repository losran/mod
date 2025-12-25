# style_manager.py
import streamlit as st

def apply_pro_style():
    # 🌟 核心魔法：引入 Google Fonts 网络字体
    # Poppins: 圆润的几何字体，专门治愈"太硬"的英文和数字
    # Noto Sans SC: 谷歌的标准黑体，比系统默认字体更均匀
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"

    st.markdown(f"""
    <style>
        /* 1. 引入字体资源 */
        @import url('{font_url}');

        /* =========================
           2. 全局字体重塑 (核心优化)
        ========================= */
        html, body, [class*="css"], .stApp {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            -webkit-font-smoothing: antialiased; /* 让字体边缘更顺滑，不锯齿 */
        }}
        
        /* 针对输入框、按钮等组件强制生效 */
        .stTextInput, .stTextArea, .stSelectbox, .stButton, .stMarkdown, .stRadio {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
        }}

        /* 代码块/数字标签：使用更现代的等宽字体 */
        code, .stCode {{
            font-family: 'Consolas', 'Monaco', monospace !important;
        }}

        /* =========================
           3. 界面美化 (保留你之前的暗黑风格)
        ========================= */
        /* 背景色 */
        .stApp {{ background-color: #0f1014; }}
        
        /* 隐藏顶部红线 */
        header[data-testid="stHeader"] {{ background: transparent; }}
        header[data-testid="stHeader"] > .decoration {{ display: none; }}

        /* 侧边栏优化 */
        [data-testid="stSidebar"] {{
            background-color: #16171d;
            border-right: 1px solid #262730;
        }}
        [data-testid="stSidebarUserContent"] {{
            padding-top: 20px;
        }}
        
        /* 侧边栏文字优化 */
        [data-testid="stSidebarUserContent"] p, [data-testid="stSidebarUserContent"] span {{
            font-size: 0.9rem;
            color: #9097a3; /*稍微调亮一点灰色，看起来不累*/
            font-weight: 400;
        }}
        
        /* 标题优化：增加一点间距，不那么拥挤 */
        h1, h2, h3 {{
            color: #ffffff !important;
            letter-spacing: 0.5px; /* 字间距微调，更透气 */
        }}

        /* =========================
           4. 组件细节微调
        ========================= */
        /* 按钮：圆角加大，看起来更柔和 */
        .stButton > button {{
            border-radius: 8px !important;
            font-weight: 500 !important;
        }}
        
        /* 主按钮 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #2e6cff 0%, #2554c7 100%); /* 加个微渐变，更有质感 */
            border: none;
            color: white;
            box-shadow: 0 4px 14px rgba(46, 108, 255, 0.2);
        }}

        /* 输入框：柔化边框 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #16171d !important;
            border: 1px solid #2d313a !important;
            color: #e6edf3 !important;
            border-radius: 8px !important; /* 也是圆角 */
        }}
        
        /* 聚焦时的光晕效果 */
        .stTextArea textarea:focus, .stTextInput input:focus {{
            border-color: #2e6cff !important;
            box-shadow: 0 0 0 1px #2e6cff !important;
        }}

        /* 绿色数字标签：更精致 */
        code {{
            background-color: rgba(46, 213, 115, 0.15); /* 半透明背景 */
            color: #2ed573;
            padding: 2px 6px;
            border-radius: 6px;
            font-size: 0.9em;
            border: 1px solid rgba(46, 213, 115, 0.2);
        }}
    </style>
    """, unsafe_allow_html=True)
