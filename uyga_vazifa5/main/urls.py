from django.urls import path

from .views import index_1, kursdagi_oquvchilar, oquvchi_haqida

urlpatterns = [
    path('', index_1, name='home'),
    path('course/<int:course_id>', kursdagi_oquvchilar, name="kursdagi_oquvchilar"),
    path('oquvchi/<int:student_id>', oquvchi_haqida, name='oquvchi_haqida')
]