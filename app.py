import pandas as pd
import streamlit as st

# Title
st.title("Dataset Viewer and Preprocessor")

# Sidebar navigation
menu = st.sidebar.radio(
    "Menu",
    ["Upload and Combine Data", "Preprocess Data", "View Combined Dataset"]
)

# Variables to store combined data
combined_df = None

# Upload and Combine Data
if menu == "Upload and Combine Data":
    st.header("Upload Datasets")
    uploaded_file1 = st.file_uploader("Upload the first CSV file", type=["csv"])
    uploaded_file2 = st.file_uploader("Upload the second CSV file", type=["csv"])
    
    if uploaded_file1 and uploaded_file2:
        # Load CSV files
        df1 = pd.read_csv(uploaded_file1)
        df2 = pd.read_csv(uploaded_file2)
        
        # Combine datasets
        combined_df = pd.concat([df1, df2], ignore_index=True)
        st.success("Datasets combined successfully!")
        st.write(f"The combined dataset contains {combined_df.shape[0]} rows and {combined_df.shape[1]} columns.")
        
        # Save the combined data to a session state for later use
        st.session_state["combined_df"] = combined_df

# Preprocess Data
elif menu == "Preprocess Data":
    st.header("Preprocessing Options")
    
    # Load data from session state
    if "combined_df" in st.session_state:
        combined_df = st.session_state["combined_df"]
        
        # Handle missing values
        if st.checkbox("Remove rows with missing values"):
            combined_df = combined_df.dropna()
            st.success("Missing values removed.")
            st.write(f"Updated dataset contains {combined_df.shape[0]} rows and {combined_df.shape[1]} columns.")
        
        # Filter numeric columns
        numeric_columns = combined_df.select_dtypes(include=['float64', 'int64']).columns
        if not numeric_columns.empty:
            selected_column = st.selectbox("Select a numeric column to filter:", numeric_columns)
            if selected_column:
                min_val = st.number_input(f"Minimum {selected_column}:", value=float(combined_df[selected_column].min()))
                max_val = st.number_input(f"Maximum {selected_column}:", value=float(combined_df[selected_column].max()))
                combined_df = combined_df[(combined_df[selected_column] >= min_val) & (combined_df[selected_column] <= max_val)]
                st.success(f"Filtered dataset on {selected_column}.")
                st.write(f"Updated dataset contains {combined_df.shape[0]} rows.")
        
        # Save updated dataset
        if st.button("Save Preprocessed Data"):
            combined_df.to_csv("preprocessed_dataset.csv", index=False)
            st.success("Preprocessed dataset saved as preprocessed_dataset.csv!")
            
    else:
        st.warning("Please upload and combine datasets first!")

# View Combined Dataset
elif menu == "View Combined Dataset":
    st.header("View Combined Dataset")
    
    # Load data from session state
    if "combined_df" in st.session_state:
        combined_df = st.session_state["combined_df"]
        st.write("Here is your combined dataset:")
        st.dataframe(combined_df)
    else:
        st.warning("Please upload and combine datasets first!")
