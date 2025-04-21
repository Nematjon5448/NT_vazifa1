from django.contrib import admin
from .models import Teacher, Class, Student, Admin

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Admin)