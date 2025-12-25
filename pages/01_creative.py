import streamlit as st
import random
import base64
import requests
from openai import OpenAI
from style_manager import apply_pro_style
# 🔥 核心改动：引入通用引擎
from engine_manager import render_sidebar, WAREHOUSE, save_data

# --- 1. 基础配置 ---
st.set_page_config(layout="wide", page_title="Creative Engine")
apply_pro_style()
render_sidebar() # 👈 这一行就把侧边栏加进来了！

# --- 2. 配置 ---
client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = "losran/tattoo-ai-tool"
GALLERY_FILE = "gallery/inspirations.txt"

# 专门用于读取 Gallery 的独立函数 (因为 Gallery 不在 WAREHOUSE 里)
def get_gallery_data():
    url = f"https://api.github.com/repos/{REPO}/contents/{GALLERY_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            content = base64.b64decode(r.json()['content']).decode()
            return [line.strip() for line in content.splitlines() if line.strip()]
    except:
        pass
    return []

# 专门保存 Gallery 的函数
def save_gallery_data(data_list):
    url = f"https://api.github.com/repos/{REPO}/contents/{GALLERY_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        old = requests.get(url, headers=headers).json()
        content = "\n".join(list(set(data_list)))
        payload = {
            "message": "update", 
            "content": base64.b64encode(content.encode()).decode(), 
            "sha": old["sha"]
        }
        requests.put(url, headers=headers, json=payload)
        return True
    except: return False

# 混沌选择算法
def chaos_pick(chaos, low, mid, high):
    if chaos < 30: return random.randint(*low)
    elif chaos < 70: return random.randint(*mid)
    else: return random.randint(*high)

# 智能采样
def smart_sample_with_ai(category, user_intent, inventory, chaos_val):
    if not inventory: return []
    
    # 无意图或高混乱：直接随机
    if not user_intent or not user_intent.strip():
        pool_size = int(20 + (300 - 20) * chaos_val / 100)
        shuffled = random.sample(inventory, min(len(inventory), pool_size))
        pick_n = chaos_pick(chaos_val, (1,2), (2,3), (3,5)) # 稍微调整了数量逻辑
        return random.sample(shuffled, min(len(shuffled), pick_n))

    # 有意图：AI 筛选
    try:
        prompt = f"从词库中选出最符合'{user_intent}'的{category}词汇。词库:{random.sample(inventory, min(50, len(inventory)))}。只返回词，用逗号分隔。"
        res = client.chat.completions.create(
            model="deepseek-chat", 
            messages=[{"role": "user", "content": prompt}], 
            temperature=chaos_val/100.0
        ).choices[0].message.content
        
        words = [w.strip() for w in res.replace("，", ",").split(",") if w.strip()]
        valid = [w for w in words if w in inventory]
        return valid if valid else random.sample(inventory, 1)
    except:
        return random.sample(inventory, 1)

# --- 3. Session 初始化 ---
if 'history_log' not in st.session_state: st.session_state.history_log = []
for key in ['selected_prompts', 'generated_cache', 'polished_text', 'manual_editor']:
    if key not in st.session_state:
        st.session_state[key] = "" if 'editor' in key or 'text' in key else []

is_working = len(st.session_state.polished_text) > 0

st.title("🎨 创意引擎")
col_main, col_gallery = st.columns([5, 2.5])

# --- 🟢 右侧：仓库管理 ---
with col_gallery:
    st.subheader("📦 仓库管理")
    mode = st.radio("模式", ["素材仓库", "灵感成品"], horizontal=True)
    
    with st.container(height=300, border=True):
        if mode == "素材仓库":
            # 🔥 优化：直接从 Session 读数据，秒开！
            cat = st.selectbox("分类", list(WAREHOUSE.keys()))
            if "db_all" in st.session_state:
                words = st.session_state.db_all.get(cat, [])
                for w in words:
                    if st.checkbox(f" {w}", key=f"cat_{cat}_{w}", disabled=is_working):
                        if not is_working and w not in st.session_state.selected_prompts:
                            st.session_state.selected_prompts.append(w)
            else:
                st.warning("数据正在同步中，请稍等...")
        else:
            # Gallery 还是实时读取比较安全
            insps = get_gallery_data()
            for i in insps:
                if st.checkbox(i, key=f"insp_{abs(hash(i))}", disabled=is_working):
                    if not is_working and i not in st.session_state.selected_prompts:
                        st.session_state.selected_prompts.append(i)

    # 历史档案
    st.divider()
    st.subheader("📜 历史档案")
    if st.session_state.history_log:
        with st.container(height=400, border=True):
            for h_idx, h_text in enumerate(st.session_state.history_log):
                checked = h_text in st.session_state.selected_prompts
                if st.checkbox(f"备选 {h_idx+1}: {h_text}", key=f"hist_{h_idx}", value=checked, disabled=is_working):
                    if not is_working and h_text not in st.session_state.selected_prompts:
                        st.session_state.selected_prompts.append(h_text)
                        st.rerun()
        if st.button("🗑️ 清空历史", use_container_width=True):
            st.session_state.history_log = []; st.rerun()

