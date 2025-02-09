import streamlit as st
import pandas as pd

# Load dataset
def load_data():
    url = "https://raw.githubusercontent.com/procountry/conflict-maxims/main/conflict_maxims.csv"  # Replace with actual URL
    df = pd.read_csv(url)
    return df

df = load_data()

# Display the full dataset to check if maxims exist
st.title("🔍 Debugging: Checking the Dataset")
st.write("### Full Dataset Preview")
st.write(df)  # ✅ This will display ALL maxims

# Show total number of maxims
st.write(f"### Total Maxims: {len(df)}")
