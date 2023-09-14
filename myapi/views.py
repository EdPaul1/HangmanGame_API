from django.shortcuts import render

import random
from .words import words
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer, GameStateSerializer

@api_view(['POST'])
def new_game(request):
    # Select a random word from the 'words' list
    word = random.choice(words)

    #max_incorrect_guesses based on word length
    if len(word) % 2 == 0: 
        max_incorrect_guesses = len(word) // 2
    else:
        max_incorrect_guesses = len(word) // 2 + 1

    # Create a new game instance
    game = Game.objects.create(
        word=word,
        current_state='_' * len(word),
        max_incorrect_guesses=max_incorrect_guesses,
        # Set initial status
        status='InProgress'  
    )

    serializer = GameSerializer(game)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def game_state(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return Response({'error': f'Game with ID {id} not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GameStateSerializer(game)
        return Response(serializer.data)
    

@api_view(['POST'])
def make_guess(request, id, guess):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        return Response({'error': f'Game with ID {id} not found'}, status=status.HTTP_404_NOT_FOUND)

    if game.status != 'InProgress':
        return Response({"error": "Game is already finished."}, status=status.HTTP_400_BAD_REQUEST)

    # Validate the guess
    if len(guess) != 1 or not guess.isalpha():
        return Response({"error": "Invalid guess. Please enter a single letter."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the guess is in the word
    word = game.word
    current_state = list(game.current_state)
    correct_guess = False  # Initialize the flag for correctness

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                current_state[i] = guess

        game.current_state = ''.join(current_state)
        game.save()

        if '_' not in game.current_state:
            game.status = 'Won'
            game.save()
        
        correct_guess = True  # Set the flag to True if the guess is correct
    else:
        game.incorrect_guesses += 1
        game.save()

        if game.incorrect_guesses >= game.max_incorrect_guesses:
            game.status = 'Lost'
            game.save()

    serializer = GameSerializer(game)
    response_data = serializer.data
    response_data['correct'] = correct_guess
    return Response(response_data)


