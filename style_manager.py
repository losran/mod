# style_manager.py
import streamlit as st

def apply_pro_style():
    # 引入 Google Fonts
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"

    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* =========================
           1. ☢️ 核弹级去红 (覆盖系统变量)
        ========================= */
        :root {{
            --primary-color: #888888 !important; /* 把系统默认的红色变量强制改成灰色 */
        }}
        
        /* 强制覆盖所有使用了系统红色的组件 */
        *[style*="background-color: rgb(255, 75, 75)"], 
        *[style*="background-color: #ff4b4b"],
        *[style*="background-color: #FF4B4B"] {{
            background-color: #666666 !important;
        }}

        /* =========================
           2. 滑块 (Slider) 深度定制
        ========================= */
        /* 滑轨底色 */
        div[data-baseweb="slider"] div {{
            background-color: #333333 !important;
        }}
        
        /* 滑块头 (那个圆点) */
        div[role="slider"] {{
            background-color: #e0e0e0 !important;
            border: 2px solid #000000 !important;
            box-shadow: 0 0 10px rgba(255,255,255,0.1);
        }}
        
        /* 滑块数值显示框 */
        div[data-testid="stThumbValue"] {{
            background-color: #222222 !important;
            color: #cccccc !important;
            border: 1px solid #444444 !important;
        }}

        /* =========================
           3. 其他组件黑灰化
        ========================= */
        /* 单选框/复选框选中状态 */
        div[data-baseweb="radio"] div[class*="css"], 
        div[data-baseweb="checkbox"] div[class*="css"] {{
            background-color: #666666 !important;
            border-color: #666666 !important;
        }}

        /* 按钮 */
        .stButton > button {{
            border-radius: 4px !important;
            font-weight: 500 !important;
            border: 1px solid #444 !important;
        }}
        /* 主按钮 (Primary) - 深灰渐变 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(180deg, #3a3a3a 0%, #222222 100%) !important;
            color: #ffffff !important;
        }}
        .stButton > button[kind="primary"]:hover {{
            border-color: #888;
            color: #fff;
        }}
        
        /* =========================
           4. 全局界面 (暗黑)
        ========================= */
        .stApp {{ background-color: #000000; }} /* 极致纯黑背景 */
        
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #1a1a1a;
        }}
        
        h1, h2, h3, p, span, label, div {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0 !important;
        }}
        
        /* 输入框 */
        .stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {{
            background-color: #111111 !important;
            border: 1px solid #333333 !important;
            color: #e0e0e0 !important;
            border-radius: 4px !important;
        }}
        
        /* 标签 Tag */
        code {{
            background-color: #222;
            color: #aaa;
            border: 1px solid #333;
        }}
    </style>
    """, unsafe_allow_html=True)
