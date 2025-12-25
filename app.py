import streamlit as st
import requests, base64, time
from openai import OpenAI
from style_manager import apply_pro_style
# 🔢 左下角库存状态（实时 GitHub）
real_counts = {
    k: len(get_data(v))
    for k, v in FILES.items()
}
render_unified_sidebar(real_counts)


# --- 1. 页面配置 ---
st.set_page_config(layout="wide", page_title="Tattoo AI Workbench")

# --- 2. API 配置 ---
client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = "losran/tattoo-ai-tool"

FILES = {
    "Subject": "subjects.txt",
    "Action": "actions.txt",

    # ✅ 新 Style 拆分
    "StyleSystem": "styles_system.txt",
    "Technique": "styles_technique.txt",
    "Color": "styles_color.txt",
    "Texture": "styles_texture.txt",
    "Composition": "styles_composition.txt",
    "Accent": "styles_accent.txt",

    "Mood": "moods.txt",
    "Usage": "usage.txt"
}


# --- 3. GitHub IO ---
def get_data(filename):
    url = f"https://api.github.com/repos/{REPO}/contents/data/{filename}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return [
            x.strip()
            for x in base64.b64decode(r.json()["content"]).decode().splitlines()
            if x.strip()
        ]
    return []

def sync_data(filename, data):
    url = f"https://api.github.com/repos/{REPO}/contents/data/{filename}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    sha = requests.get(url, headers=headers).json().get("sha")
    content = base64.b64encode("\n".join(sorted(set(data))).encode()).decode()
    requests.put(
        url,
        headers=headers,
        json={"message": "sync", "content": content, "sha": sha},
    )

# --- 4. 状态初始化 ---
if "db" not in st.session_state:
    st.session_state.db = {k: get_data(v) for k, v in FILES.items()}

if "ai_results" not in st.session_state:
    st.session_state.ai_results = []

if "input_val" not in st.session_state:
    st.session_state.input_val = ""

if "is_open" not in st.session_state:
    st.session_state.is_open = True

# --- 5. 样式 ---
apply_pro_style()

# --- 6. 布局 ---
if st.session_state.is_open:
    col_main, col_right = st.columns([5, 2])
else:
    col_main = st.container()

# ================= 主区 =================
with col_main:
    st.title("⚡ 智能入库")

    user_text = st.text_area(
        "提示词编辑区",
        value=st.session_state.input_val,
        height=300,
        label_visibility="collapsed",
    )
    st.session_state.input_val = user_text

    if st.button("🚀 开始 AI 拆解", use_container_width=True):
        if user_text:
            with st.spinner("解析中..."):
                prompt = f"""
你是一位【强迫症级别的关键词拆解师】。
请将用户的描述【粉碎】为最细小的独立中文标签。

【硬性规则】
1. 每个标签必须是【单词级】，禁止长句
2. 不得造词，只拆词
3. 必须严格归类
4. 纯中文输出

【分类定义】
Subject：主体、生物、物体、材质
Action：动作、状态
StyleSystem：艺术流派 / 体系（如 日式, 美式, 赛博）
Technique：绘制 / 表现技法（如 线描, 黑线, 水彩）
Color：颜色（如 黑色, 朱红）
Texture：材质 / 肌理（如 金属, 粗糙）
Composition：构图（如 对称, 居中）
Accent：装饰点（如 火焰, 符号）
Mood：情绪
Usage：纹身部位

【原文】
{user_text}

【输出格式】
Subject:词1,词2|Action:词1|StyleSystem:词1|Technique:词1|Color:词1|Texture:词1|Composition:词1|Accent:词1|Mood:词1|Usage:词1
"""

                res = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1,
                ).choices[0].message.content

                parsed = []
                clean = res.replace("：", ":").replace("\n", "|")
                for seg in clean.split("|"):
                    if ":" in seg:
                        cat, vals = seg.split(":", 1)
                        for k in FILES:
                            if k.lower() in cat.lower():
                                for v in vals.split(","):
                                    v = v.strip()
                                    if v:
                                        parsed.append({"cat": k, "val": v})

                st.session_state.ai_results = parsed
                st.rerun()

    # ---- 入库预览 ----
    if st.session_state.ai_results:
        st.divider()
        st.subheader("拆解结果")

        selected = []
        for cat in FILES:
            items = [x for x in st.session_state.ai_results if x["cat"] == cat]
            if items:
                st.markdown(f"**{cat}**")
                cols = st.columns(4)
                for i, it in enumerate(items):
                    with cols[i % 4]:
                        if st.checkbox(it["val"], value=True, key=f"{cat}_{i}"):
                            selected.append(it)

        if st.button("📥 一键入库", type="primary", use_container_width=True):
            for it in selected:
                cat = it["cat"]
                if it["val"] not in st.session_state.db[cat]:
                    st.session_state.db[cat].append(it["val"])
                    sync_data(FILES[cat], st.session_state.db[cat])
            st.session_state.ai_results = []
            st.success("已入库")
            time.sleep(0.3)
            st.rerun()

# ================= 仓库区 =================
if st.session_state.is_open:
    with col_right:
        st.subheader("📦 仓库")
        cat_view = st.selectbox("分类", FILES.keys())
        words = st.session_state.db[cat_view]

        if words:
            with st.container(height=600):
                for i, w in enumerate(words):
                    c1, c2 = st.columns([4, 1])
                    with c1:
                        if st.button(w, key=f"add_{i}", use_container_width=True):
                            st.session_state.input_val += f" {w}"
                            st.rerun()
                    with c2:
                        if st.button("✕", key=f"del_{i}"):
                            new_list = [x for x in words if x != w]
                            st.session_state.db[cat_view] = new_list
                            sync_data(FILES[cat_view], new_list)
                            st.rerun()
        else:
            st.caption("暂无数据")
