import streamlit as st
import pandas as pd
import random

# Load the maxims dataset from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/procountry/conflict-maxims/main/conflict_maxims.csv"  # Replace with your actual raw file URL
    df = pd.read_csv(url)
    return df

df = load_data()


# Function to get a random maxim
def get_random_maxim():
    maxim_row = df.sample(1).iloc[0]  # Get one random row
    return maxim_row["Maxim"], maxim_row["Exploration"], maxim_row["Sun_Tzu_Connection"]

# Streamlit UI
st.title("Conflict Wisdom: Maxims & Strategy")

# Button to show a random maxim
if st.button("Show Random Maxim"):
    maxim, exploration, connection = get_random_maxim()  # Ensure all three update
    st.subheader(maxim)
    st.write(f"**Exploration:** {exploration}")
    st.write(f"**Connection to *The Art of War***: {connection}")

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
