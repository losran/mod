import streamlit as st
import random
import base64
import requests
from openai import OpenAI
from style_manager import apply_pro_style
from engine_manager import render_sidebar, WAREHOUSE, save_data

# ===========================
# Configuration
# ===========================
st.set_page_config(layout="wide", page_title="Creative Engine")
# --- ✂️ 复制这段代码 (终极修复补丁) ✂️ ---
st.markdown("""
<style>
    /* 1. 引入图标字体 (修复那个奇怪的 keyboard_... 文字) */
    @import url('https://fonts.googleapis.com/icon?family=Material+Icons');

    /* 2. 彻底隐藏右上角工具栏 (Share, Star, Menu) */
    [data-testid="stToolbar"] {
        visibility: hidden !important;
        display: none !important;
    }
    
    /* 3. 隐藏顶部的彩色装饰线 */
    [data-testid="stDecoration"] {
        display: none !important;
    }

    /* 4. 隐藏左上角的默认页面导航 */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* 5. 修复滑块看不见的问题 (强制高亮) */
    div[data-baseweb="slider"] div { background-color: #333 !important; }
    div[data-baseweb="slider"] div[class*="css"] { background-color: #e0e0e0 !important; }
    div[role="slider"] {
        background-color: #fff !important;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
        border: none !important;
    }
    div[data-testid="stThumbValue"] {
        background-color: #000 !important;
        color: #fff !important;
        border: 1px solid #fff !important;
    }
</style>
""", unsafe_allow_html=True)
# --- ✂️ 结束 ✂️ ---
# Apply Styles & Sidebar
apply_pro_style()
render_sidebar()

