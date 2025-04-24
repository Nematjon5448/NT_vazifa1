from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin' or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin' or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class CoursePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False


class GroupPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class StudentGroupPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class LessonPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class AttendancePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class LikePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user

class HomeworkPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif request.user.role in ['admin', 'teacher'] or request.user.is_superuser or request.user.is_staff:
            return True
        return False

class HomeworkStudentPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user