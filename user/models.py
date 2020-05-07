from django.db import models
from django.contrib.auth.models import User
from game.models import Games

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_game=models.ForeignKey(Games, on_delete=models.CASCADE)
    profile_image=models.CharField(max_length=9999)
