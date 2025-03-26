from rest_framework.permissions import BasePermission
from .models import RoleChoices

class IsLibrarian(BasePermission):
    """Allow access only to librarians."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == RoleChoices.LIBRARIAN

class IsMember(BasePermission):
    """Allow access only to members."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == RoleChoices.MEMBER
