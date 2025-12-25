# engine_manager.py
import streamlit as st
import requests
import base64

# ===========================
# 1. Config
# ===========================
REPO = "losran/mod" # Make sure this is correct
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
# 2. Core Functions
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
# 3. Sidebar Render (English Version)
# ===========================
# 找到 def render_sidebar(): ... 这一整块，替换成下面这样：

def render_sidebar():
    # 引入样式
    try:
        from style_manager import apply_pro_style
        apply_pro_style()
    except ImportError:
        pass

    # 隐藏 Streamlit 自带的导航
    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

    init_data()
    
    with st.sidebar:
        # 1. 顶部 Logo 区域
        if os.path.exists("images/logo.png"):
            st.image("images/logo.png", width=140)
        else:
            st.markdown("### ⚡ MOD ENGINE")

        st.markdown("---")
        
        # 2. 🔥 核心菜单区域 (位置就在 Logo 下面)
        st.markdown("#### 🧭 Navigation") # 加个小标题更好看
        st.page_link("app.py", label="Smart Ingest")
        st.page_link("pages/01_creative.py", label="Creative Engine")
        st.page_link("pages/02_automation.py", label="Automation")

        st.markdown("---")

        # 3. 下半部分：控制台和库存
        st.header("Engine Console")
        st.caption("Live Inventory Stats") # 加个副标题
        
        if "db_all" in st.session_state:
            # 使用 expander 收纳库存，避免太长占位置
            with st.expander("📦 Inventory Details", expanded=True):
                for k, v in st.session_state.db_all.items():
                    st.markdown(f"**{k}** : `{len(v)}`")
        else:
            st.warning("Syncing...")
        
        st.markdown("---")
        if st.button("Refresh All", use_container_width=True):
            st.cache_data.clear()
            st.session_state.db_all = fetch_repo_data()
            st.rerun()
