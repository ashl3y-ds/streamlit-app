import streamlit as st
import pandas as pd

# Title
st.title("My Streamlit App")

# Description
st.write("This app allows you to upload and preview a dataset!")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of your dataset:")
    st.dataframe(df)
