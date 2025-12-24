import streamlit as st

st.set_page_config(layout="wide", page_title="Creative Engine")

st.title("Creative Engine")
st.caption("入口已隐藏，请从左侧直接进入功能模块")
if st.button("🧪 打印 Usage 仓库到控制台"):
    data = get_github_data("data/usage.txt")
    st.write(data)          # 页面显示
    print(data)             # 控制台显示