# ===========================
# Logic & Helpers
# ===========================
client = OpenAI(api_key=st.secrets["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO = "losran/tattoo-ai-tool" # Check your REPO name
GALLERY_FILE = "gallery/inspirations.txt"

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

def save_gallery_data(data_list):
    url = f"https://api.github.com/repos/{REPO}/contents/{GALLERY_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        old = requests.get(url, headers=headers).json()
        content = "\n".join(list(set(data_list)))
        payload = { "message": "update", "content": base64.b64encode(content.encode()).decode(), "sha": old["sha"] }
        requests.put(url, headers=headers, json=payload)
        return True
    except: return False

def chaos_pick(chaos, low, mid, high):
    if chaos < 30: return random.randint(*low)
    elif chaos < 70: return random.randint(*mid)
    else: return random.randint(*high)

def smart_sample_with_ai(category, user_intent, inventory, chaos_val):
    if not inventory: return []
    if not user_intent or not user_intent.strip():
        pool_size = int(20 + (300 - 20) * chaos_val / 100)
        shuffled = random.sample(inventory, min(len(inventory), pool_size))
        pick_n = chaos_pick(chaos_val, (1,2), (2,3), (3,5))
        return random.sample(shuffled, min(len(shuffled), pick_n))

    try:
        # Prompt remains Chinese to process Chinese database correctly
        prompt = f"从词库中选出符合'{user_intent}'的{category}词汇。词库:{random.sample(inventory, min(50, len(inventory)))}。只返回词，用逗号分隔。"
        res = client.chat.completions.create(
            model="deepseek-chat", messages=[{"role": "user", "content": prompt}], temperature=chaos_val/100.0
        ).choices[0].message.content
        words = [w.strip() for w in res.replace("，", ",").split(",") if w.strip()]
        valid = [w for w in words if w in inventory]
        return valid if valid else random.sample(inventory, 1)
    except:
        return random.sample(inventory, 1)

# ===========================
# UI Layout
# ===========================

if 'history_log' not in st.session_state: st.session_state.history_log = []
for key in ['selected_prompts', 'generated_cache', 'polished_text', 'manual_editor']:
    if key not in st.session_state: st.session_state[key] = "" if 'editor' in key or 'text' in key else []

is_working = len(st.session_state.polished_text) > 0

# Pure English Title
st.title("Creative Engine")
col_main, col_gallery = st.columns([5, 2.5])

# --- Right Column: Warehouse ---
with col_gallery:
    st.subheader("Warehouse")
    # Clean English Labels
    mode = st.radio("Mode", ["Materials", "Gallery"], horizontal=True)
    
    with st.container(height=300, border=True):
        if mode == "Materials":
            cat = st.selectbox("Category", list(WAREHOUSE.keys()))
            if "db_all" in st.session_state:
                words = st.session_state.db_all.get(cat, [])
                for w in words:
                    if st.checkbox(f" {w}", key=f"cat_{cat}_{w}", disabled=is_working):
                        if not is_working and w not in st.session_state.selected_prompts:
                            st.session_state.selected_prompts.append(w)
            else:
                st.caption("Loading data...")
        else:
            insps = get_gallery_data()
            for i in insps:
                if st.checkbox(i, key=f"insp_{abs(hash(i))}", disabled=is_working):
                    if not is_working and i not in st.session_state.selected_prompts:
                        st.session_state.selected_prompts.append(i)

    st.divider()
    st.subheader("History Archive")
    if st.session_state.history_log:
        with st.container(height=400, border=True):
            for h_idx, h_text in enumerate(st.session_state.history_log):
                checked = h_text in st.session_state.selected_prompts
                if st.checkbox(f"Option {h_idx+1}: {h_text}", key=f"hist_{h_idx}", value=checked, disabled=is_working):
                    if not is_working and h_text not in st.session_state.selected_prompts:
                        st.session_state.selected_prompts.append(h_text)
                        st.rerun()
        if st.button("Clear History", use_container_width=True):
            st.session_state.history_log = []; st.rerun()

# --- Left Column: Main Control ---
with col_main:
    c1, c2 = st.columns(2)
    with c1: num = st.slider("Quantity", 1, 6, 6)
    with c2: chaos = st.slider("Chaos Level", 0, 100, 100)
    
    intent = st.text_area("Intent Input", value=st.session_state.manual_editor, disabled=is_working)
    st.session_state.manual_editor = intent

    if st.button("Generate Ideas", type="primary", use_container_width=True, disabled=is_working):
        if "db_all" not in st.session_state:
            st.error("Please wait for data sync...")
        else:
            db = st.session_state.db_all
            with st.spinner("Brainstorming..."):
                new_batch = []
                subs = smart_sample_with_ai("Subject", "", db["Subject"], chaos)
                acts = smart_sample_with_ai("Action", "", db["Action"], chaos)
                moods = smart_sample_with_ai("Mood", "", db["Mood"], chaos)
                usages = smart_sample_with_ai("Usage", "", db["Usage"], chaos)
                
                s_sys = smart_sample_with_ai("StyleSystem", intent, db["StyleSystem"], chaos)
                s_tech = smart_sample_with_ai("Technique", intent, db["Technique"], chaos)
                s_col = smart_sample_with_ai("Color", intent, db["Color"], chaos)
                s_tex = smart_sample_with_ai("Texture", intent, db["Texture"], chaos)
                s_comp = smart_sample_with_ai("Composition", intent, db["Composition"], chaos)
                s_acc = smart_sample_with_ai("Accent", intent, db["Accent"], chaos)

                for _ in range(num):
                    def get_one(lst): return random.choice(lst) if lst else ""
                    parts = [intent.strip(), get_one(subs), get_one(s_sys), get_one(s_tech), get_one(s_col), get_one(s_tex), get_one(s_comp), get_one(acts), get_one(moods)]
                    if chaos > 60: parts.append(get_one(s_acc))
                    
                    final_str = "，".join([p for p in parts if p]) + f"，纹在{get_one(usages)}"
                    new_batch.append(final_str)
                
                st.session_state.generated_cache = new_batch
                st.rerun()

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
        if c_t1.button("Save to Gallery", use_container_width=True):
            if st.session_state.selected_prompts:
                curr = get_gallery_data()
                curr.extend(st.session_state.selected_prompts)
                save_gallery_data(curr)
                st.success("Saved")
        if c_t2.button("Clear Current", use_container_width=True):
            st.session_state.generated_cache = []
            st.session_state.selected_prompts = []
            st.rerun()

    if st.session_state.selected_prompts and not st.session_state.polished_text:
        st.divider()
        if st.button("Confirm & Polish", type="primary", use_container_width=True):
            abandoned = [p for p in st.session_state.generated_cache if p not in st.session_state.selected_prompts]
            st.session_state.history_log = abandoned + st.session_state.history_log
            st.session_state.generated_cache = []
            
            with st.spinner("Polishing..."):
                input_text = "\n".join([f"方案{i+1}: {p}" for i, p in enumerate(st.session_state.selected_prompts)])
                # Prompt stays Chinese to ensure output quality for tattoo descriptions
                sys_p = "你是一位资深刺青策展人。请将方案润色为极具艺术感的纹身描述。每段必须出现'纹身'二字。格式：**方案[数字]：**"
                
                try:
                    res = client.chat.completions.create(
                        model="deepseek-chat", messages=[
                            {"role": "system", "content": sys_p},
                            {"role": "user", "content": input_text}
                        ]
                    ).choices[0].message.content
                    st.session_state.polished_text = res
                    st.session_state.selected_prompts = [] 
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

    if st.session_state.polished_text:
        st.divider()
        st.subheader("Polished Result")
        st.text_area("Preview", st.session_state.polished_text, height=300)
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("Send to Automation", type="primary", use_container_width=True):
            st.session_state.auto_input_cache = st.session_state.polished_text
            st.switch_page("pages/02_automation.py")
        if c_b2.button("Reset", use_container_width=True):
            st.session_state.polished_text = ""
            st.rerun()
