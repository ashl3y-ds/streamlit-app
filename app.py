import streamlit as st
import pandas as pd

# Title
st.title("My Streamlit App")

# Description
st.write("This app allows you to upload and preview a dataset!")

# File upload widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")  # Limiting to CSV files for clarity

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Show a message and the preview of the DataFrame
    st.write("Preview of your dataset:")
    st.dataframe(df)

    # Optionally display the shape of the dataset
    st.write(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")