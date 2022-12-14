from rest_framework import permissions


read_methods = ["GET"]
edit_methods = ["PUT", "PATCH", "DELETE"]


class EventPermission(permissions.BasePermission):

    message = "Permission denied. Only supportcontact or salescontact can edit event data."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or \
                request.method in read_methods:
            return True
        if request.user.team == 'MANAGEMENT':
            return True
        # check contract signature before creating a event
        if request.method == 'POST' and request.user.team == "SALES":
            return obj.status and obj.salescontact == request.user
        elif request.method in edit_methods and request.user.team == "SUPPORT":
            return obj.supportcontact == request.user
        elif request.method in edit_methods and request.user.team == 'SALES':
            return obj.contract.salescontact == request.user
        return False
