from django.urls import path, include
from rest_framework import routers

from .views import TeacherAPIViewSet, ClassAPIViewSet, StudentAPIViewSet

router = routers.DefaultRouter()
router.register('teachers', TeacherAPIViewSet)
router.register('classes', ClassAPIViewSet)
router.register('students', StudentAPIViewSet)

urlpatterns = router.urls