# --- 🔵 左侧：生成区 ---
with col_main:
    c1, c2 = st.columns(2)
    with c1: num = st.slider("生成方案数量", 1, 6, 6)
    with c2: chaos = st.slider("混乱程度", 0, 100, 100)
    
    intent = st.text_area("✍ 意图输入", value=st.session_state.manual_editor, disabled=is_working)
    st.session_state.manual_editor = intent

    if st.button("🔥 激发创意", type="primary", use_container_width=True, disabled=is_working):
        # 🔥 优化：直接使用缓存数据
        if "db_all" not in st.session_state:
            st.error("请先等待左侧数据加载完成")
        else:
            db = st.session_state.db_all
            with st.spinner("AI 正在头脑风暴..."):
                new_batch = []
                # 预取词汇
                subs = smart_sample_with_ai("Subject", "", db["Subject"], chaos)
                acts = smart_sample_with_ai("Action", "", db["Action"], chaos)
                moods = smart_sample_with_ai("Mood", "", db["Mood"], chaos)
                usages = smart_sample_with_ai("Usage", "", db["Usage"], chaos)
                
                # 风格相关
                s_sys = smart_sample_with_ai("StyleSystem", intent, db["StyleSystem"], chaos)
                s_tech = smart_sample_with_ai("Technique", intent, db["Technique"], chaos)
                s_col = smart_sample_with_ai("Color", intent, db["Color"], chaos)
                s_tex = smart_sample_with_ai("Texture", intent, db["Texture"], chaos)
                s_comp = smart_sample_with_ai("Composition", intent, db["Composition"], chaos)
                s_acc = smart_sample_with_ai("Accent", intent, db["Accent"], chaos)

                for _ in range(num):
                    # 安全获取随机词函数
                    def get_one(lst): return random.choice(lst) if lst else ""
                    
                    parts = [
                        intent.strip(),
                        get_one(subs), get_one(s_sys), get_one(s_tech),
                        get_one(s_col), get_one(s_tex), get_one(s_comp),
                        get_one(acts), get_one(moods)
                    ]
                    if chaos > 60: parts.append(get_one(s_acc))
                    
                    final_str = "，".join([p for p in parts if p]) + f"，纹在{get_one(usages)}"
                    new_batch.append(final_str)
                
                st.session_state.generated_cache = new_batch
                st.rerun()

    # 方案筛选区
    if st.session_state.generated_cache:
        st.divider()
        cols = st.columns(2)
        for i, p in enumerate(st.session_state.generated_cache):
            with cols[i % 2]:
                sel = p in st.session_state.selected_prompts
                if st.button(f"{i+1}. {p}", key=f"gen_{i}", type="primary" if sel else "secondary", use_container_width=True):
                    if sel: st.session_state.selected_prompts.remove(p)
                    else: st.session_state.selected_prompts.append(p)
                    st.rerun()
        
        c_t1, c_t2 = st.columns(2)
        if c_t1.button("💾 存入成品库", use_container_width=True):
            if st.session_state.selected_prompts:
                curr = get_gallery_data()
                curr.extend(st.session_state.selected_prompts)
                save_gallery_data(curr)
                st.success("已存档")
        if c_t2.button("🗑️ 清除当前", use_container_width=True):
            st.session_state.generated_cache = []
            st.session_state.selected_prompts = []
            st.rerun()

    # 润色逻辑
    if st.session_state.selected_prompts and not st.session_state.polished_text:
        st.divider()
        if st.button("✨ 确认方案并润色", type="primary", use_container_width=True):
            # 归档未选中的
            abandoned = [p for p in st.session_state.generated_cache if p not in st.session_state.selected_prompts]
            st.session_state.history_log = abandoned + st.session_state.history_log
            st.session_state.generated_cache = []
            
            with st.spinner("DeepSeek 正在注入灵魂..."):
                input_text = "\n".join([f"方案{i+1}: {p}" for i, p in enumerate(st.session_state.selected_prompts)])
                sys_p = "你是一位资深刺青策展人。请将方案润色为极具艺术感的纹身描述。每段必须出现'纹身'二字。格式：**方案[数字]：**"
                
                try:
                    res = client.chat.completions.create(
                        model="deepseek-chat", messages=[
                            {"role": "system", "content": sys_p},
                            {"role": "user", "content": input_text}
                        ]
                    ).choices[0].message.content
                    st.session_state.polished_text = res
                    st.session_state.selected_prompts = [] # 清空已选
                    st.rerun()
                except Exception as e:
                    st.error(f"润色失败: {e}")

    # 结果展示与跳转
    if st.session_state.polished_text:
        st.divider()
        st.subheader("🎨 润色成品")
        st.text_area("预览", st.session_state.polished_text, height=300)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("🚀 发送到自动化", type="primary", use_container_width=True):
            st.session_state.auto_input_cache = st.session_state.polished_text
            st.switch_page("pages/02_automation.py")
        if c_b2.button("🔄 重置", use_container_width=True):
            st.session_state.polished_text = ""
            st.rerun()
