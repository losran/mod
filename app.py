import streamlit as st
import json
from openai import OpenAI
from engine_manager import render_sidebar, WAREHOUSE, save_data, init_data
from style_manager import apply_pro_style

# ===========================
# Configuration
# ===========================
st.set_page_config(layout="wide", page_title="Creative Engine")

# Apply Styles & Sidebar
apply_pro_style()
render_sidebar()

# ===========================
# Logic & Helpers
# ===========================
client = OpenAI(
    api_key=st.secrets["DEEPSEEK_KEY"],
    base_url="https://api.deepseek.com"
)

# Session State Init
if "ai_results" not in st.session_state:
    st.session_state.ai_results = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ===========================
# UI Layout
# ===========================
center, right = st.columns([4, 2])

# --- Left Column: Smart Ingest ---
with center:
    st.header("Smart Ingest")
    st.session_state.input_text = st.text_area(
        "Inspiration Input",
        st.session_state.input_text,
        height=220,
        placeholder="Describe your tattoo idea or paste visual elements here..."
    )

    if st.button("Start Analysis", use_container_width=True):
        if not st.session_state.input_text:
            st.warning("Input is empty.")
        else:
            with st.spinner("Analyzing..."):
                # Prompt remains robust for Chinese input handling
                prompt = f"""
                任务：将纹身描述文本拆解为结构化关键词。
                
                【重要规则】
                1. 请务必区分：
                   - Subject (主体): 具体的物体、生物 (如: 猫, 骷髅, 玫瑰)
                   - StyleSystem (风格): 艺术流派 (如: 赛博朋克, Old School, 水墨)
                   - Mood (情绪): 氛围感受 (如: 压抑, 欢快, 神圣)
                   - Action (动作): 动态 (如: 奔跑, 燃烧, 缠绕)
                2. 不要把风格和情绪全塞进 Subject！
                
                【输出格式】
                请直接返回纯 JSON 数据，不要包含 ```json 代码块标记。格式如下：
                {{
                    "Subject": ["词1", "词2"],
                    "Action": ["词1"],
                    "Mood": ["词1"],
                    "StyleSystem": ["词1"],
                    "Usage": ["词1"]
                }}
                
                可用Key: Subject, Action, Mood, Usage, StyleSystem, Technique, Color, Texture, Composition, Accent

                输入文本：{st.session_state.input_text}
                """
                
                try:
                    res_obj = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.1
                    )
                    res = res_obj.choices[0].message.content
                    
                    parsed = []
                    
                    # JSON Parsing Logic
                    try:
                        clean_json = res.replace("```json", "").replace("```", "").strip()
                        data = json.loads(clean_json)
                        
                        for cat, words in data.items():
                            target_key = None
                            for k in WAREHOUSE:
                                if k.lower() == cat.lower() or k.lower() in cat.lower():
                                    target_key = k
                                    break
                            
                            if target_key and isinstance(words, list):
                                for w in words:
                                    if w and isinstance(w, str):
                                        parsed.append({"cat": target_key, "val": w.strip()})
                                        
                    except json.JSONDecodeError:
                        # Fallback Logic
                        st.warning("JSON parsing failed, switching to fallback mode...")
                        clean_res = res.replace("：", ":").replace("\n", "|").replace("，", ",")
                        for block in clean_res.split("|"):
                            if ":" in block:
                                parts = block.split(":", 1)
                                if len(parts) == 2:
                                    cat, words = parts
                                    cat = cat.strip()
                                    target_key = None
                                    for k in WAREHOUSE:
                                        if k.lower() in cat.lower(): 
                                            target_key = k
                                            break
                                    if target_key:
                                        for w in words.split(","):
                                            w = w.strip()
                                            if w: parsed.append({"cat": target_key, "val": w})

                    st.session_state.ai_results = parsed

                    if not parsed:
                        st.error("No keywords extracted. The AI might have refused the request.")
                        with st.expander("Raw AI Response"):
                            st.text(res)

                except Exception as e:
                    st.error(f"Request Error: {e}")

    # Display Results
    if st.session_state.ai_results:
        st.success(f"Extracted {len(st.session_state.ai_results)} keywords")
        st.subheader("Analysis Results")
        
        selected = []
        cols = st.columns(3)
        for i, item in enumerate(st.session_state.ai_results):
            with cols[i % 3]:
                if st.checkbox(f'{item["cat"]} · {item["val"]}', key=f'chk_{i}', value=True):
                    selected.append(item)
        
        st.divider()

        if st.button("Confirm Import", type="primary", use_container_width=True):
            if "db_all" not in st.session_state:
                init_data()
            
            changed_cats = set()
            for item in selected:
                cat, val = item["cat"], item["val"]
                current = st.session_state.db_all.get(cat, [])
                if val not in current:
                    current.append(val)
                    st.session_state.db_all[cat] = current
                    changed_cats.add(cat)
            
            if changed_cats:
                with st.spinner("Syncing to Warehouse..."):
                    for c in changed_cats: 
                        save_data(WAREHOUSE[c], st.session_state.db_all[c])
                st.success("Import Successful")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.info("No new keywords to import.")

# --- Right Column: Warehouse Manager ---
with right:
    st.header("Warehouse")
    cat = st.selectbox("Category", list(WAREHOUSE.keys()))
    
    if "db_all" not in st.session_state:
        init_data()
        
    words = st.session_state.db_all.get(cat, [])

    with st.container(height=500):
        if not words:
            st.caption("No Data")
        for w in words:
            c1, c2 = st.columns([4, 1]) 
            with c1:
                if st.button(w, key=f"add_{w}", use_container_width=True):
                    st.session_state.input_text += f" {w}"
            with c2:
                if st.button("✕", key=f"del_{cat}_{w}"):
                    new_list = [i for i in words if i != w]
                    st.session_state.db_all[cat] = new_list
                    save_data(WAREHOUSE[cat], new_list)
                    st.rerun()
