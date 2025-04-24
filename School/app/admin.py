from django.contrib import admin
from .models import Teacher, Student, Admin

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Admin)