from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nomi')
    description = models.TextField(verbose_name='Tavsifi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Kurslar'
        verbose_name = 'Kurs '

class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ismi")
    email = models.EmailField(verbose_name="Pochtasi")
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Kursi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Talabalar'
        verbose_name = 'Talaba '