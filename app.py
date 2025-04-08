import streamlit as st
import ui_elements
import backend
import game_engine
import websocket_handler

# Initialize session state
if 'player_id' not in st.session_state:
    st.session_state['player_id'] = None
if 'game_state' not in st.session_state:
    st.session_state['game_state'] = None
if 'screen' not in st.session_state:
    st.session_state['screen'] = 'login'

# Function to handle routing
def route():
    if st.session_state['screen'] == 'login':
        login_screen()
    elif st.session_state['screen'] == 'main_menu':
        main_menu_screen()
    elif st.session_state['screen'] == 'game':
        game_screen()
    elif st.session_state['screen'] == 'chat':
        chat_screen()

# Login screen
def login_screen():
    st.sidebar.title("Carrom Pool Controller")
    player_id = st.sidebar.text_input("Enter Player ID", value=st.session_state['player_id'])
    if st.sidebar.button("Login"):
        st.session_state['player_id'] = player_id
        st.session_state['screen'] = 'main_menu'
        st.experimental_rerun()  # Rerun the script after updating session state

# Main menu screen
def main_menu_screen():
    st.title("Carrom Pool Game Controller")
    st.sidebar.button("Start Game", on_click=start_game)
    st.sidebar.button("Join Game", on_click=join_game)
    st.sidebar.button("Chat", on_click=go_to_chat)
    if st.session_state['player_id']:
        st.sidebar.write(f"Logged in as: {st.session_state['player_id']}")
    # Display player info
    player_info = backend.get_player_info(st.session_state['player_id'])
    st.write(player_info)

# Game screen
def game_screen():
    st.title("Carrom Pool Game")
    if st.session_state['game_state']:
        ui_elements.load_game_board(st.session_state['game_state'])
        ui_elements.load_striker_controller()
    if st.sidebar.button("Exit Game"):
        st.session_state['screen'] = 'main_menu'
        st.experimental_rerun()

# Chat screen
def chat_screen():
    st.title("Chat")
    ui_elements.load_chat_box()
    if st.sidebar.button("Back to Menu"):
        st.session_state['screen'] = 'main_menu'
        st.experimental_rerun()

# Helper functions to change screens
def start_game():
    st.session_state['game_state'] = game_engine.start_game(st.session_state['player_id'])
    websocket_handler.sync_game_state(st.session_state['game_state'])
    st.session_state['screen'] = 'game'
    st.experimental_rerun()

def join_game():
    st.session_state['game_state'] = game_engine.join_game(st.session_state['player_id'])
    websocket_handler.sync_game_state(st.session_state['game_state'])
    st.session_state['screen'] = 'game'
    st.experimental_rerun()

def go_to_chat():
    st.session_state['screen'] = 'chat'
    st.experimental_rerun()

# Main entry point for the app
if __name__ == "__main__":
    route()
