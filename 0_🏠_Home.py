import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Quant AI Lab",
    page_icon="🏠",
    layout="centered"
)

#setting logos in the page
company_logo = Image.open("./figs/app-logo.png")
your_logo = Image.open("./figs/app-logo.png")

col1, col2, col3, col4, col5 = st.columns(5,  gap="large")

with col1:
    st.image(company_logo, width=300)
with col2:
    st.write("")
with col3:
    st.write("")
with col4:
    st.write("")
with col5:
    st.image(your_logo, width=300)

st.write("# Welcome to MyApp! 👋")

# st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Welcome to my app
"""
)

