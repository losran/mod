import streamlit as st
import json
import os
import random
import numpy as np
import requests
import base64
from openai import OpenAI
from style_manager import apply_pro_style

# 📍 视觉样式同步
apply_pro_style()

# --- 1. 核心配置 ---
client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = "losran/tattoo-ai-tool"

WAREHOUSE = {
    "Subject": "data/subjects.txt",
    "Action": "data/actions.txt",
    "Mood": "data/moods.txt",
    "Usage": "data/usage.txt",

    # 👇 新增的风格分层
    "StyleSystem": "data/styles_system.txt",
    "Technique": "data/styles_technique.txt",
    "Color": "data/styles_color.txt",
    "Texture": "data/styles_texture.txt",
    "Composition": "data/styles_composition.txt",
    "Accent": "data/styles_accent.txt"
}

GALLERY_FILE = "gallery/inspirations.txt"

def chaos_pick(chaos, low, mid, high):
    if chaos < 30:
        return random.randint(*low)
    elif chaos < 70:
        return random.randint(*mid)
    else:
        return random.randint(*high)


def smart_sample_with_ai(category, user_intent, inventory, chaos_val):
    # 1. 映射计算与物理洗牌
    temp_score = float(chaos_val) / 100.0 

    if not inventory:
        return []
    pool_size = int(20 + (300 - 20) * chaos_val / 100)

    shuffled_pool = random.sample(
        inventory,
        min(len(inventory), pool_size)
    )
           
    # 2. 情况 A：如果没有意图，直接返回随机组合
    if not user_intent or not user_intent.strip():
        pick_n = chaos_pick(
            chaos_val,
            (10, 30),   # chaos < 30
            (30, 150),   # chaos < 70
            (150, 300)    # chaos >= 70
        )

        return random.sample(
            shuffled_pool,
            min(len(shuffled_pool), pick_n)
        )

    # ---------- 3. 有意图：AI 只负责“选”，不理解 ----------
    temp_score = chaos_val / 100.0

    prompt = f"""
    分类：{category}
    词库：{shuffled_pool}

    规则：
    1. 只能从词库中选词，不得造词
    2. 返回 1-3 个词
    3. 只输出词，用逗号分隔
    """
    
    try:
        res = client.chat.completions.create(
            model="deepseek-chat", 
            messages=[{"role": "user", "content": prompt}], 
            temperature=temp_score,
            frequency_penalty=1.5  # 增加惩罚，进一步防止雷同
        )
        
        # ✅ 关键修改：不再返回字符串，而是【词列表】
        raw = res.choices[0].message.content.strip()
        words = [w.strip() for w in raw.replace("，", ",").split(",") if w.strip()]
         # 只保留在池子里的词
        valid = [w for w in words if w in shuffled_pool]
        #return words
        return valid if valid else random.sample(shuffled_pool, 1)

        
    except Exception:
        # 兜底也返回【词列表】
        return [user_intent, random.choice(shuffled_pool)]
        

def get_github_data(path):
    
    import time

    url = f"https://api.github.com/repos/{REPO}/contents/{path}?t={int(time.time())}"

    #url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            # 解码 GitHub 的 Base64 内容
            content = base64.b64decode(resp.json()['content']).decode()
            return [line.strip() for line in content.splitlines() if line.strip()]
    except Exception as e:
        st.error(f"GitHub 读取失败: {e}")
    return []

def save_to_github(path, data_list):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        get_resp = requests.get(url, headers=headers, timeout=10).json()
        content_str = "\n".join(list(set(data_list)))
        b64_content = base64.b64encode(content_str.encode()).decode()
        requests.put(url, headers=headers, json={"message": "update", "content": b64_content, "sha": get_resp.get('sha')}, timeout=15)
        return True
    except: return False

# --- 3. UI 布局与 Session 初始化 ---
st.set_page_config(layout="wide", page_title="Creative Engine")

for key in ['selected_prompts', 'generated_cache', 'polished_text', 'manual_editor']:
    if key not in st.session_state:
        st.session_state[key] = "" if 'editor' in key or 'text' in key else []

# 🔒 定义全局锁定状态
is_working = len(st.session_state.polished_text) > 0

