
from rest_framework import permissions
from rest_framework.views import Request, View
from loans.models import Loan


class IsAdminOrLoanOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Loan) -> bool:
        return (
            obj.user == request.user
            or (request.method == "POST"
            and request.user.is_authenticated)
            
        )
