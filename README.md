# Hangman Game API

This Django Rest Framework based API powers the frontend for a Hangman game. It provides endpoints for creating and managing Hangman games. A simple Streamlit frontend as been created to demonstrate the functionalities of the API.

![Streamlit Frontend](https://github.com/EdPaul1/HangmanGame_API/blob/main/assets/streamlit.png?raw=true)

## Table of Contents

- [API Endpoints](#api-endpoints)
  - [New Game](#new-game)
  - [Game State](#game-state)
  - [Guess](#guess)
- [Hangman Game Repository Setup Guide](#hangman-game-repository-setup-guide)
- [Prerequisites](#prerequisites)
- [Clone the Repository](#clone-the-repository)
- [Set Up the Virtual Environment](#set-up-the-virtual-environment)
- [Run Migrations](#run-migrations)
- [Run the Development Server](#run-the-development-server)
- [Start the Streamlit frontend](#start-the-streamlit-frontend)

## API Endpoints

### New Game

**Endpoint:** `/game/new`

Starts a new Hangman game and assigns a random word for the player to guess. The player is allowed to make incorrect guesses based on the word's length.

- **Method:** POST

#### Request Body

None

#### Response

- Status: 201 Created
- JSON Response Example:
  ![game/new](https://github.com/EdPaul1/HangmanGame_API/blob/main/assets/new_game.png?raw=true)
  
### Game State

**Endpoint:** `/game/<:id>`

Accepts a game ID and returns the current state of the game. The response includes:

  - The current state of the game (InProgress, Lost, or Won)

  - The current state of the word with underscores for unguessed letters

  - The number of incorrect guesses made
  - The number of remaining incorrect guesses

  - The maximum number of incorrect guesses allowed

 - **Method:** GET

Response

  Status: 200 OK
  JSON Response Example:
![game/<:id>](https://github.com/EdPaul1/HangmanGame_API/blob/main/assets/game_state.png?raw=true)

### Guess

**Endpoint:** `/game/<:id>/guess`

Accepts a single character as a guess and returns the updated game state, including whether the guess was correct or not.

  - **Method:** POST

Response

  Status: 200 OK
  JSON Response Example:
![/game/<:id>/guess](https://github.com/EdPaul1/HangmanGame_API/blob/main/assets/guess.png?raw=true)

## Hangman Game Repository Setup Guide

This guide will walk you through the process of cloning the Hangman Game repository, setting up the project locally, and running it using the provided `requirements.txt` file.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- **Python 3.x**: You can download Python from the [official website](https://www.python.org/downloads/).

## Clone the Repository
Open your terminal and navigate to the directory where you want to clone the repository. Then, run the following command:

```
git clone git@github.com:EdPaul1/HangmanGame_API.git
```
## Set Up the Virtual Environment
Navigate to the Project Directory: Change your working directory to the cloned project folder:

```
cd HangmanGame_API
```
Create a virtual environment to isolate project dependencies:
```
python -m venv venv
```
Activate the Virtual Environment:
On Windows:
```
venv\Scripts\activate
```
On macOS and Linux:
```
source venv/bin/activate
```
With the virtual environment activated, install the project dependencies listed in the requirements.txt file:
```
pip install -r requirements.txt
```
## Run Migrations
Use the following command to run migrations:
```
python manage.py migrate
```
This command will create the necessary database tables based on the project's models defined in the models.py file.

## Run the Development Server
Finally, you can run the Django development server to start the application:
```
python manage.py runserver
```
This command will start the server, and you can access the Django app in your web browser by navigating to the provided URL (usually http://localhost:8000/).

## Start the Streamlit frontend
Run:
```
streamlit run hangman_client.py
```
Congratulations! You have successfully cloned the repository, set up the project locally, and are now running the Hangman Game on your computer. Enjoy playing the game!
