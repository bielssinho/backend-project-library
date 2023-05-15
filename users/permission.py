from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User
from rest_framework import permissions
from rest_framework.views import Request, View


class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_superuser or obj.pk == request.user.pk


class IsAdminOrLoanOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (request.user.is_authenticated and request.user.is_superuser) or request.method == "POST"
