from django.shortcuts import render
from .models import Course, Student

# Create your views here.

def course(request):
    kurs = Course.objects.all()
    student = Student.objects.all()
    context = {
        'course': kurs,
        'student': student
    }
    return render(request, 'index_1.html', context)