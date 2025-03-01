from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kurs(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = 'Kurslar'
        verbose_name = 'Kurs '

class Dars(models.Model):
    nomi = models.CharField(max_length=100)
    mavzu = models.CharField(max_length=200)
    oqituvchi = models.CharField(max_length=100)
    xona = models.CharField(max_length=20)
    boshlanish_vaqti = models.TimeField()
    tugash_vaqti = models.TimeField()
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = 'Darslar'
        verbose_name = 'Dars '

class Comment(models.Model):
    matni = models.TextField()
    dars = models.ForeignKey(Dars, on_delete=models.CASCADE)
    foydalanuvchi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.foydalanuvchi.username}"

    class Meta:
        ordering = ['-pk']
