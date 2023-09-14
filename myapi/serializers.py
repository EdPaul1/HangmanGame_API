from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('current_state', 'incorrect_guesses', 'max_incorrect_guesses', 'remaining_incorrect_guesses', 'status')
    
