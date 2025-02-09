import streamlit as st
import pandas as pd
import random

# Load the dataset
def load_data():
    url = "https://raw.githubusercontent.com/procountry/conflict-maxims/main/conflict_maxims.csv"  # Replace with actual raw URL
    df = pd.read_csv(url)
    return df

df = load_data()

# Function to get a random maxim
def get_random_maxim():
    return df.sample(1).iloc[0]  # ✅ This ensures a truly random selection

# Streamlit UI
st.title("Conflict Wisdom: Maxims & Strategy")

# Button to show a random maxim
if st.button("Show Random Maxim"):
    maxim = get_random_maxim()
    st.subheader(maxim["Maxim"])
    st.write(f"**Exploration:** {maxim['Exploration']}")
    st.write(f"**Connection to *The Art of War***: {maxim['Sun_Tzu_Connection']}")
