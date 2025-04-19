from django.urls import path, include
from rest_framework import routers

from .views import TeacherAPIViewSet, ClassAPIViewSet, StudentAPIViewSet

router = routers.DefaultRouter()
router.register('teachers', TeacherAPIViewSet, basename='teacher')
router.register('classes', ClassAPIViewSet, basename='class')
router.register('students', StudentAPIViewSet, basename='student')

urlpatterns = router.urls