st.title("🎨 创意引擎")
col_main, col_gallery = st.columns([5, 2.5])

# --- 🟢 右侧：仓库管理 (上) + 历史记录 (下) ---
with col_gallery:
    st.subheader("📦 仓库管理")
    mode = st.radio("模式", ["素材仓库", "灵感成品"], horizontal=True)
    
    # 1. 仓库管理容器
    with st.container(height=300, border=True):
        if mode == "素材仓库":
            cat = st.selectbox("分类", list(WAREHOUSE.keys()))
            #words = get_github_data(WAREHOUSE[cat])
            raw_words = get_github_data(WAREHOUSE[cat])
            warehouse_set = set(raw_words)
            words = [w for w in raw_words if w in warehouse_set]

            if words:
                for w in words:
                    if st.checkbox(f" {w}", key=f"cat_{cat}_{w}", disabled=is_working):
                        if not is_working and w not in st.session_state.selected_prompts:
                            st.session_state.selected_prompts.append(w)
        else:
            insps = get_github_data(GALLERY_FILE)
            if insps:
                for i in insps:
                    if st.checkbox(i, key=f"insp_lib_{abs(hash(i))}", disabled=is_working):
                        if not is_working and i not in st.session_state.selected_prompts:
                            st.session_state.selected_prompts.append(i)


# --- 🔵 左侧：核心生成区 ---
with col_main:
    
    
    col_cfg1, col_cfg2 = st.columns(2)
    with col_cfg1: num = st.slider("生成方案数量", 1, 6, 6)
    with col_cfg2: chaos_level = st.slider("混乱程度", 0, 100,100)
    
    intent_input = st.text_area("✍ 组合意图输入框", value=st.session_state.manual_editor, disabled=is_working)
    st.session_state.manual_editor = intent_input

    # 💡 激发逻辑：只更新中间桌面，不进历史
    if st.button("🔥 激发创意组合", type="primary", use_container_width=True, disabled=is_working):
        db_all = {k: get_github_data(v) for k, v in WAREHOUSE.items()}
        with st.spinner("AI 精准挑词中..."):
            new_batch = []
            subjects = smart_sample_with_ai("Subject", "", db_all["Subject"], chaos_level)
            actions = smart_sample_with_ai("Action", "", db_all["Action"], chaos_level)
            moods   = smart_sample_with_ai("Mood", "", db_all["Mood"], chaos_level)
            usages  = smart_sample_with_ai("Usage", "", db_all["Usage"], chaos_level)


            
            style_system  = smart_sample_with_ai("StyleSystem", intent_input, db_all["StyleSystem"], chaos_level)
            style_tech    = smart_sample_with_ai("Technique", intent_input, db_all["Technique"], chaos_level)
            style_color   = smart_sample_with_ai("Color", intent_input, db_all["Color"], chaos_level)
            style_texture = smart_sample_with_ai("Texture", intent_input, db_all["Texture"], chaos_level)
            style_comp    = smart_sample_with_ai("Composition", intent_input, db_all["Composition"], chaos_level)
            style_accent  = smart_sample_with_ai("Accent", intent_input, db_all["Accent"], chaos_level)

            intent = intent_input.strip()

            for _ in range(num):
                s = random.sample(subjects, min(1, len(subjects)))
                a = random.sample(actions,  min(1, len(actions)))
                m = random.sample(moods, min(1, len(moods)))
                u = random.sample(usages, min(1, len(usages)))

                new_batch.append(
                    f"{intent}，"
                    f"{random.choice(subjects)}，"
                    f"{random.choice(style_system)}，"
                    f"{random.choice(style_tech)}，"
                    f"{random.choice(style_color)}，"
                    f"{random.choice(style_texture)}，"
                    f"{random.choice(style_comp)}，"
                    f"{random.choice(actions)}，"
                    f"{random.choice(moods)}，"
                    + (f"{random.choice(style_accent)}，" if chaos_level > 60 and style_accent else "")
                    + f"纹在{random.choice(usages)}"
                )

            st.session_state.generated_cache = new_batch
        st.rerun()
    # 🎲 方案筛选 (中间桌面)
    if st.session_state.generated_cache:
        st.divider()
        st.subheader("🎲 方案筛选")
        cols = st.columns(2)
        for idx, p in enumerate(st.session_state.generated_cache):
            with cols[idx % 2]:
                is_sel = p in st.session_state.selected_prompts
                if st.button(f"{idx+1}. {p}", key=f"gen_{idx}", 
                             type="primary" if is_sel else "secondary", 
                             disabled=is_working, use_container_width=True):
                    if not is_working:
                        if is_sel: st.session_state.selected_prompts.remove(p)
                        else: st.session_state.selected_prompts.append(p)
                        st.rerun()
        
        c_tool1, c_tool2 = st.columns(2)
        with c_tool1:
            if st.button("💾 存入成品库", use_container_width=True, disabled=is_working):
                if st.session_state.selected_prompts:
                    current = get_github_data(GALLERY_FILE)
                    current.extend(st.session_state.selected_prompts)
                    save_to_github(GALLERY_FILE, current); st.success("已存档")
        with c_tool2:
            if st.button("🗑️ 清除当前", use_container_width=True, disabled=is_working):
                st.session_state.generated_cache = []; st.session_state.selected_prompts = []
                st.rerun()

