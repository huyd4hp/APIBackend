from rest_framework.permissions import BasePermission

class IsManagerOrAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or (request.user.role == 'manager')
