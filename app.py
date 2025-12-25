import streamlit as st
import requests, base64
from openai import OpenAI

# ======================
# 基础配置
# ======================
st.set_page_config(layout="wide", page_title="Creative Engine")

# 引入自定义样式（如果你的 style_manager.py 还在的话）
try:
    from style_manager import apply_pro_style
    apply_pro_style()
except:
    pass

# 使用缓存避免重复请求 GitHub，只有手动刷新或数据更改时才重新获取
@st.cache_data(show_spinner="正在同步仓库...", ttl=3600)
def fetch_all_db():
    return {k: get_data(path) for k, path in WAREHOUSE.items()}

# 初始化数据
if "db_all" not in st.session_state:
    st.session_state.db_all = fetch_all_db()

# ... (keep get_data, save_data, client config as is) ...

# ======================
# 侧边栏：强制置顶
# ======================
with st.sidebar:
    st.header("📊 库存状态")
    # 使用 container 确保内容紧凑
    with st.container():
        for k in WAREHOUSE.keys():
            # 从 session_state 读取，速度极快
            count = len(st.session_state.db_all.get(k, []))
            st.write(f"**{k}**: `{count}`")
    
    if st.button("🔄 同步最新数据", use_container_width=True):
        st.cache_data.clear() # 清除缓存
        st.session_state.db_all = fetch_all_db()
        st.rerun()

# ======================
# 主页面布局
# ======================
# 确保这里只有两列
center, right = st.columns([4, 2])

with center:
    st.markdown("## ⚡ 智能入库")
    # ... (你的 AI 拆分逻辑代码) ...
    # 注意：入库成功后要记得更新 session_state.db_all
    if st.button("📥 确认入库", type="primary"):
        # ... 入库逻辑 ...
        st.cache_data.clear() # 强制下次加载取新数据
        st.session_state.db_all = fetch_all_db()
        st.success("已写入 GitHub")
        st.rerun()

with right:
    st.markdown("## 📦 仓库")
    # 这里的下拉框也从缓存读取
    cat = st.selectbox("分类选择", list(WAREHOUSE.keys()))
    words = st.session_state.db_all.get(cat, [])
    # ... (你的仓库展示逻辑代码) ...
