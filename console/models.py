from django.db import models

class ConsoleCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Console(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    image = models.CharField(max_length=999)
    price = models.FloatField()
    on_sale = models.BooleanField()
    category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name