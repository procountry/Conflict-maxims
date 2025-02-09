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

# Function to get a new random maxim
def get_random_maxim():
    maxim_row = df.sample(1).iloc[0]  # Pick one random row
    return {
        "maxim": maxim_row["Maxim"],
        "exploration": maxim_row["Exploration"],
        "connection": maxim_row["Sun_Tzu_Connection"]
    }

# ✅ Ensure session state is initialized
if "current_maxim" not in st.session_state:
    st.session_state.current_maxim = get_random_maxim()

# Streamlit UI
st.title("Conflict Wisdom: Maxims & Strategy")

# Button to show a random maxim
if st.button("Show Random Maxim"):
    st.session_state.current_maxim = get_random_maxim()  # ✅ Update all fields together

# ✅ Display the stored maxim
st.subheader(st.session_state.current_maxim["maxim"])
st.write(f"**Exploration:** {st.session_state.current_maxim['exploration']}")
st.write(f"**Connection to *The Art of War***: {st.session_state.current_maxim['connection']}")
