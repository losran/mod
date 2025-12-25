# style_manager.py
import streamlit as st

def apply_pro_style():
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"

    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* =========================
           1. ⚪ 亮银色主题核心
        ========================= */
        :root {{
            --primary-color: #cccccc !important; /* 核心变量：改成亮灰色，让滑块填充条变亮 */
        }}
        
        /* 强制覆盖红色的组件 */
        *[style*="background-color: rgb(255, 75, 75)"], 
        *[style*="background-color: #ff4b4b"],
        *[style*="background-color: #FF4B4B"] {{
            background-color: #aaaaaa !important;
        }}

        /* =========================
           2. 滑块 (Slider) 高亮修复
        ========================= */
        /* 1. 滑块轨道 (未选中部分) - 深灰 */
        div[data-baseweb="slider"] div {{
            background-color: #333333 !important;
        }}
        
        /* 2. 滑块轨道 (选中/填充部分) - 这部分由 --primary-color 控制，上面已经设为 #cccccc */
        
        /* 3. 滑块圆点 (Handle) - 纯白发光 */
        div[role="slider"] {{
            background-color: #ffffff !important;
            border: 2px solid #ffffff !important;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.5); /* 加个发光效果 */
        }}
        
        /* 4. 数值显示框 */
        div[data-testid="stThumbValue"] {{
            background-color: #222222 !important;
            color: #ffffff !important;
            border: 1px solid #555555 !important;
        }}

        /* =========================
           3. 其他 UI 优化
        ========================= */
        /* 单选框/复选框选中状态 - 亮灰 */
        div[data-baseweb="radio"] div[class*="css"], 
        div[data-baseweb="checkbox"] div[class*="css"] {{
            background-color: #bbbbbb !important;
            border-color: #bbbbbb !important;
        }}

        /* 按钮 */
        .stButton > button {{
            border-radius: 4px !important;
            font-weight: 500 !important;
        }}
        /* 主按钮 (Primary) - 深灰渐变 */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(180deg, #555555 0%, #333333 100%) !important;
            color: #ffffff !important;
            border: 1px solid #666 !important;
        }}
        .stButton > button[kind="primary"]:hover {{
            background: linear-gradient(180deg, #666666 0%, #444444 100%) !important;
            border-color: #999;
        }}
        
        /* 全局背景纯黑 */
        .stApp {{ background-color: #000000; }}
        
        /* 侧边栏背景深灰 */
        [data-testid="stSidebar"] {{
            background-color: #0a0a0a;
            border-right: 1px solid #222;
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
