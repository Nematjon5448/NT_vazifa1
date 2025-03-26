from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    sarlavha = models.CharField(max_length=200)
    tarkib = models.TextField()
    chop_etilgan_sana = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    korishlar_soni = models.PositiveIntegerField(default=0)
    muallif = models.CharField(max_length=100)

    def __str__(self):
        return self.sarlavha

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    sharh_matni = models.TextField()
    chop_etilgan_sana = models.DateTimeField(auto_now_add=True)