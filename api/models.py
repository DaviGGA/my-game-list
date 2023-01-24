from django.db import models
from user.models import User

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)


class Review(models.Model):
    game_id = models.ForeignKey(Game,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    comment =  models.TextField(blank=True,null=True)
    grade = models.IntegerField()