from rest_framework import permissions
from epicEvents.appEvents.models import Client, Contract, Event


read_methods = ["GET"]
edit_methods = ("PUT", "PATCH", "DELETE")

class ClientPermission(permissions.BasePermission):

    message = "Permission denied. Only salescontact can edit client data."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.team in ('MANAGEMENT'):
            return True
        elif request.method in read_methods:
            return True
        elif request.method in edit_methods \
                and request.user.team in ('SALES'):
            if obj.salescontact_id == request.user:
                return True
        return False


class ContractPermission(permissions.BasePermission):

    message = "Permission denied. Only salescontact can edit contract data."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or \
                request.method in read_methods:
            return True
        if request.user.team in ('MANAGEMENT'):
            return True
        elif request.method in read_methods:
            return True
        elif request.method in edit_methods \
                and request.user.team in ('SALES'):
            if obj.salescontact_id == request.user:
                return True
        return False


class EventPermission(permissions.BasePermission):

    message = "Permission denied. Only supportcontact or salescontact can edit event data."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS or \
                request.method in read_methods:
            return True
        if request.user.team in ('MANAGEMENT'):
            return True
        elif request.method in read_methods:
            return True
        elif request.method in edit_methods \
                and request.user.team in ('SUPPORT'):
            if obj.supportcontact_id == request.user:
                return True
        elif request.method in edit_methods \
                and request.user.team in ('SALES'):
            if request.user == Client.objects.filter(id=obj.client_id).salescontact_id:
                return True
        return False
