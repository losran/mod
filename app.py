import streamlit as st

st.set_page_config(layout="wide", page_title="Creative Engine")

st.title("Creative Engine")
st.caption("入口已隐藏，请从左侧直接进入功能模块")
print(get_github_data("data/usage.txt"))
