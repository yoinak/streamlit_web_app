import streamlit as st
from PIL import Image

st.title("中山アプリ")
st.caption("最初のアプリです")

image = Image.open("./data/boxplot.jpg")
st.image(image, width=400)
