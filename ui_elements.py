import streamlit as st

def load_striker_controller():
    st.subheader("Striker Controller")
    st.text("Controls to move the striker")

def load_game_board(game_state):
    st.subheader("Game Board")
    st.text(f"Game State: {game_state['state']}")

def load_chat_box():
    st.subheader("Chat Box")
    chat_history = st.empty()
    chat_input = st.text_input("Type your message here")
    if st.button("Send"):
        chat_history.text(chat_input)
        
# Neon dark theme using CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #222;
        color: #0f0;
    }
    .sidebar .sidebar-content {
        background-color: #111;
        color: #0f0;
    }
    .stButton>button {
        background-color: #444;
        color: #0f0;
        border: 1px solid #0f0;
    }
    .stTextInput>div>input {
        background-color: #333;
        color: #0f0;
        border: 1px solid #0f0;
    }
    .stTextArea>div>textarea {
        background-color: #333;
        color: #0f0;
        border: 1px solid #0f0;
    }
    .stSelectbox>div>div {
        background-color: #333;
        color: #0f0;
        border: 1px solid #0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
