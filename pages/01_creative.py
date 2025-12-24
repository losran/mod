import streamlit as st
import random
import requests
import base64
from openai import OpenAI

# ================== 页面配置 ==================
st.set_page_config(layout="wide", page_title="Creative Engine")

# ================== OpenAI / DeepSeek ==================
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_KEY"],
    base_url="https://api.deepseek.com"
)

# ================== GitHub 仓库配置（仅后台） ==================
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = "losran/tattoo-ai-tool"

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
    "Accent": "data/styles_accent.txt"
}

# ================== Session State ==================
if "generated_cache" not in st.session_state:
    st.session_state.generated_cache = []

if "selected_prompts" not in st.session_state:
    st.session_state.selected_prompts = []

if "polished_text" not in st.session_state:
    st.session_state.polished_text = ""

# ================== 工具函数 ==================
def get_github_data(path):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()["content"]).decode()
        return [l.strip() for l in content.splitlines() if l.strip()]
    return []


def chaos_pick(chaos, low, mid, high):
    if chaos < 30:
        return random.randint(*low)
    elif chaos < 70:
        return random.randint(*mid)
    else:
        return random.randint(*high)


def smart_sample_with_ai(category, user_intent, inventory, chaos_val):
    """
    - 只允许从仓库 inventory 中取词
    - AI 不得造词
    """
    if not inventory:
        return []

    shuffled_pool = random.sample(inventory, min(len(inventory), 40))
    temp = chaos_val / 100.0

    if not user_intent.strip():
        return random.sample(shuffled_pool, min(2, len(shuffled_pool)))

    if chaos_val < 20:
        guide = "挑选最稳定、最协调的词"
    elif chaos_val < 60:
        guide = "挑选具有张力但不突兀的词"
    else:
        guide = "挑选反差最大、最冷门的词"

    prompt = f"""
    分类：{category}
    词库：{shuffled_pool}

    规则：
    1. 只能从词库中选择，不得新增词语
    2. {guide}
    3. 返回 1-2 个词
    4. 只输出词语，用逗号分隔
    """

    try:
        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp
        )
        raw = res.choices[0].message.content
        words = [w.strip() for w in raw.replace("，", ",").split(",") if w.strip()]
        valid = [w for w in words if w in shuffled_pool]
        return valid if valid else random.sample(shuffled_pool, 1)
    except Exception:
        return random.sample(shuffled_pool, 1)


# ================== UI ==================
st.title("🎨 Creative Engine")

chaos_level = st.slider("混乱度", 0, 100, 55)
num = st.number_input("生成数量", 1, 10, 6)
intent_input = st.text_area("创作意图", placeholder="例如：青蛙 / 日式 / emo")

if st.button("🔥 激发组合", type="primary", use_container_width=True):
    st.session_state.polished_text = ""
    st.session_state.selected_prompts = []

    # 👉 后台读取真实仓库
    db = {k: get_github_data(v) for k, v in WAREHOUSE.items()}

    new_batch = []

    subjects = smart_sample_with_ai("主体", intent_input, db["Subject"], chaos_level)
    actions  = smart_sample_with_ai("动作", intent_input, db["Action"], chaos_level)
    moods    = smart_sample_with_ai("情绪", intent_input, db["Mood"], chaos_level)
    usages   = smart_sample_with_ai("部位", intent_input, db["Usage"], chaos_level)

    stylesys = smart_sample_with_ai("系统", intent_input, db["StyleSystem"], chaos_level)
    tech     = smart_sample_with_ai("技法", intent_input, db["Technique"], chaos_level)
    color    = smart_sample_with_ai("色彩", intent_input, db["Color"], chaos_level)
    texture  = smart_sample_with_ai("肌理", intent_input, db["Texture"], chaos_level)
    comp     = smart_sample_with_ai("构图", intent_input, db["Composition"], chaos_level)
    accent   = smart_sample_with_ai("点缀", intent_input, db["Accent"], chaos_level)

    for _ in range(num):
        new_batch.append(
            f"{random.choice(subjects)}，"
            f"{random.choice(stylesys)}，{random.choice(tech)}，{random.choice(color)}，"
            f"{random.choice(texture)}，{random.choice(comp)}，"
            f"{random.choice(actions)}，{random.choice(moods)}，"
            + (f"{random.choice(accent)}，" if accent and chaos_level > 60 else "")
            + f"纹在{random.choice(usages)}"
        )

    st.session_state.generated_cache = new_batch
    st.rerun()


# ================== 方案选择 ==================
if st.session_state.generated_cache:
    st.divider()
    st.subheader("🎲 方案选择")

    cols = st.columns(2)
    for i, p in enumerate(st.session_state.generated_cache):
        with cols[i % 2]:
            sel = p in st.session_state.selected_prompts
            if st.button(p, key=f"pick_{i}", type="primary" if sel else "secondary", use_container_width=True):
                if sel:
                    st.session_state.selected_prompts.remove(p)
                else:
                    st.session_state.selected_prompts.append(p)
                st.rerun()


# ================== 润色 ==================
if st.session_state.selected_prompts and not st.session_state.polished_text:
    st.divider()
    if st.button("✨ 开始润色", type="primary", use_container_width=True):
        with st.spinner("AI 正在润色..."):
            text = "\n".join([f"方案{i+1}：{p}" for i, p in enumerate(st.session_state.selected_prompts)])

            sys_prompt = """
            你是一位专业纹身设计说明撰写者。
            请将以下方案润色为可直接用于刺青设计沟通的中文描述。
            要求：
            - 每条不少于 60 字
            - 必须出现“纹身”
            - 禁止抒情与文学化
            - 格式必须为 **方案X：**
            """

            res = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": text}
                ],
                temperature=0.7
            )

            st.session_state.polished_text = res.choices[0].message.content
            st.rerun()


# ================== 最终输出 ==================
if st.session_state.polished_text:
    st.divider()
    st.subheader("🎨 润色完成")
    st.text_area("最终文案", st.session_state.polished_text, height=420)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 发送到自动化", use_container_width=True):
            st.session_state.auto_input_cache = st.session_state.polished_text
            st.switch_page("pages/02_automation.py")
    with c2:
        if st.button("🔄 重新开始", use_container_width=True):
            st.session_state.generated_cache = []
            st.session_state.selected_prompts = []
            st.session_state.polished_text = ""
            st.rerun()
