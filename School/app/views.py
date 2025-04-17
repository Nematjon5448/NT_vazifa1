from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Class, Teacher, Student
from .serializers import TeacherSerializer, ClassSerializer, StudentSerializer

class TeacherAPIViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClassAPIViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentAPIViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


