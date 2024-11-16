import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Title of the app
st.title("Zomato Data Analysis")

# Upload the dataset
uploaded_file = st.file_uploader("Upload your Zomato CSV file", type="csv")

if uploaded_file is not None:
    # Load dataset into a DataFrame
    dataframe = pd.read_csv(uploaded_file)
    
    # Display dataset preview
    st.write("Dataset Preview:")
    st.write(dataframe.head())
    
    # Select which graphs to generate
    st.sidebar.subheader("Select Graph Types")
    graph_type = st.sidebar.multiselect(
        "Choose Graph Types to Display",
        ["Bar Chart", "Line Chart", "Histogram", "Box Plot"]
    )
    
    # Select columns for X and Y axes
    column_names = dataframe.columns.tolist()
    
    # Select X and Y axis columns
    x_column = st.sidebar.selectbox("Select X-axis column", column_names)
    y_column = st.sidebar.selectbox("Select Y-axis column", column_names)
    
    # Create different types of plots based on the user selection
    if "Bar Chart" in graph_type:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=dataframe[x_column], y=dataframe[y_column], ax=ax, palette="pastel")
        ax.set_title(f"Bar Chart: {y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    if "Line Chart" in graph_type:
        st.subheader("Line Chart")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(x=dataframe[x_column], y=dataframe[y_column], ax=ax, color="blue")
        ax.set_title(f"Line Chart: {y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)
    
    
    if "Histogram" in graph_type:
        st.subheader("Histogram")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(dataframe[y_column], kde=True, ax=ax, color="green", bins=20)
        ax.set_title(f"Histogram of {y_column}")
        ax.set_xlabel(y_column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    
    if "Box Plot" in graph_type:
        st.subheader("Box Plot")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(x=dataframe[x_column], y=dataframe[y_column], ax=ax, palette="muted")
        ax.set_title(f"Box Plot: {y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)
        
else:
    st.info("Please upload a Zomato CSV file to proceed.")
