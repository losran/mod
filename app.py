import streamlit as st
import requests, base64
from openai import OpenAI

# 1. 页面配置
st.set_page_config(layout="wide", page_title="Creative Engine")

# 尝试加载样式（可选，如果报错也不影响运行）
try:
    from style_manager import apply_pro_style
    apply_pro_style()
except ImportError:
    pass

# ======================
# 核心配置与函数
# ======================
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_KEY"], 
    base_url="https://api.deepseek.com"
)
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

# 缓存数据，避免重复请求导致卡顿
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

def save_data(path, data):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    try:
        old = requests.get(url, headers=headers).json()
        content = "\n".join(sorted(set(data)))
        payload = {
            "message": "update",
            "content": base64.b64encode(content.encode()).decode(),
            "sha": old["sha"]
        }
        requests.put(url, headers=headers, json=payload)
    except Exception as e:
        st.error(f"保存失败: {e}")

# 初始化 Session State
if "db_all" not in st.session_state:
    st.session_state.db_all = fetch_repo_data()
if "ai_results" not in st.session_state:
    st.session_state.ai_results = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ======================
# 布局开始
# ======================

# 🟢 侧边栏：库存状态
with st.sidebar:
    st.title("🚀 引擎控制台")
    st.markdown("---")
    st.markdown("### 📊 实时库存")
    
    # 遍历显示数据
    for k, v in st.session_state.db_all.items():
        st.markdown(f"**{k}**: `{len(v)}`")
        
    st.markdown("---")
    if st.button("🔄 刷新数据", use_container_width=True):
        st.cache_data.clear()
        st.session_state.db_all = fetch_repo_data()
        st.rerun()

# 🔵 主区域：两列布局
center, right = st.columns([4, 2])

# 中间列：智能入库
with center:
    st.subheader("⚡ 智能入库")
    st.session_state.input_text = st.text_area("输入灵感描述", st.session_state.input_text, height=200)

    if st.button("🚀 AI 拆分", type="primary", use_container_width=True):
        with st.spinner("正在分析语义..."):
            prompt = f"将内容拆分为最小中文关键词。分类：Subject/Action/Style/Mood/Usage。格式：Category:Word1,Word2|... 内容：{st.session_state.input_text}"
            try:
                res = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1
                ).choices[0].message.content
                
                parsed = []
                clean = res.replace("：", ":").replace("\n", "|")
                for block in clean.split("|"):
                    if ":" in block:
                        cat, words = block.split(":", 1)
                        for k in WAREHOUSE:
                            if k.lower() in cat.lower():
                                for w in words.split(","):
                                    if w.strip():
                                        parsed.append({"cat": k, "val": w.strip()})
                st.session_state.ai_results = parsed
            except Exception as e:
                st.error(f"AI 响应错误: {e}")

    # 显示拆分结果
    if st.session_state.ai_results:
        st.write("---")
        st.caption("勾选确认入库项：")
        selected = []
        cols = st.columns(3)
        for i, item in enumerate(st.session_state.ai_results):
            with cols[i % 3]:
                if st.checkbox(f"{item['cat']} · {item['val']}", value=True, key=f"chk_{i}"):
                    selected.append(item)
        
        if st.button("📥 确认写入数据库", type="secondary"):
            for item in selected:
                path = WAREHOUSE[item["cat"]]
                current_list = st.session_state.db_all.get(item["cat"], [])
                if item["val"] not in current_list:
                    current_list.append(item["val"])
                    save_data(path, current_list)
            
            st.cache_data.clear()
            st.session_state.db_all = fetch_repo_data()
            st.session_state.ai_results = []
            st.success("入库完成！")
            st.rerun()

# 右侧列：仓库管理
with right:
    st.subheader("📦 仓库管理")
    cat_
