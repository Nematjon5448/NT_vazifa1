from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    class_id = models.ManyToManyField(Class, related_name='teachers')

    def __str__(self):
        return self.full_name

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Class, models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return self.full_name