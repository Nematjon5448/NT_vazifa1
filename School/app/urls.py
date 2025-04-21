from rest_framework import routers

from .views import AdminAPIViewSet, TeacherAPIViewSet, ClassAPIViewSet, StudentAPIViewSet

router = routers.DefaultRouter()
router.register('teachers', TeacherAPIViewSet, basename='teacher')
router.register('classes', ClassAPIViewSet, basename='class')
router.register('students', StudentAPIViewSet, basename='student')
router.register('admins', AdminAPIViewSet, basename='admin')

urlpatterns = router.urls