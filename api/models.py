from django.db import models
from user.models import User

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)


class Review(models.Model):
    game_id = models.ForeignKey(Game,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    comment =  models.TextField(blank=True,null=True)
    grade = models.IntegerField()

class GameLists(models.Model):
    name = models.CharField(max_length=25, blank=False,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='profile_images',blank=True,null=True)
    games = models.ManyToManyField(Game)