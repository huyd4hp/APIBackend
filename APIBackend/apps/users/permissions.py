from rest_framework.permissions import BasePermission

class IsOwnerOrAdminUser(BasePermission):
    def has_permission(self, request,view):
        return bool(request.user and request.user.is_staff)
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user