import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from glob import glob
from pathlib import Path
from PIL import Image
import hydralit_components as hc
from hydralit_components import HyLoader, Loaders
from PIL import Image
import statsmodels.api as sm

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
    {'id': 'visualization',
     'icon': "📈",
     'label': "Visualization"},
    {'id': 'transformation',
     'icon': "〽️",
     'label': "Time Series Transformation"},
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
    if menu_id == "visualization":
        if 'dataframe' not in st.session_state:
            st.write("Please import Time-series dataset first.")
        else:
            loaded_dataframe = st.session_state.dataframe

            # for time feature
            date = st.selectbox( 'Please choose the timestamp column?', (loaded_dataframe.columns))   
            if 'date' not in st.session_state:
                st.session_state['date'] = date
            
            st.write(" ")
            multi_features = st.multiselect(
                'Please choose one or more features?',
                (loaded_dataframe.columns))
            
            
            
            if st.button('Visualaze'):
                st.line_chart(loaded_dataframe, x = date, y = multi_features)
                st.bar_chart(loaded_dataframe, x=date)

    elif menu_id == "transformation":
        if 'dataframe' not in st.session_state:
            st.write('Please import Time-series dataset first.')
        else:
            st.button('Do something')