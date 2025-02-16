from django.shortcuts import render

from .models import Course, Student


# Create your views here.

def index_1(request):
    course = Course.objects.all()
    student = Student.objects.all()

    context = {
        'course': course,
        'student': student
    }

    return render(request, 'index_1.html', context)

def kursdagi_oquvchilar(request, course_id):
    kurs = Course.objects.filter(id=course_id)
    oquvchilar = Student.objects.filter(course_id=course_id)
    context = {
        'oquvchilar': oquvchilar,
        'kurs': kurs
    }
    return render(request, 'kursdagi_oquvchilar.html', context)

def oquvchi_haqida(request, student_id):
    kurs = Course.objects.all()
    oquvchi = Student.objects.get(id=student_id)
    context = {
        'oquvchi': oquvchi,
        'kurs': kurs
    }
    return render(request, 'oquvchi_haqida.html', context)