from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    ])

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="users/teacher", null=True, blank=True)
    experience = models.IntegerField(default=1)
    class_id = models.ManyToManyField(Class, related_name='teachers')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Student(models.Model):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="users/student", null=True, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='students')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
