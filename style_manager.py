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
        
        /* 隐藏 Header 和装饰条，让界面更像 App */
        [data-testid="stHeader"] {
            background: transparent !important;
        }
        [data-testid="stHeader"] > div:first-child {
            display: none !important;
        }

        /* =========================
           2. 侧边栏 (Sidebar) 美化
           对应 Python 中的 with st.sidebar:
        ========================= */
        [data-testid="stSidebar"] {
            background-color: #16171d;
            border-right: 1px solid #262730;
        }
        
        /* 调整侧边栏宽度，让它看起来不那么挤 */
        [data-testid="stSidebar"] > div:first-child {
            width: 300px; /* 如果觉得太宽可以改小，比如 260px */
        }

        /* =========================
           3. 按钮与交互组件风格
        ========================= */
        /* 主按钮 (Primary) - 比如“确认入库” */
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

        /* 次要按钮 (Secondary) - 比如“删除” */
        .stButton > button[kind="secondary"] {
            background-color: #1a1b23;
            border: 1px solid #363740;
            color: #8b949e;
        }
        .stButton > button[kind="secondary"]:hover {
            border-color: #6e7681;
            color: #e6edf3;
        }
        
        /* 输入框样式 */
        .stTextArea textarea {
            background-color: #16171d;
            border: 1px solid #262730;
            color: #e6edf3;
        }
        .stTextArea textarea:focus {
            border-color: #2e6cff;
            box-shadow: none;
        }

        /* =========================
           4. 视觉微调
        ========================= */
        /* 分割线颜色 */
        hr {
            border-color: #262730 !important;
        }
        
        /* Metric 组件数值颜色 */
        [data-testid="stMetricValue"] {
            color: #e6edf3;
        }
        [data-testid="stMetricLabel"] {
            color: #8b949e;
        }
    </style>
    """, unsafe_allow_html=True)
