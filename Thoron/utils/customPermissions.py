from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser == True

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser == True or obj.owner == request.user