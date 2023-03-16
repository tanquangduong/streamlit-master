import streamlit as st
import pandas as pd
from PIL import Image
from glob import glob
from pathlib import Path

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
                "**Select dataset**", glob(".\datasets\*.csv")
            )
            # Load dataframe from dataset path using pandas
            df = pd.read_csv(dataset_path)

            # Get number of columns and rows
            df_shape = df.shape
            df_rowNum, df_colNum = df_shape[0], df_shape[1]

            # Get feature/column names
            column_names = list(df.columns)

            # Show dataframe
            numRowDisplay = st.slider('**Choose number of row to display**', 1, df_rowNum, 3)
            st.dataframe(df.head(numRowDisplay), width=800)

            # Choose specific column for more statistical analysis
            chosen_column = st.selectbox(
                "**Select specific column for more statistical analysis**", column_names
            )

            # Show unique value count if chosen column dtype is Object
            if df[chosen_column].dtypes == 'O':
                df_unique = pd.DataFrame(df[chosen_column].value_counts(ascending=True))
                df_unique.rename(columns={chosen_column: 'count'}, inplace=True)
                df_unique.index.name = chosen_column

                # Streamlit widgets
                st.markdown("**Count unique values for string object**")
                st.dataframe(df_unique)

            # Show describe() method of chosen column
            df_des = pd.DataFrame(df[chosen_column].describe())
            df_des.rename(columns={chosen_column:'Value'}, inplace=True)
            df_des.index.name = 'Statistic info'
            # Streamlit widgets
            st.markdown("**Key statistic values**")
            st.dataframe(df_des)
