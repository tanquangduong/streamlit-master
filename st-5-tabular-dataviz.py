import streamlit as st
import pandas as pd
from PIL import Image
from glob import glob
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import mpld3
import streamlit.components.v1 as components

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
                ":white_check_mark:**Select dataset**", glob(".\datasets\*.csv")
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

            # Choose ONE column for visualization
            st.markdown(":white_check_mark:**Visualization**")
            col_viz = st.radio('Select one column:', column_names)
            st.markdown("**You selected:** **:green[{}] column with dtype: :green[{}] for visualization.**".format(col_viz, df[col_viz].dtypes))
            if df[col_viz].dtypes == 'O':
                st.markdown("**:red[_Please choose \'numerical\' column for visualization!_]**")
            else:
                # Show describe() method of chosen column
                df_des = pd.DataFrame(df[col_viz].describe())
                df_des.rename(columns={col_viz: 'Value'}, inplace=True)
                df_des.index.name = 'Statistic info'
                # Streamlit widgets
                st.markdown("**Key statistic values**")
                st.dataframe(df_des)

            # Display histogram with Matplotlib
            if df[col_viz].dtypes != 'O':
                st.markdown(":chart_with_upwards_trend:**:green[Histogram with Matplotlib]**")

                # Show slide to select 'bin' value for Matplotlib's histogram
                binMatplotlib = st.slider('**Choose `bin` value:**', 1, 100, 50, key=1)

                # Create figure with matplotlib
                fig_plt, ax_plt = plt.subplots(figsize=(10, 4))
                ax_plt.hist(df[col_viz], binMatplotlib,
                        color='green',
                        edgecolor="black",
                        alpha=0.7)
                ax_plt.set_title('Histogram of \'{}\' column by Matplotlib'.format(col_viz),
                             fontdict={'fontsize': 15, 'fontweight': 'bold'})
                ax_plt.set_xlabel('{}'.format(col_viz), fontsize=15, fontweight='bold')
                ax_plt.set_ylabel('Count', fontsize=15, fontweight='bold')
                # Hide the right and top spines
                ax_plt.spines[['right', 'top']].set_visible(False)

                # Display figure on streamlit
                st.pyplot(fig_plt)

                # Display histogram with Seaborn
            if df[col_viz].dtypes != 'O':
                st.markdown(":chart_with_upwards_trend:**:green[Histogram with Seaborn]**")

                # Show slide to select 'bin' value for Matplotlib's histogram
                binSeaborn = st.slider('**Choose `bin` value:**', 1, 100, 50, key=2)

                # Create figure with matplotlib
                fig_sns, ax_sns = plt.subplots(figsize=(10, 4))
                g = sns.histplot(data=df,
                                 x=col_viz,
                                 bins=binSeaborn,
                                 color='g',
                                 ax=ax_sns)
                g.set_title('Histogram of \'{}\' column by Seaborn'.format(col_viz),
                            fontdict={'fontsize': 15, 'fontweight': 'bold'})
                g.set_xlabel('{}'.format(col_viz), fontsize=15, fontweight='bold')
                g.set_ylabel('Count', fontsize=15, fontweight='bold')
                sns.despine()

                # Display figure on streamlit
                st.pyplot(fig_sns)

            # Display ECDF with Matplotlib, plot with st.pyplot
            if df[col_viz].dtypes != 'O':
                st.markdown(":chart_with_upwards_trend:**:green[ECDF (Empirical Cumulative Distribution Function) with Matplotlib]**")

                df_quantile = df.sort_values(col_viz, ascending=True)
                percentage_list = np.arange(0, 1.01, 0.01)
                amount_quantile = df_quantile[col_viz].quantile(percentage_list)
                df_ecdf = pd.DataFrame({"amount_quantile": amount_quantile, "percentage_list": percentage_list},
                                       index=percentage_list)
                quantile_50 = df_ecdf.loc[0.50, 'amount_quantile']
                quantile_80 = df_ecdf.loc[0.80, 'amount_quantile']
                quantile_100 = df_ecdf.loc[1.0, 'amount_quantile']

                # Create ECDF plot with matplotlib
                fig_ecdf, ax_ecdf = plt.subplots(figsize=(10, 4))

                ax_ecdf.plot(df_ecdf.amount_quantile, df_ecdf.percentage_list,
                             color='g', linestyle='-', marker="+")

                ax_ecdf.vlines([quantile_50], ymin=0, ymax=0.5, linestyles='--', color='k', linewidth=1)
                ax_ecdf.hlines([0.50], xmin=0, xmax=quantile_50, linestyles='--', color='k', linewidth=1)

                ax_ecdf.vlines([quantile_80], ymin=0, ymax=0.8, linestyles='--', color='k', linewidth=1)
                ax_ecdf.hlines([0.80], xmin=0, xmax=quantile_80, linestyles='--', color='k', linewidth=1)

                ax_ecdf.vlines([quantile_100], ymin=0, ymax=1.0, linestyles='--', color='k', linewidth=1)
                ax_ecdf.hlines([1.0], xmin=0, xmax=quantile_100, linestyles='--', color='k', linewidth=1)

                ax_ecdf.set_yticks([0, 0.5, 0.8, 1], labels=['0', '50%', '80%', '100%'], weight='bold')
                ax_ecdf.set_xticks([quantile_50, quantile_80, quantile_100],
                              labels=[str(round(quantile_50)), str(round(quantile_80)), str(round(quantile_100))],
                              rotation=20,
                              weight='bold')

                ax_ecdf.set_ylim([0, 1.05])
                ax_ecdf.set_xlim([df_ecdf.amount_quantile[0], df_ecdf.amount_quantile[1]])
                ax_ecdf.set_xlabel("{}".format(col_viz), weight='bold', fontsize=15)
                ax_ecdf.set_ylabel('ECDF (%)', weight='bold', fontsize=15)
                ax_ecdf.set_title("ECDF for \'{}\'".format(col_viz), weight='bold', fontsize=15, y=1.02)

                # Hide the right and top spines
                ax_ecdf.spines[['right', 'top']].set_visible(False)

                # Plot with st.pyplot
                st.pyplot(fig_ecdf)

            # Display ECDF with Matplotlib, plot with fig_html for zooming interatively
            if df[col_viz].dtypes != 'O':
                st.markdown(
                    ":chart_with_upwards_trend:**:green[ECDF (Empirical Cumulative Distribution Function) with Zoom In-Out features]**")

                # Create ECDF plot with matplotlib
                fig_html = plt.figure(figsize=(8,6))

                plt.plot(df_ecdf.amount_quantile, df_ecdf.percentage_list,
                         linestyle='-', marker="+", color='g', linewidth=2)

                plt.vlines([quantile_50], ymin=0, ymax=0.5, linestyles='--', color='k', linewidth=1)
                plt.hlines([0.50], xmin=0, xmax=quantile_50, linestyles='--', color='k', linewidth=1)

                plt.vlines([quantile_80], ymin=0, ymax=0.8, linestyles='--', color='k', linewidth=1)
                plt.hlines([0.80], xmin=0, xmax=quantile_80, linestyles='--', color='k', linewidth=1)

                plt.vlines([quantile_100], ymin=0, ymax=1.0, linestyles='--', color='k', linewidth=1)
                plt.hlines([1.0], xmin=0, xmax=quantile_100, linestyles='--', color='k', linewidth=1)

                plt.xlabel("{}".format(col_viz), weight='bold', fontsize=15)
                plt.ylabel('ECDF (%)', weight='bold', fontsize=15)
                plt.title("ECDF for {}".format(col_viz), weight='bold', fontsize=15, y=1.02)

                plt.xlim([df_ecdf.amount_quantile[0], df_ecdf.amount_quantile[1]])
                plt.ylim([0, 1.05])

                # Plot with mpld3 & components.html
                fig_html = mpld3.fig_to_html(fig_html)
                components.html(fig_html, width=800, height=600)

            # Choose one of two specific columns
            # st.markdown(":white_check_mark:**Please select one or more columns for data manipulation (later)**")
            # check_boxes = [st.checkbox(col_name, key=col_name) for col_name in column_names]
            # selected_columns = [col_name for col_name, checked in zip(column_names, check_boxes) if checked]
            # if len(selected_columns) != 0:
            #     st.markdown("**You selected:** **:green[{}] column(s)**".format(selected_columns))


