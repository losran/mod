# engine_manager.py
import streamlit as st
import requests, base64

# 1. 仓库定义移到这里，方便所有页面调用
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = "losran/mod"

WAREHOUSE = {
    "Subject": "data/subjects.txt",
    "Action": "data/actions.txt",
    "Mood": "data/moods.txt",
    "Usage": "data/usage.txt",
    "StyleSystem": "data/styles_system.txt",
    "Technique": "data/styles_technique.txt",
    "Color": "data/styles_color.txt",
    "Texture": "data/styles_texture.txt",
    "Composition": "data/styles_composition.txt",
    "Accent": "data/styles_accent.txt",
}

# 2. 数据获取函数
@st.cache_data(ttl=600)
def fetch_repo_data():
    data_map = {}
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    for k, path in WAREHOUSE.items():
        try:
            url = f"https://api.github.com/repos/{REPO}/contents/{path}"
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                content = base64.b64decode(r.json()["content"]).decode()
                data_map[k] = [i.strip() for i in content.splitlines() if i.strip()]
            else:
                data_map[k] = []
        except:
            data_map[k] = []
    return data_map

# 3. 初始化 Session 状态 (确保数据存在)
def init_data():
    if "db_all" not in st.session_state:
        st.session_state.db_all = fetch_repo_data()

# 4. 渲染通用侧边栏 (核心组件)
def render_sidebar():
    init_data()
    
    with st.sidebar:
        st.title("🚀 引擎控制台")
        st.markdown("---")
        st.markdown("### 📊 实时库存")
        
        # 显示数据
        if "db_all" in st.session_state:
            for k, v in st.session_state.db_all.items():
                st.markdown(f"**{k}**: `{len(v)}`")
        
        st.markdown("---")
        if st.button("🔄 全局刷新", use_container_width=True):
            st.cache_data.clear()
            st.session_state.db_all = fetch_repo_data()
            st.rerun()
