import streamlit as st

def apply_pro_style():
    # 加载品牌字体
    font_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Poppins:wght@400;500;600&display=swap"
    
    st.markdown(f"""
    <style>
        @import url('{font_url}');

        /* ==============================
           1. 全局字体与防重叠垫片
           ============================== */
        html, body, [class*="css"], font, span, div, h1, h2, h3, h4, h5, h6, p, a, button, input, textarea, label {{
            font-family: 'Poppins', 'Noto Sans SC', sans-serif !important;
            color: #d0d0d0;
        }}

        /* 侧边栏垫片：把内容拉下来，防止跟顶部按钮撞车 */
        [data-testid="stSidebarUserContent"] {{
            padding-top: 4.5rem !important; 
        }}
        
        [data-testid="stSidebar"] {{ 
            background-color: #0a0a0a !important; 
            border-right: 1px solid #1a1a1a !important;
            z-index: 99998 !important; 
        }}

        /* ==============================
           2. 按钮终极消音 (彻底杀掉 keyboard_... 文字)
           ============================== */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] {{
            border: 1px solid #333 !important;
            background-color: #111 !important;
            border-radius: 4px !important;
            width: 38px !important;
            height: 38px !important;
            position: relative !important;
            z-index: 100000 !important;
            
            /* 强制抹除原有内容 */
            color: transparent !important;
            font-size: 0 !important;
            line-height: 0 !important;
        }}

        /* 杀掉所有原生子元素 */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"] *,
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"] * {{
            display: none !important;
            font-size: 0 !important;
        }}

        /* ==============================
           3. “打字”生成新箭头 (使用 Unicode 字符)
           ============================== */
        
        /* 通用样式：把字写在正中心 */
        [data-testid="stHeader"] button::after {{
            display: block !important;
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -55%) !important; /* 垂直微调 */
            font-size: 16px !important; /* 控制箭头大小 */
            color: #888 !important;
            font-family: Arial, sans-serif !important; /* 确保使用通用字体显示字符 */
            transition: all 0.2s ease !important;
        }}

        /* ---> 侧边栏收起：打一个“右箭头”字 */
        [data-testid="stHeader"] button[data-testid="stSidebarCollapsedControl"]::after {{
            content: "▶" !important;
        }}

        /* <--- 侧边栏展开：打一个“左箭头”字 */
        [data-testid="stHeader"] button[data-testid="stSidebarExpandedControl"]::after {{
            content: "◀" !important;
        }}

        /* Hover 高亮 */
        [data-testid="stHeader"] button:hover {{
            border-color: #fff !important;
            background-color: #222 !important;
        }}
        [data-testid="stHeader"] button:hover::after {{
            color: #fff !important;
        }}

        /* ==============================
           4. 其他界面去噪
           ============================== */
        [data-testid="stToolbarActions"], [data-testid="stStatusWidget"], [data-testid="stDecoration"]
