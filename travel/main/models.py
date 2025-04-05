from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Klass(models.Model):
    nomi = models.CharField(max_length=150)
    narxi = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Klasslar'
        verbose_name = 'Klass '

    def __str__(self):
        return self.nomi

class Mehmonxona(models.Model):
    nomi = models.CharField(max_length=150)
    yulduzlar_soni = models.PositiveIntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(5)
    ])
    narxi = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Mehmoxonalar'
        verbose_name = 'Mehmonxona '

    def __str__(self):
        return self.nomi

class Travel(models.Model):
    nomi = models.CharField(max_length=150)
    izoh = models.TextField()
    muddati = models.DateField()
    narxi = models.PositiveIntegerField()
    klass = models.ForeignKey(Klass, on_delete=models.SET_NULL, null=True)
    mehmonxona = models.ForeignKey(Mehmonxona, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Travellar'
        verbose_name = 'Travel '

    def __str__(self):
        return self.nomi