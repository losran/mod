import streamlit as st
from style_manager import apply_pro_style
import streamlit.components.v1 as components
import json
import urllib.parse
import re
# 引入侧边栏通用模块
from engine_manager import render_sidebar

# 1. 基础配置
st.set_page_config(layout="wide", page_title="Automation Central")

# 2. 🔥 关键修改：只调用全局样式，不再自己写 CSS
apply_pro_style()
render_sidebar()

# 3. 页面标题
st.title("🤖 自动化任务分发中控")

# 4. 平台选择
col_opt1, col_opt2 = st.columns([2, 1])
with col_opt1:
    target_platform = st.selectbox(
        "选择目标 AI 平台", 
        ["万能自适应 (推荐)", "Gemini (最新版适配)", "ChatGPT", "Doubao (豆包/镜像站)"],
        help="Gemini 采用的是 DIV 编辑器逻辑，万能模式如果不动，请选此项"
    )

# 5. 输入区域
default_text = st.session_state.get('auto_input_cache', "")
if not default_text:
    default_text = st.session_state.get('polished_text', "")

user_input = st.text_area("检查待处理的提示词内容：", value=default_text, height=300, key="main_input_area")

# --- 生产辅助选项 ---
st.divider()
col_check, col_btn = st.columns([1, 2])
with col_check:
    need_white_bg = st.checkbox("🏭 生产模式：每张图后自动生成白底图", value=False)

# 6. 生成按钮逻辑
with col_btn:
    # 这里的 type="primary" 现在会自动变成 style_manager 里定义的深灰色
    if st.button("🚀 生成全能适配脚本 (v15.0 防卡死版)", type="primary", use_container_width=True):
        # --- A. 智能拆分任务 ---
        task_list = []
        if user_input:
            if "###" in user_input:
                raw_tasks = [t.strip() for t in user_input.split("###") if len(t.strip()) > 2]
            else:
                blocks = re.split(r'\*\*方案[一二三四五六七八九十\d]+[:：].*?\*\*', user_input)
                raw_tasks = [b.strip().replace('* ', '').replace('\n', ' ') for b in blocks if len(b.strip()) > 5]
            
            if need_white_bg:
                for t in raw_tasks:
                    task_list.append(t)
                    task_list.append("生成上图白底图")
            else:
                task_list = raw_tasks

        # --- B. 生成脚本 ---
        if task_list:
            encoded_data = urllib.parse.quote(json.dumps(task_list))
            # JS 核心代码 (保持不变)
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
                    return document.querySelector('#prompt-textarea, [data-testid="rich-textarea"], textarea, .n-input__textarea-el, [placeholder*="输入"], [placeholder*="提问"], [placeholder*="Message"]');
                }}
                function getSendBtn() {{
                    let geminiBtn = document.querySelector('button[aria-label*="发送"], button[aria-label*="Send"]');
                    if (geminiBtn && !geminiBtn.disabled) return geminiBtn;
                    let btns = Array.from(document.querySelectorAll('button, [role="button"], i'));
                    return btns.find(b => {{
                        const t = (b.innerText || b.ariaLabel || b.className || b.outerHTML || "").toLowerCase();
                        const isSend = t.includes('发') || t.includes('send') || t.includes('m12 2 2 21 5 12 10 12') || b.getAttribute('data-testid') === 'send-button';
                        const isNew = t.includes('新') || t.includes('new');
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
                showStatus("🚀 脚本就绪...", "#444444"); // 改成灰色提示
                for (let i = 0; i < tasks.length; i++) {{
                    if (window.kill) {{ showStatus("🛑 已停止", "#ef4444"); break; }}
                    showStatus("✍️ 输入: " + (i+1) + "/" + tasks.length, "#666666");
                    let box = getInputBox();
                    if (!box) {{ showStatus("❌ 找不到输入框", "#ef4444"); break; }}
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
                            showStatus("🎨 作画中 (" + waitTime + "s)...", "#888888");
                            await new Promise(r => setTimeout(r, 1000));
                            waitTime++;
                            if (waitTime > 180) break;
                        }}
                        for (let s = 5; s > 0; s--) {{
                            if (window.kill) break;
                            showStatus("⏳ 冷却: " + s + "s", "#b45309");
                            await new Promise(r => setTimeout(r, 1000));
                        }}
                    }}
                }}
                if(!window.kill) showStatus("🎉 全部完成！", "#15803d");
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

            st.success(f"✅ 已生成 {len(task_list)} 条任务指令！")
            st.code(js_code, language="javascript")
            
        else:
            st.error("❌ 未识别到任务内容")

# 7. 清空按钮
if st.button("🗑️ 清空当前任务"):
    st.session_state.auto_input_cache = ""
    st.session_state.polished_text = ""
    st.rerun()
