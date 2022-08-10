from django.db import models


# Create your models here.


class Persons(models.Model):
    index = models.IntegerField()
    name = models.TextField(max_length=100)
    gender = models.TextField(max_length=30)
    eyeColor = models.TextField(max_length=30)
    balance = models.TextField(max_length=100)
    tags = models.JSONField()
    friends = models.JSONField()
    greeting = models.TextField(max_length=200)
    favoriteFruit = models.TextField(max_length=100)
