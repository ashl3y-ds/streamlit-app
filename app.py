import pandas as pd
import streamlit as st

# Title and description
st.title("Combine Multiple Datasets")
st.write("Upload multiple parts of your dataset to combine and process them!")

# Allow user to upload multiple files
uploaded_files = st.file_uploader(
    "Upload your dataset parts here",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files:
    dfs = []  # List to store each uploaded dataset
    
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        dfs.append(df)
        st.write(f"Preview of {uploaded_file.name}:")
        st.dataframe(df.head())
    
    # Combine all uploaded datasets into one
    combined_df = pd.concat(dfs, ignore_index=True)
    
    st.write("### Combined Dataset:")
    st.dataframe(combined_df.head())  # Show preview of the combined dataset

    # Optionally display the shape of the dataset
    st.write(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")