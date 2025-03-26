from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    """
    Allows access only to librarians.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "librarian")
