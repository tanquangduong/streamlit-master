import streamlit as st
import pandas as pd
from PIL import Image
from glob import glob
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set page title, layout
st.set_page_config(page_title="My App Demo", layout="wide", initial_sidebar_state="expanded")

# Load logo image
app_logo = Image.open("./figs/app-logo.png")

# Create container for app
container = st.container()

# Create layout with 3 columns with the ratio 1:3:1
c1, c2, c3 = st.columns([1, 3, 1])

with container:
    with c1:  # First column for app logo
        st.image(app_logo, width=150)

    with c2:  # Second column for all features
        # Set App title, slogan, etc
        st.markdown("<h1 style='text-align: center; color: #00B050 ;'> AI App </h1>", unsafe_allow_html=True)
        st.markdown(
            "<h5 style='text-align: center; color: #00163E ;'> Empower your business with AI-based solutions </h5>",
            unsafe_allow_html=True)
        st.markdown("#")

        # Create 3 tabs (pages)
        tab1, tab2, tab3 = st.tabs(["**Tabular data**", "**Image**", "**Text**"])

        with tab1:
            # Set tab1 header
            st.header("Exploratory Data Analysis - Understanding dataset")

            # Get dataset (*.csv) path from selection box
            dataset_path = st.selectbox(
                ":rocket:**Select dataset**", glob(".\datasets\*.csv")
            )
            # Load dataframe from dataset path using pandas
            df = pd.read_csv(dataset_path)

            # Get number of columns and rows
            df_shape = df.shape
            df_rowNum, df_colNum = df_shape[0], df_shape[1]

            # Get feature/column names
            column_names = list(df.columns)

            # Show dataframe
            st.dataframe(df, width=800)

            # Choose one of two specific columns
            st.markdown(":white_check_mark:**Please select one or more columns:**")
            check_boxes = [st.checkbox(col_name, key=col_name) for col_name in column_names]
            selected_columns = [col_name for col_name, checked in zip(column_names, check_boxes) if checked]
            if len(selected_columns) != 0:
                st.markdown("**You selected:** **:green[{}] column(s)**".format(selected_columns))

            # Choose ONE column for visualization
            st.markdown(":chart_with_upwards_trend:**Visualization:**")
            col_viz = st.radio('Select one column:', column_names)
            st.markdown("**You selected:** **:green[{}] column for visualization.**".format(col_viz))

            # Trigger button to do dataviz on one column
            if st.button("**Histogram**"):
                if df[col_viz].dtypes != 'O':
                    fig, ax = plt.subplots(figsize=(10, 4))
                    num_bins = 100
                    ax.hist(df[col_viz], num_bins,
                            density=1,
                            color='green',
                            alpha=0.7)
                    ax.set_title('Histogram of \'{}\' column'.format(col_viz), fontdict={'fontsize': 15, 'fontweight': 'bold'})
                    ax.set_xlabel('Category', fontsize=15, fontweight='bold')
                    ax.set_ylabel('Sum', fontsize=15, fontweight='bold')
                    # Hide the right and top spines
                    ax.spines[['right', 'top']].set_visible(False)

                    st.pyplot(fig)
                else:
                    st.markdown("**:red[_Please choose numerical column for histogram!_]**")


