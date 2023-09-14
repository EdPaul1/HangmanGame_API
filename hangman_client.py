import streamlit as st
import requests

# Set the API URL
API_URL = 'http://localhost:8000/'  # Replace with your Django API URL

st.image('assets/hangman.png', width=75)
st.title('Hangman Game')

# Streamlit UI elements go here
# Function to start a new game
def start_new_game():
    response = requests.post(API_URL + 'game/new/')
    if response.status_code == 201:
        game_data = response.json()
        return game_data
    else:
        return None

# Function to make a guess
def make_guess(game_id, guess):
    response = requests.post(API_URL + f'game/{game_id}/{guess}/')
    if response.status_code == 200:
        game_data = response.json()
        return game_data
    else:
        return None

# Function to get game state
def get_game_state(game_id):
    response = requests.get(API_URL + f'game/{game_id}/')
    if response.status_code == 200:
        game_state_data = response.json()
        return game_state_data
    else:
        return None

# Streamlit UI elements
if st.button('Start New Game'):
    game_data = start_new_game()
    if game_data:
        st.write(f'Started a new game with ID: {game_data["id"]}')

game_id = st.text_input('Enter Game ID:')
guess = st.text_input('Enter a Guess (single character):')

game_state_button = st.button('Game State')
if game_state_button:
    if game_id:
        game_state_data = get_game_state(game_id)
        if game_state_data:
            st.write(f'Game State for ID {game_id}:')
            st.write(f'Current State: {game_state_data["current_state"]}')
            st.write(f'Incorrect Guesses: {game_state_data["incorrect_guesses"]}')
            st.write(f'Remaining Incorrect Guesses: {game_state_data["remaining_incorrect_guesses"]}')


if st.button('Make Guess'):
    if game_id and guess:
        game_data = make_guess(game_id, guess)
        if game_data:
            st.write(f'Game Status: {game_data["status"]}')
            st.write(f'Current Word: {game_data["current_state"]}')

            if "correct" in game_data:
                if game_data["correct"]:
                    st.write(f'Your guess "{guess}" was correct!')
                else:
                    st.write(f'Your guess "{guess}" was incorrect.')
            st.write(f'Incorrect Guesses: {game_data["incorrect_guesses"]}')
            st.write(f'Remaining Incorrect Guesses: {game_data["remaining_incorrect_guesses"]}')


