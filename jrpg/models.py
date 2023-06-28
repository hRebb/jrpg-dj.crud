from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    console = models.CharField(max_length=100)
    adaptation= models.CharField(max_length=100)
