from django.db import models


class Nashriyot(models.Model):
    nomi = models.CharField(max_length=200)
    manzil = models.CharField(max_length=200)
    email = models.EmailField()
    telefon = models.CharField(max_length=13)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Nashriyotlar"
        verbose_name = "Nashriyot "

class Muallif(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    tugilgan_sana = models.DateField()
    rasm = models.ImageField(upload_to='muallif/rasmlar/', null=True, blank=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    class Meta:
        verbose_name_plural = "Mualliflar"
        verbose_name = "Muallif "

class Kitob(models.Model):
    nomi = models.CharField(max_length=150)
    janr = models.CharField(max_length=100)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    nashriyot = models.ForeignKey(Nashriyot, on_delete=models.SET_NULL, null=True)
    rasm = models.ImageField(upload_to='kitob/rasmlar/', null=True, blank=True)
    chop_etilgan_sana = models.DateField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Kitoblar"
        verbose_name = "Kitob "
