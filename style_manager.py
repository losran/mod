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
           1. ⚪ 银色滑块 (Silver Slider)
        ================================================== */
        :root {{ --primary-color: #C0C0C0 !important; --text-color: #E0E0E0 !important; }}
        div[role="slider"] {{
            background-color: #FFFFFF !important;
            box-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;
            border: 1px solid #C0C0C0 !important;
        }}
        div[data-testid="stThumbValue"] {{ background-color: #1a1a1a !important; border: 1px solid #555 !important; }}

        /* ==================================================
           2. 🖱️ 按钮交互：多选状态系统
        ================================================== */
        
        /* A. 【未选中】暗黑状态 (Secondary) */
        .stButton > button[kind="secondary"] {{
            border: 1px solid #333 !important;
            background: #111 !important;
            color: #888 !important;
            transition: all 0.2s ease-in-out !important;
        }}
        .stButton > button[kind="secondary"]:hover {{
            border-color: #666 !important;
            color: #ccc !important;
        }}

        /* B. 【已选中】亮银状态 (Primary) - 永久高亮！ */
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #e0e0e0 0%, #ffffff 100%) !important;
            color: #000000 !important;
            border: 1px solid #FFFFFF !important;
            box-shadow: 0 0 12px rgba(255, 255, 255, 0.4) !important; /* 银色光晕 */
            font-weight: 700 !important;
            transform: scale(1.02);
        }}
        .stButton > button[kind="primary"]:hover {{
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.7) !important;
        }}

        /* C. 基础清理 */
        header[data-testid="stHeader"] {{ background: transparent !important; }}
        [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
        .stApp {{ background-color: #000000; }}
        [data-testid="stSidebar"] {{ background-color: #0a0a0a; border-right: 1px solid #1a1a1a; }}
        h1, h2, h3, p, span, label, div {{ font-family: 'Poppins', 'Noto Sans SC', sans-serif !important; color: #d0d0d0; }}
        .stButton > button {{ border-radius: 6px !important; }}
        
        /* 修复图标显示 */
        .material-icons, .material-icons-outlined {{ font-family: 'Material Icons' !important; }}
    </style>
    """, unsafe_allow_html=True)
