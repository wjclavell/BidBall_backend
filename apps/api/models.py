from django.db import models
from apps.authentication.models import User

# Create your models here.
class Game(models.Model):
    sport = models.CharField(max_length=25)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sport}: {self.team1} v. {self.team2}'


class Bid(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
