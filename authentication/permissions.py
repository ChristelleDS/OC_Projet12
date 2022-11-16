from rest_framework import permissions
from .models import User


read_methods = ["GET"]


class UserPermission(permissions.BasePermission):
    message = "Permission denied. Only an admin can create or edit a user."

    def has_permission(self, request, view):
        if request.user.team in ('MANAGEMENT') \
                and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.team in ('MANAGEMENT'):
            return True
        elif request.method in read_methods:
            return True
        return False
