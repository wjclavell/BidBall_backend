from django.db import models
from apps.authentication.models import User

# Create your models here.
class Game(models.Model):
    sport = models.IntegerField()    # id number from 'rundown' ie: 3 = MLB, 2 = NFL
    event = models.IntegerField()    # id from 'rundown' will be used to associate user bid with specific game
    team1 = models.CharField(max_length=100)    # team names
    team2 = models.CharField(max_length=100)
    score1 = models.IntegerField(default=0)    # team scores
    score2 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sport}: {self.team1} v. {self.team2}'


class Bid(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   # associate a bid with its user
    game = Game.event   # associate a bid with specific game
    amount = models.IntegerField()
    team = models.CharField(max_length=100)    # user's choice of who will win
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.amount} | {self.team}'
