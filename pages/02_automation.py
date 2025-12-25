import streamlit as st
from style_manager import apply_pro_style
import streamlit.components.v1 as components
import json
import urllib.parse
import re
from engine_manager import render_sidebar

# ===========================
# Configuration
# ===========================
st.set_page_config(layout="wide", page_title="Automation Central")

# Apply Styles & Sidebar
apply_pro_style()
render_sidebar()

# ===========================
# UI Layout
# ===========================
st.title("Automation Central")

# Platform Selection
col_opt1, col_opt2 = st.columns([2, 1])
with col_opt1:
    target_platform = st.selectbox(
        "Target AI Platform", 
        ["Universal (Recommended)", "Gemini", "ChatGPT", "Doubao"],
        help="Universal mode adapts to most chat interfaces."
    )

# Input Area
default_text = st.session_state.get('auto_input_cache', "")
if not default_text:
    default_text = st.session_state.get('polished_text', "")

user_input = st.text_area("Prompt Queue", value=default_text, height=300, key="main_input_area")

# --- Options ---
st.divider()

# 使用固定比例并开启强制垂直居中对齐
col_check, col_btn = st.columns([1.2, 2], vertical_alignment="center")

with col_check:
    # 移除多余的间距，让它贴近中轴
    need_white_bg = st.checkbox("Production Mode: Auto White Background", value=False)
    
# --- Generation Logic ---
with col_btn:
    # Primary button (Deep Grey Style)
    if st.button("Generate Script (v15.0)", type="primary", use_container_width=True):
        # --- A. Task Parsing ---
        task_list = []
        if user_input:
            # Handle manual separator '###'
            if "###" in user_input:
                raw_tasks = [t.strip() for t in user_input.split("###") if len(t.strip()) > 2]
            else:
                # Handle auto-generated format "**Scheme 1:**"
                # Regex covers both Chinese "方案" and English "Scheme/Option" just in case
                blocks = re.split(r'\*\*.*?(?:方案|Scheme|Option).*?[\d]+[:：].*?\*\*', user_input)
                raw_tasks = [b.strip().replace('* ', '').replace('\n', ' ') for b in blocks if len(b.strip()) > 5]
            
            if need_white_bg:
                for t in raw_tasks:
                    task_list.append(t)
                    task_list.append("Generate a white background version of the image above")
            else:
                task_list = raw_tasks

        # --- B. Script Construction ---
        if task_list:
            encoded_data = urllib.parse.quote(json.dumps(task_list))
            
            # JS Core Logic (Translated to English UI)
            js_code = f"""(async function() {{
                window.kill = false;
                const tasks = JSON.parse(decodeURIComponent("{encoded_data}"));
                
                function showStatus(text, color = "#1e293b", textColor = "#fff") {{
                    let el = document.getElementById('magic-status-bar');
                    if (!el) {{
                        el = document.createElement('div');
                        el.id = 'magic-status-bar';
                        el.style.cssText = "position:fixed; top:20px; left:50%; transform:translateX(-50%); z-index:999999; padding:10px 20px; border-radius:30px; font-family:sans-serif; font-size:14px; font-weight:bold; box-shadow:0 10px 25px rgba(0,0,0,0.2); transition: all 0.3s;";
                        document.body.appendChild(el);
                    }}
                    el.textContent = text;
                    el.style.backgroundColor = color;
                    el.style.color = textColor;
                }}

                function getInputBox() {{
                    let geminiBox = document.querySelector('div[role="textbox"][contenteditable="true"]');
                    if (geminiBox) return geminiBox;
                    return document.querySelector('#prompt-textarea, [data-testid="rich-textarea"], textarea, .n-input__textarea-el, [placeholder*="Enter"], [placeholder*="Message"], [placeholder*="输入"]');
                }}

                function getSendBtn() {{
                    let geminiBtn = document.querySelector('button[aria-label*="Send"], button[aria-label*="发送"]');
                    if (geminiBtn && !geminiBtn.disabled) return geminiBtn;
                    let btns = Array.from(document.querySelectorAll('button, [role="button"], i'));
                    return btns.find(b => {{
                        const t = (b.innerText || b.ariaLabel || b.className || b.outerHTML || "").toLowerCase();
                        const isSend = t.includes('send') || t.includes('发') || t.includes('m12 2 2 21 5 12 10 12') || b.getAttribute('data-testid') === 'send-button';
                        const isNew = t.includes('new') || t.includes('新');
                        const isStop = t.includes('stop') || t.includes('停止');
                        return isSend && !isNew && !isStop && b.offsetParent !== null && !b.disabled;
                    }});
                }}

                function isGenerating() {{
                    let btns = Array.from(document.querySelectorAll('button, [role="button"]'));
                    return btns.some(b => {{
                        const t = (b.innerText || b.ariaLabel || "").toLowerCase();
                        return t.includes('stop') || t.includes('停止') || t.includes('generating');
                    }});
                }}

                showStatus("🚀 Script Ready...", "#444444"); 
                
                for (let i = 0; i < tasks.length; i++) {{
                    if (window.kill) {{ showStatus("🛑 Stopped", "#ef4444"); break; }}
                    
                    showStatus("✍️ Inputting: " + (i+1) + "/" + tasks.length, "#666666");
                    let box = getInputBox();
                    if (!box) {{ showStatus("❌ Input Box Not Found", "#ef4444"); break; }}
                    
                    box.focus();
                    if (box.tagName === 'DIV') {{ box.innerText = tasks[i]; }} else {{ document.execCommand('insertText', false, tasks[i]); }}
                    
                    await new Promise(r => setTimeout(r, 1000));
                    box.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    box.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    
                    await new Promise(r => setTimeout(r, 500));
                    let sendBtn = getSendBtn();
                    if (sendBtn) sendBtn.click();
                    
                    if (i < tasks.length - 1) {{
                        let waitTime = 0;
                        await new Promise(r => setTimeout(r, 3000));
                        while(true) {{
                            if (window.kill) break;
                            if (!isGenerating()) break;
                            showStatus("🎨 Generating (" + waitTime + "s)...", "#888888");
                            await new Promise(r => setTimeout(r, 1000));
                            waitTime++;
                            if (waitTime > 180) break;
                        }}
                        for (let s = 5; s > 0; s--) {{
                            if (window.kill) break;
                            showStatus("⏳ Cooldown: " + s + "s", "#b45309");
                            await new Promise(r => setTimeout(r, 1000));
                        }}
                    }}
                }}
                if(!window.kill) showStatus("🎉 All Tasks Completed!", "#15803d");
            }})();"""

            js_val = json.dumps(js_code)
            components.html(f"""
            <script>
                const text = {js_val};
                if (navigator.clipboard) {{
                    navigator.clipboard.writeText(text).catch(err => console.log('Auto-copy failed'));
                }}
            </script>
            """, height=0)

            st.success(f"Generated {len(task_list)} task instructions. Script copied to clipboard.")
            st.code(js_code, language="javascript")
            
        else:
            st.error("No valid tasks found in queue.")

# Clear Button
if st.button("Clear Queue"):
    st.session_state.auto_input_cache = ""
    st.session_state.polished_text = ""
    st.rerun()
