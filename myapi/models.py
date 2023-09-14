from django.db import models

# Create your models here.

class Game(models.Model):
    word = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
    incorrect_guesses = models.IntegerField(default=0)
    max_incorrect_guesses = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default='InProgress')
    remaining_incorrect_guesses = models.IntegerField(default=0)

    def __str__(self):
        return f"Game ID: {self.id}, Status: {self.status}"

    def save(self, *args, **kwargs):
        # Calculate remaining incorrect guesses when the model is saved
        self.remaining_incorrect_guesses = max(self.max_incorrect_guesses - self.incorrect_guesses, 0)
        super(Game, self).save(*args, **kwargs)