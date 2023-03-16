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
        tab1, tab2, tab3 = st.tabs(["Tabular data", "Image", "Text"])

        with tab1:
            # Set tab1 header
            st.header("Exploratory Data Analysis - Understanding dataset")

            # Get dataset (*.csv) path from selection box
            dataset_path = st.selectbox(
                "Select dataset", glob(".\datasets\*.csv")
            )
            # Load dataframe from dataset path using pandas
            df = pd.read_csv(dataset_path)

            # Get & show dataset name
            dataset_name = Path(dataset_path).stem
            st.markdown("**Dataset Name:** **:green[{}]**".format(dataset_name))

            # Get & show dataset extension
            dataset_extension = Path(dataset_path).suffix
            st.markdown("**Dataset Extension:** **:green[{}]**".format(dataset_extension))

            # Get number of columns and rows
            df_shape = df.shape
            df_rowNum, df_colNum = df_shape[0], df_shape[1]
            st.markdown("**Number of rows:** **:green[{}]**".format(df_rowNum))
            st.markdown("**Number of columns:** **:green[{}]**".format(df_colNum))

            # Get feature/column names
            column_names = list(df.columns)
            st.markdown("**Column names:**")
            for col_name in column_names:
                st.markdown("- " + "**:green[{}]**".format(col_name))

            # Show dataframe
            st.dataframe(df, width=800)

            # Trigger button to show column/feature dtypes as dataframe
            if st.button(':tada: Get Dtypes'):
                st.markdown("**Column Dtypes:**")
                df_dtypes = pd.DataFrame(df.dtypes, columns=['Dtype'])
                df_dtypes.index.name = 'Columns'
                st.dataframe(df_dtypes)

            # Trigger button to show missing data
            if st.button(":rotating_light: Count Missing values"):
                st.markdown("**Number of missing values by columns:**")
                df_missing_count = pd.DataFrame(df.isnull().sum(), columns=['Count'])
                df_missing_count.index.name = 'Columns'
                st.dataframe(df_missing_count)
