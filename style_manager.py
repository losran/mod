# style_manager.py
import streamlit as st

def apply_pro_style():
    st.markdown("""
    <style>
        /* =========================
           1. 全局暗黑基础
        ========================= */
        .stApp {
            background-color: #0f1014;
        }
        
        /* 隐藏顶部红线装饰 */
        header[data-testid="stHeader"] {
            background: transparent;
        }
        header[data-testid="stHeader"] > .decoration {
            display: none;
        }

        /* =========================
           2. 侧边栏 (Sidebar) 深度修复
        ========================= */
        /* 侧边栏整体背景和边框 */
        [data-testid="stSidebar"] {
            background-color: #16171d;
            border-right: 1px solid #262730;
        }
        
        /* 🚨 关键修复：给侧边栏内容加呼吸空间，防止贴边 */
        [data-testid="stSidebarUserContent"] {
            padding-top: 1rem;
            padding-left: 1.2rem;   /* 左侧留白 */
            padding-right: 1.2rem;  /* 右侧留白 */
        }

        /* 侧边栏里的文字稍微改小一点，防止换行挤压 */
        [data-testid="stSidebarUserContent"] p {
            font-size: 0.95rem;
            color: #b0b8c3;
        }
        
        /* 侧边栏标题颜色 */
        [data-testid="stSidebarUserContent"] h1, 
        [data-testid="stSidebarUserContent"] h2, 
        [data-testid="stSidebarUserContent"] h3 {
            color: #ffffff;
        }

        /* =========================
           3. 按钮与组件优化
        ========================= */
        /* 主按钮 (Primary) */
        .stButton > button[kind="primary"] {
            background-color: #2e6cff;
            border: none;
            color: white;
            transition: all 0.2s;
        }
        .stButton > button[kind="primary"]:hover {
            background-color: #4b82ff;
            box-shadow: 0 4px 12px rgba(46, 108, 255, 0.3);
        }

        /* 次要按钮 / 普通按钮 */
        .stButton > button[kind="secondary"] {
            background-color: #1a1b23;
            border: 1px solid #363740;
            color: #8b949e;
        }
        
        /* 输入框背景统一 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
            background-color: #16171d !important;
            border: 1px solid #262730 !important;
            color: #e6edf3 !important;
        }

        /* 绿色数字高亮优化 (对应你的 Subject: 121 这种) */
        code {
            background-color: #1c2e26; /* 深绿色背景 */
            color: #4ade80;            /* 亮绿色文字 */
            padding: 2px 6px;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)
