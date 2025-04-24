from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

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

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="users/teacher", null=True, blank=True)
    experience = models.IntegerField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to="users/student", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(default=8)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    started = models.DateField()
    finished = models.DateField()
    time_lesson = models.TimeField()
    days = models.CharField(max_length=20, choices=[
        ('du_chor_ju', 'Du-Chor-Ju'),
        ('se_pay_shan', 'Se-Pay-Shan'),
        ('har_kuni', 'Har kuni')
    ])

    def __str__(self):
        return self.name

class StudentGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} {self.group.name}"

class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    came = models.BooleanField(default=False)
    caming_time = models.TimeField()

class Like(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField()

class Homework(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    file = models.FileField(upload_to='homeworks/lessons', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

class HomeworkStudent(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    file = models.FileField(upload_to='homeworks/students/')
    created = models.DateTimeField(auto_now_add=True)
