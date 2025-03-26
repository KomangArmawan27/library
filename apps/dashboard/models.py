from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Q
from apps.users.models import User
from apps.books.models import Book, BorrowHistory

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """Returns dashboard statistics based on user role"""
    user = request.user

    total_books = Book.objects.count()
    borrowed_books = Book.objects.filter(is_borrowed=True).count()
    total_members = User.objects.filter(role="member").count()

    # For librarians only: Track overdue books
    overdue_books = 0
    if user.role == "librarian":
        overdue_books = BorrowHistory.objects.filter(
            returned_at__isnull=True,  # Not returned
            borrowed_at__lt="now() - interval '14 days'"  # Overdue for 14+ days
        ).count()

    data = {
        "total_books": total_books,
        "borrowed_books": borrowed_books,
        "total_members": total_members,
        "overdue_books": overdue_books if user.role == "librarian" else None
    }

    return Response(data)
