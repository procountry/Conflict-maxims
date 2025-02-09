import streamlit as st
import pandas as pd
import random

# Load the maxims dataset from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/conflict-maxims/main/conflict_maxims.csv"  # Replace with your actual raw file URL
    df = pd.read_csv(url)
    return df

df = load_data()

# Function to get a random maxim
def get_random_maxim():
    return df.sample(1).iloc[0]

# Streamlit UI
st.title("Conflict Wisdom: Maxims & Strategy")

# Display a random maxim
if st.button("Show Random Maxim"):
    maxim = get_random_maxim()
    st.subheader(maxim["Maxim"])
    st.write(f"**Exploration:** {maxim['Exploration']}")
    st.write(f"**Connection to *The Art of War***: {maxim['Sun_Tzu_Connection']}")

# Search for maxims
search_term = st.text_input("Search maxims by keyword")
if search_term:
    results = df[df["Maxim"].str.contains(search_term, case=False, na=False)]
    if not results.empty:
        for _, row in results.iterrows():
            st.subheader(row["Maxim"])
            st.write(f"**Exploration:** {row['Exploration']}")
            st.write(f"**Connection to *The Art of War***: {row['Sun_Tzu_Connection']}")
    else:
        st.warning("No matching maxims found.")
