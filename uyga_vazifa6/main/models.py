from django.db import models

# Create your models here.

class Brand(models.Model):
    nomi = models.CharField(max_length=50)
    davlati = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi

class Car(models.Model):
    model = models.CharField(max_length=80)
    ot_kuchi = models.IntegerField()
    rangi = models.CharField(max_length=50)
    narxi = models.IntegerField()
    rasmi = models.ImageField(upload_to='car/photo', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model