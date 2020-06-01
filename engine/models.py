from django.db import models

# Create your models here.
class Character():
    name = models.CharField(max_length=200)
    birthPlace = models.CharField(max_length=200)

class Place():
    name = models.CharField(max_length=200)
