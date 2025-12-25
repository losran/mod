# style_manager.py
import streamlit as st

def apply_pro_style():
    st.markdown("""
    <style>
        /* =========================
           全局基础
        ========================= */
        .stApp { background-color: #0f1014; }
        [data-testid="stHeader"] { background: transparent !important; }
        [data-testid="stHeader"] > div:first-child { display: none !important; }

        /* =========================
           右侧仓库（固定）
        ========================= */
        #warehouse-panel {
            position: fixed;
            right: 0;
            top: 0;
            width: 300px;
            height: 100vh;
            background: #16171d;
            border-left: 1px solid #262730;
            padding: 24px 16px;
            overflow-y: auto;
            z-index: 50;
        }

        /* =========================
           左下角库存状态（固定）
        ========================= */
        #inventory-panel {
            position: fixed;
            left: 300px;   /* ← 这里！！ */
            bottom: 20px;
            width: 220px;
            background: rgba(22,23,29,0.95);
            border: 1px solid #262730;
            border-radius: 12px;
            padding: 14px;
            z-index: 60;
        }


        #inventory-panel h4 {
            margin: 0 0 10px 0;
            font-size: 14px;
        }

        .inv-item {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            color: #8b949e;
            margin-bottom: 4px;
        }

        /* =========================
           中央内容防遮挡
        ========================= */
        .main-content {
            margin-right: 320px;
            padding-bottom: 120px;
        }

        /* =========================
           标签按钮视觉
        ========================= */
        .tag-pill {
            display: flex;
            align-items: center;
            background: #1a1b23;
            border: 1px solid #262730;
            border-radius: 6px;
            padding: 6px 10px;
            margin-bottom: 6px;
        }
    </style>
    """, unsafe_allow_html=True)
