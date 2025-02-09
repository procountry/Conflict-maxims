import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    url = "https://raw.githubusercontent.com/procountry/conflict-maxims/main/conflict_maxims.csv"  # Replace with your actual raw URL
    df = pd.read_csv(url)
    return df

df = load_data()

# Show the first 5 rows to check if the data is loading
st.title("Debug: Checking Dataset")
st.write(df.head())  # ✅ This will display 5 sample maxims
