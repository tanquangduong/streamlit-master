import streamlit as st
import pandas as pd
from PIL import Image

# Set page title, layout
st.set_page_config(page_title="My App Demo", layout="wide", initial_sidebar_state="expanded")

app_logo = Image.open("./figs/app-logo.png")
container = st.container()
c1, c2, c3 = st.columns([1, 3, 1])

with container:
    with c1:
        st.image(app_logo, width=150)

    with c2:
        st.markdown("<h1 style='text-align: center; color: #00B050 ;'> AI App </h1>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: #00163E ;'> Empower your business with AI-based solutions </h5>",
                    unsafe_allow_html=True)
        st.markdown("#")

        tab1, tab2, tab3 = st.tabs(["Train", "Inference", "Report"])

        with tab1:
            st.header("Train a model")
            st.write('Add more features below!')

        with tab2:
            st.header("Inference")
            st.write('Add more features below!')

        with tab3:
            st.header("Insight Dashboard")
            st.write('Add more features below!')