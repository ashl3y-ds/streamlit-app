import pandas as pd
import streamlit as st

# Title and description
st.title("Combined Dataset Viewer")

# File uploads for two CSV files
uploaded_file1 = st.file_uploader("Upload the first CSV file", type=["csv"])
uploaded_file2 = st.file_uploader("Upload the second CSV file", type=["csv"])

if uploaded_file1 and uploaded_file2:
    # Read the uploaded CSV files
    df1 = pd.read_csv(uploaded_file1)
    df2 = pd.read_csv(uploaded_file2)
    
    # Combine the datasets
    combined_df = pd.concat([df1, df2], ignore_index=True)

    # Display combined dataset shape
    st.write(f"The combined dataset contains {combined_df.shape[0]} rows and {combined_df.shape[1]} columns.")

    # Display the combined dataset
    st.write("Here is a preview of the combined dataset:")
    st.dataframe(combined_df)