from django.contrib import admin

from .models import Course, Student

# Register your models here.

admin.site.register(Course)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'enrolled_at', 'course')

admin.site.register(Student, StudentAdmin)