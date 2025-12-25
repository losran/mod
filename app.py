# app.py
import streamlit as st
from openai import OpenAI
import requests, base64
from style_manager import apply_pro_style
from engine_manager import render_sidebar, WAREHOUSE, save_data # 引入我们刚才写的模块

st.set_page_config(layout="wide", page_title="Creative Engine")
apply_pro_style()  # 应用 CSS

# ✅ 一行代码调用侧边栏 (所有页面都只要加这一行)
render_sidebar()

# ... (保留你的 OpenAI 初始化) ...
client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")

# ... (中间的 session_state 初始化逻辑保持不变) ...

# 布局
center, right = st.columns([4, 2])

with center:
    st.subheader("⚡ 智能入库")
    # ... (你的 AI 拆分逻辑保持不变) ...
    # 记得：如果入库成功，需要调用 st.rerun() 来刷新侧边栏数字

with right:
    st.subheader("📦 仓库管理")
    # 修复之前的报错：正确使用变量名
    cat_view = st.selectbox("查看分类", list(WAREHOUSE.keys()))
    
    # 从 session 读取数据
    if "db_all" in st.session_state:
        words_view = st.session_state.db_all.get(cat_view, [])
        
        with st.container(height=600):
            for w in words_view:
                c1, c2 = st.columns([0.8, 0.2])
                c1.text(w)
                # ... (删除按钮逻辑) ...
