from django.db import models

class scoreboard(models.Model):
    human_wins = models.IntegerField()
    computer_wins = models.IntegerField()
