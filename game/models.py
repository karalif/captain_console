from django.db import models
from console.models import ConsoleCategory
from console.models import Console

#class GameCategory(models.Model):
#    name = models.CharField(max_length=255)

class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    age_limit = models.CharField(max_length=999)
    price = models.FloatField()
    on_sale = models.BooleanField()
    category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    def __str__(self):
        return self.image