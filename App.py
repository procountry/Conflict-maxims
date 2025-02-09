import streamlit as st
import pandas as pd
import random

# Load the maxims dataset from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/procountry/Conflict-maxims/main/fresh_conflict_maxims-1.csv"  # 🔹 Replace with your actual raw file URL
    df = pd.read_csv(url)
    return df

df = load_data()

# Function to get a truly random maxim
def get_random_maxim():
    return df.sample(1).iloc[0]  # ✅ This ensures all fields update properly

# ✅ Ensure session state is initialized
if "current_maxim" not in st.session_state:
    st.session_state.current_maxim = get_random_maxim()

# Streamlit UI
st.title("🛡 Conflict Wisdom: Maxims & Strategy")

# Button to show a random maxim
if st.button("🔄 Show Random Maxim"):
    st.session_state.current_maxim = get_random_maxim()  # ✅ Update all fields

# ✅ Display the stored maxim (Ensures all fields change together)
st.subheader(st.session_state.current_maxim["Maxim"])
st.write(f"**💡 Exploration:** {st.session_state.current_maxim['Exploration']}")
st.write(f"**📖 Connection to *The Art of War***: {st.session_state.current_maxim['Sun_Tzu_Connection']}")
