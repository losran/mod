import streamlit as st
import requests, base64
from openai import OpenAI

# ======================
# 基础配置
# ======================
st.set_page_config(layout="wide", page_title="Creative Engine")


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

    # Style 系统（完整）
    "StyleSystem": "data/styles_system.txt",
    "Technique": "data/styles_technique.txt",
    "Color": "data/styles_color.txt",
    "Texture": "data/styles_texture.txt",
    "Composition": "data/styles_composition.txt",
    "Accent": "data/styles_accent.txt",
}



# ======================
# GitHub 工具函数（唯一数据源）
# ======================
def get_data(path):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return []
    content = base64.b64decode(r.json()["content"]).decode()
    return [i.strip() for i in content.splitlines() if i.strip()]

def save_data(path, data):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    old = requests.get(url, headers=headers).json()
    content = "\n".join(sorted(set(data)))
    payload = {
        "message": "update",
        "content": base64.b64encode(content.encode()).decode(),
        "sha": old["sha"]
    }
    requests.put(url, headers=headers, json=payload)

db_all = {
    k: get_data(path)
    for k, path in WAREHOUSE.items()
}
# ======================
# Session 初始化（只存 UI 状态）
# ======================
if "ai_results" not in st.session_state:
    st.session_state.ai_results = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ======================
# 页面布局
# ======================
# 删掉 left，只保留中间和右侧
center, right = st.columns([4, 2])


# 侧边栏：📊 库存状态
# ======================
with st.sidebar:
    st.title("🚀 Creative Engine") # 可以在侧边栏加个标题
    st.markdown("---")
    st.markdown("### 📊 库存状态")
    
    # 注意：这里改用 db_all 以提高加载速度，避免重复请求 GitHub
    for k in WAREHOUSE.keys():
        count = len(db_all.get(k, []))
        # 使用 metric 组件看起来更专业
        st.write(f"**{k}** : `{count}`") 
    
    st.markdown("---")
    if st.button("🔄 刷新仓库数据", use_container_width=True):
        st.rerun()
# ======================
# 中间：⚡ 智能拆分 & 入库
# ======================
with center:
    st.markdown("## ⚡ 智能入库")

    st.session_state.input_text = st.text_area(
        "输入描述",
        st.session_state.input_text,
        height=220
    )

    if st.button("🚀 开始 AI 拆分", use_container_width=True):
        prompt = f"""
        将下列内容拆分为最小中文关键词。
        分类：Subject / Action / Style / Mood / Usage
        用 | 分隔分类，用逗号分隔词。

        内容：{st.session_state.input_text}
        """
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
                            w = w.strip()
                            if w:
                                parsed.append({"cat": k, "val": w})
        st.session_state.ai_results = parsed

    if st.session_state.ai_results:
        st.markdown("### 🧠 拆分结果（勾选后入库）")
        selected = []
        for item in st.session_state.ai_results:
            if st.checkbox(f'{item["cat"]} · {item["val"]}', key=f'{item["cat"]}_{item["val"]}'):
                selected.append(item)

        if st.button("📥 确认入库", type="primary"):
            for item in selected:
                path = WAREHOUSE[item["cat"]]
                current = get_data(path)
                if item["val"] not in current:
                    current.append(item["val"])
                    save_data(path, current)
            st.session_state.ai_results = []
            st.success("已写入 GitHub")

# ======================
# 右侧：📦 仓库内容（可点 / 可删）
# ======================
with right:
    st.markdown("## 📦 仓库")
    cat = st.selectbox("分类", list(WAREHOUSE.keys()))
    words = get_data(WAREHOUSE[cat])

    with st.container(height=500):
        for w in words:
            c1, c2 = st.columns([4, 1])
            with c1:
                if st.button(w, key=f"add_{w}", use_container_width=True):
                    st.session_state.input_text += f" {w}"
            with c2:
                if st.button("✕", key=f"del_{w}"):
                    new = [i for i in words if i != w]
                    save_data(WAREHOUSE[cat], new)
                    st.rerun()
