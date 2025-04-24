from rest_framework import routers

from .views import (AdminAPIViewSet, TeacherAPIViewSet, StudentAPIViewSet,
                    CourseAPIViewSet, GroupAPIViewSet, StudentGroupAPIViewSet,
                    LessonAPIViewSet, AttendanceAPIViewSet, LikeAPIViewSet,
                    HomeworkAPIViewSet, HomeworkStudentAPIViewSet)

router = routers.DefaultRouter()
router.register('teachers', TeacherAPIViewSet, basename='teacher')
router.register('students', StudentAPIViewSet, basename='student')
router.register('admins', AdminAPIViewSet, basename='admin')
router.register('courses', CourseAPIViewSet, basename='course')
router.register('groups', GroupAPIViewSet, basename='group')
router.register('group-students', StudentGroupAPIViewSet, basename='group-student')
router.register('lessons', LessonAPIViewSet, basename='lesson')
router.register('attendances', AttendanceAPIViewSet, basename='attendance')
router.register('likes', LikeAPIViewSet, basename='like')
router.register('homeworks', HomeworkAPIViewSet, basename='homework')
router.register('homework-students', HomeworkStudentAPIViewSet, basename='homework-student')

urlpatterns = router.urls