# --- 🔵 精准加固后的润色逻辑 ---
if st.session_state.selected_prompts and not st.session_state.polished_text:
    st.divider()

    if st.button("✨ 确认方案并开始润色", type="primary", use_container_width=True):

        # ✅ 0. 确保 history_log 存在（这是你刚刚那个报错的根源）
        if 'history_log' not in st.session_state:
            st.session_state.history_log = []

        # ✅ 1. 先归档：用还没被清空的 generated_cache
        if st.session_state.generated_cache:
            abandoned = [
                p for p in st.session_state.generated_cache
                if p not in st.session_state.selected_prompts
            ]
            if abandoned:
                st.session_state.history_log = abandoned + st.session_state.history_log

        # ✅ 2. 再清空展示缓存（顺序必须在这里）
        st.session_state.generated_cache = []

        # ✅ 3. 再进入后续润色流程（你原本已有的那套）
        # —— 后面的 AI 润色代码保持不动

        
        except Exception as e:
            st.error(f"归档过程出错: {e}")         

            # 2. 执行润色
            with st.spinner("AI 注入灵魂中..."):
                try:
                    # 构造纯净的输入文本
                    input_text = "\n".join([f"方案{idx+1}: {p}" for idx, p in enumerate(st.session_state.selected_prompts)])
                    
                    # 审美光谱映射
                    if chaos_level <= 35: v, f, n = "可爱治愈", "软萌圆润", "陪伴"
                    elif chaos_level <= 75: v, f, n = "日式传统", "黑线重彩", "沉淀"
                    else: v, f, n = "欧美极简", "力量解构", "破局"
                    
                    sys_p = f"你是一位资深刺青策展人。风格基调：{v}。请将方案润色为极具艺术感的纹身描述,每一段文本必须出现纹身这两个字。请务必为每个润色后的方案加上标题，格式严格遵守：**方案[数字]：**，禁止省略星号和冒号。"
                    
                    response = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[
                            {"role": "system", "content": sys_p},
                            {"role": "user", "content": input_text}
                        ],
                        temperature=0.7,
                        timeout=30 # 增加超时保护
                    )
                    
                    st.session_state.polished_text = response.choices[0].message.content

                    # 🔥 清空生成态
                    st.session_state.generated_cache = []
                    st.session_state.selected_prompts = []
                    
                    st.rerun()

                except Exception as e:
                    st.error(f"润色失败原因: {e}")
                    # 如果失败了，建议不要清空 generated_cache，让用户可以重试

    if st.session_state.polished_text:
        st.divider(); st.subheader("🎨 艺术润色成品")
        st.text_area("文案预览：", st.session_state.polished_text, height=400)
        c_b1, c_b2 = st.columns(2)
        with c_b1:
            if st.button("🚀 发送到自动化", type="primary", use_container_width=True):
                st.session_state.auto_input_cache = st.session_state.polished_text; st.switch_page("pages/02_automation.py")
        with c_b2:
            if st.button("🔄 重新调配 (解锁所有)", use_container_width=True):
                st.session_state.polished_text = ""; st.rerun()
