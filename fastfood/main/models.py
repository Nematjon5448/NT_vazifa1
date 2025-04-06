from django.db import models

class Burgerlar(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

class Lavashlar(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

class Ichimliklar(models.Model):
    name = models.CharField(max_length=100)
    liter = models.FloatField()
    price = models.PositiveIntegerField()

class Souslar(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
