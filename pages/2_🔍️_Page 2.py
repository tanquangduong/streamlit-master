import os
import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path
from flowqast.preprocessing.preprocess import Preprocessing
from flowqast.preprocessing.utils import show_numeric_feature_info, show_object_feature_info
import hydralit_components as hc
from hydralit_components import HyLoader, Loaders
from PIL import Image

# make it look nice from the start
st.set_page_config(
    layout='wide',
    # initial_sidebar_state='collapsed'
)
# show Flowqast logo
your_logo = Image.open("./figs/app-logo.png")

col1, col2, col3, col4, col5 = st.columns(5,  gap="large")

with col1:
    st.write("")
with col2:
    st.write("")
with col3:
    st.write("")
with col4:
    st.write("")
with col5:
    st.image(your_logo, width=150)

# specify the primary menu definition
menu_data = [
    {'id': 'tab1',
     'icon': "🔎",
     'label': "Analysis"},
    {'id': 'tab2',
     'icon': "📃",
     'label': "DataViz"}
]

over_theme = {
    'menu_background': '#C04555',
    'txc_active': '#000000',
    'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    # home_name='Home',
    # login_name='Logout',
    hide_streamlit_markers=False,  # will show the st hamburger as well as the navbar now!
    sticky_nav=True,  # at the top or not
    sticky_mode='pinned',  # jumpy or not-jumpy, but sticky or pinned
)

with HyLoader("", loader_name=Loaders.pulse_bars):
    if menu_id == 'tab1':
        if 'dataframe' not in st.session_state:
            st.write("Import dataset first!")
        else:
            st.button('Do something')
    elif menu_id == "tab2":
        if 'dataframe' not in st.session_state:
            st.write("Import dataset first!")
        else:
            st.button('Do something')
