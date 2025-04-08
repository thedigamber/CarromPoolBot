import streamlit as st
import json
import os

# Initialize session state
if 'player_id' not in st.session_state:
    st.session_state['player_id'] = None
if 'player_data' not in st.session_state:
    st.session_state['player_data'] = {}

# Load player data from JSON file
def load_player_data():
    try:
        if os.path.exists('player_data.json'):
            with open('player_data.json', 'r') as f:
                st.session_state['player_data'] = json.load(f)
        else:
            st.session_state['player_data'] = {}
    except json.JSONDecodeError:
        st.session_state['player_data'] = {}
        st.error("Failed to load player data. The data file is corrupted or empty. Initializing empty data.")

# Save player data to JSON file
def save_player_data():
    with open('player_data.json', 'w') as f:
        json.dump(st.session_state['player_data'], f)

# Function to handle login
def login(player_id):
    st.session_state['player_id'] = player_id
    if player_id not in st.session_state['player_data']:
        st.session_state['player_data'][player_id] = {
            "coins": 1000,
            "diamonds": 50,
            "games_played": 0,
            "wins": 0
        }
    save_player_data()

# Sidebar for player login
with st.sidebar:
    st.title("Carrom Pool Client")
    player_id = st.text_input("Enter Player ID", value=st.session_state['player_id'] or "")
    if st.button("Login"):
        login(player_id)

# Load player data on start
load_player_data()

# Main layout
if st.session_state['player_id']:
    player_id = st.session_state['player_id']
    st.title(f"Welcome, Player {player_id}")

    player_data = st.session_state['player_data'][player_id]

    # Display player data
    st.json(player_data)

    # Buttons to add coins, diamonds, and wins
    if st.button("Add 100 Coins"):
        player_data["coins"] += 100
        save_player_data()
        st.rerun()

    if st.button("Add 50 Diamonds"):
        player_data["diamonds"] += 50
        save_player_data()
        st.rerun()

    if st.button("Simulate 1 Win"):
        player_data["games_played"] += 1
        player_data["wins"] += 1
        save_player_data()
        st.rerun()

else:
    st.title("Please log in to continue")
