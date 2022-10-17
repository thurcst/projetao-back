from time import clock_getres
from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if str(request.user) == "AnonymousUser":
            return False
        elif request.user or request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff
