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
    maxim_row = df.sample(1).iloc[0]  # Pick a random row
    return {
        "maxim": maxim_row["Maxim"],
        "exploration": maxim_row["Exploration"],
        "connection": maxim_row["Sun_Tzu_Connection"]
    }

# ✅ Use Streamlit Session State to Store & Update Maxim
if "current_maxim" not in st.session_state:
    st.session_state.current_maxim = get_random_maxim()

# Streamlit UI
st.title("Conflict Wisdom: Maxims & Strategy")

# Button to show a random maxim
if st.button("Show Random Maxim"):
    st.session_state.current_maxim = get_random_maxim()  # ✅ Update session state

# ✅ Display the stored maxim (Ensures all fields change together)
st.subheader(st.session_state.current_maxim["maxim"])
st.write(f"**Exploration:** {st.session_state.current_maxim['exploration']}")
st.write(f"**Connection to *The Art of War***: {st.session_state.current_maxim['connection']}")
