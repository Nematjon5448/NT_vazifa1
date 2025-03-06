from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class Rang(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi

class Brand(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Car(models.Model):
    nomi = models.CharField(max_length=100)
    rang = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    ot_kuchi = models.IntegerField()
    mator_hajmi = models.FloatField()
    rasm = models.ImageField(upload_to='car/photo')
    narx = models.IntegerField()

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse_lazy('mashina_batafsil', kwargs={'car_id': self.pk})

    class Meta:
        verbose_name_plural = 'Mashinalar'
        verbose_name = 'Mashina '

class Comment(models.Model):
    matni = models.TextField()
    mashina = models.ForeignKey(Car, on_delete=models.CASCADE)
    foydalanuvchi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.foydalanuvchi.username}"

    class Meta:
        ordering = ['-pk']
