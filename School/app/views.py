from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import (Teacher, Student, Admin, User, Course,
                     Group, StudentGroup, Attendance,
                     Lesson, Like, HomeworkStudent, Homework)
from .serializers import (TeacherSerializer, StudentSerializer, AdminSerializer,
                          CourseSerializer, GroupSerializer, StudentGroupSerializer,
                          AttendanceSerializer, LessonSerializer, LikeSerializer,
                          HomeworkSerializer, HomeworkStudentSerializer)

from .permissions import (AdminPermission, TeacherPermission, StudentPermission,
                          CoursePermission, GroupPermission, StudentGroupPermission,
                          AttendancePermission, LessonPermission, LikePermission,
                          HomeworkPermission, HomeworkStudentPermission)

class AdminAPIViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [AdminPermission]

class TeacherAPIViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [TeacherPermission]

class StudentAPIViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [StudentPermission]


class CourseAPIViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]

class GroupAPIViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [GroupPermission]

class StudentGroupAPIViewSet(ModelViewSet):
    queryset = StudentGroup.objects.all()
    permission_classes = [StudentGroupPermission]

class AttendanceAPIViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [AttendancePermission]

class LessonAPIViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]

class LikeAPIViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [LikePermission]

class HomeworkAPIViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [HomeworkPermission]

class HomeworkStudentAPIViewSet(ModelViewSet):
    queryset = HomeworkStudent.objects.all()
    serializer_class = HomeworkStudentSerializer
    permission_classes = [HomeworkStudentPermission]


