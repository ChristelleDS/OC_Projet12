from rest_framework import permissions


read_methods = ["GET"]
create_methods = ["POST"]
edit_methods = ["PUT", "PATCH", "DELETE"]


class ClientPermission(permissions.BasePermission):

    message = "Permission denied. Only salescontact can edit client data."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or \
                request.method in read_methods:
            return True
        if request.user.team in ('MANAGEMENT'):
            return True
        if request.method in edit_methods \
                and request.user.team in ('SALES'):
            if obj.salescontact_id == request.user:
                return True
        return False
