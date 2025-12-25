# engine_manager.py
import streamlit as st
import requests
import base64

# ===========================
# 1. 基础配置
# ===========================
# 🚨 请确认你的 GitHub 仓库名！
# 如果是 tattoo-ai-tool 请改为 "losran/tattoo-ai-tool"
REPO = "losran/mod" 
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

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

# ===========================
# 2. 核心函数
# ===========================
@st.cache_data(ttl=600)
def fetch_repo_data():
    data_map = {}
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    for k, path in WAREHOUSE.items():
        try:
            url = f"https://api.github.com/repos/{REPO}/contents/{path}"
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                content = base64.b64decode(r.json()["content"]).decode()
                data_map[k] = [i.strip() for i in content.splitlines() if i.strip()]
            else:
                data_map[k] = []
        except:
            data_map[k] = []
    return data_map

def save_data(path, data_list):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        old_resp = requests.get(url, headers=headers).json()
        sha = old_resp.get("sha")
        content_str = "\n".join(sorted(list(set(data_list))))
        b64_content = base64.b64encode(content_str.encode()).decode()
        
        payload = {
            "message": "update via engine",
            "content": b64_content,
            "sha": sha
        }
        requests.put(url, headers=headers, json=payload)
        return True
    except Exception as e:
        print(f"Save error: {e}")
        return False

def init_data():
    if "db_all" not in st.session_state:
        st.session_state.db_all = fetch_repo_data()

# ===========================
# 3. 侧边栏渲染 (Render Sidebar)
# ===========================
def render_sidebar():
    # 尝试应用样式
    try:
        from style_manager import apply_pro_style
        apply_pro_style()
    except ImportError:
        pass

    init_data()
    # ✨✨✨ 在这里加入 Logo 代码！ ✨✨✨
    # image 参数写你的文件路径
    # icon_image 参数是当侧边栏收起变窄时显示的小图标（可选，不写也行）
    st.logo("image/logo.png", icon_image="image/logo.png")
    
    with st.sidebar:
        st.title("🚀 引擎控制台")
        st.markdown("---")
        st.markdown("### 📊 实时库存")
        
        if "db_all" in st.session_state:
            for k, v in st.session_state.db_all.items():
                st.markdown(f"**{k}** : `{len(v)}`")
        else:
            st.warning("数据同步中...")
        
        st.markdown("---")
        if st.button("🔄 全局刷新", use_container_width=True):
            st.cache_data.clear()
            st.session_state.db_all = fetch_repo_data()
            st.rerun()
