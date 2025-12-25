import streamlit as st

def apply_pro_style():
    # 保持字体加载
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* 1. 全局基础与禁止翻译干扰 */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}
        /* 标记该区域不接受浏览器自动翻译，防止乱码浮现 */
        [data-testid*="Sidebar"], .notranslate {{
            translate: no !important;
        }}

        /* 2. 侧边栏与头部：增加垫片防止内容重叠 */
        [data-testid="stSidebar"] {{ background-color: #0a0a0a !important; border-right: 1px solid #1a1a1a !important; }}
        [data-testid="stSidebarUserContent"] {{ padding-top: 4.5rem !important; }}
        header[data-testid="stHeader"] {{ background-color: rgba(0,0,0,0.85) !important; border-bottom: 1px solid #1a1a1a !important; height: 3.5rem !important; }}
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"] {{ display: none !important; }}

        /* 3. 【核心修复】彻底杀掉按钮内的 Ghost 文字 */
        /* 选中侧边栏控制按钮，强行将其原本的所有子元素(文字/图标)彻底抹除 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] * {{
            display: none !important;
            font-size: 0 !important;
            visibility: hidden !important;
        }}

        /* 4. 【核心修复】画三条杠 (纯 CSS) */
        [data-testid="stHeader"] button[data-testid*="Sidebar"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            width: 34px !important;
            height: 34px !important;
            position: relative !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            z-index: 100000 !important;
            overflow: hidden !important;
            text-indent: -9999px !important; /* 将可能残留的文本溢出出视野 */
        }}

        /* 利用伪元素绘制三条横杠 */
        [data-testid="stHeader"] button[data-testid*="Sidebar"]::after {{
            content: "" !important;
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: 16px !important;
            height: 2px !important;
            background-color: #888 !important; /* 中间杠 */
            box-shadow: 0 -5px 0 #888, 0 5px 0 #888 !important; /* 上下杠 */
            transition: all 0.2s ease !important;
        }}

        /* 悬停反馈 */
        [data-testid="stHeader"] button:hover::after {{
            background-color: #fff !important;
            box-shadow: 0 -5px 0 #fff, 0 5px 0 #fff !important;
        }}

        /* 5. 布局对齐锁死 (42px 物理平齐) */
        [data-testid="column"] {{
            display: flex !important;
            align-items: flex-end !important;
        }}
        div[data-testid="stNumberInput"] div[data-baseweb="input"],
        div[data-testid="stButton"] button {{
            height: 42px !important;
            min-height: 42px !important;
        }}
        div[data-testid="stNumberInput"] label {{ display: none !important; }}
        div[data-testid="stNumberInput"] input {{ height: 42px !important; }}
        div[data-testid="stButton"] button p {{ line-height: 42px !important; margin: 0 !important; font-size: 14px !important; }}

        /* 6. 响应式适配：解决平板端重叠 */
        @media (max-width: 1024px) {{
            [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap !important; gap: 10px !important; }}
            [data-testid="column"] {{ flex: 1 1 auto !important; min-width: 130px !important; }}
        }}
        @media (max-width: 768px) {{
            [data-testid="stHorizontalBlock"] {{ flex-direction: column !important; }}
            [data-testid="column"], div[data-testid="stNumberInput"], div[data-testid="stButton"] {{
                width: 100% !important;
                max-width: 100% !important;
            }}
        }}

        /* 其他组件配色 */
        :root {{ --primary-color: #C0C0C0 !important; }}
        .stButton > button {{ border: 1px solid #333 !important; background: #111 !important; }}
        .stTextArea textarea, .stTextInput input {{ background-color: #111111 !important; border: 1px solid #333333 !important; }}
    </style>
    """, unsafe_allow_html=True)
