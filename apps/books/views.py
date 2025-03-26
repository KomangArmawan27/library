import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.books.permissions import IsLibrarian
from .models import Book, BorrowHistory
from .serializers import BookSerializer
from datetime import datetime

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    author = django_filters.CharFilter(lookup_expr="icontains")
    is_avaliable = django_filters.BooleanFilter()

class BorrowHistoryFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    book = django_filters.CharFilter(field_name="book__title", lookup_expr="icontains")
    returned = django_filters.BooleanFilter(field_name="returned_at", lookup_expr="isnull", exclude=True)

class BorrowHistoryPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = "limit"  
    max_page_size = 100

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ["title", "author"]
    pagination_class = BorrowHistoryPagination

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsLibrarian()]
        return [permissions.IsAuthenticated()]
    
    # ✅ Borrow Book (Members Only)
    @action(detail=True, methods=["POST"], permission_classes=[permissions.IsAuthenticated])
    def borrow(self, request, pk=None):
        book = self.get_object()
        if book.is_borrowed:
            return Response({"error": "Book is already borrowed."}, status=status.HTTP_400_BAD_REQUEST)

        book.is_borrowed = True
        book.borrowed_by = request.user
        book.save()

        # Save borrow history
        BorrowHistory.objects.create(user=request.user, book=book)

        return Response({"message": "Book borrowed successfully."}, status=status.HTTP_200_OK)

    # ✅ Return Book (Only Member Who Borrowed It)
    @action(detail=True, methods=["POST"], permission_classes=[permissions.IsAuthenticated])
    def return_book(self, request, pk=None):
        book = self.get_object()
        if not book.is_borrowed or book.borrowed_by != request.user:
            return Response({"error": "You cannot return this book."}, status=status.HTTP_400_BAD_REQUEST)

        book.is_borrowed = False
        book.borrowed_by = None
        book.save()

        # Update borrow history
        history = BorrowHistory.objects.filter(user=request.user, book=book, returned_at__isnull=True).first()
        if history:
            history.returned_at = datetime.now()
            history.save()

        return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)

    # ✅ Get Borrow History (Librarians Only)
    @action(detail=False, methods=["GET"])
    def history(self, request):
        if not request.user.role=="librarian":  
            return Response({"error": "Access denied."}, status=status.HTTP_403_FORBIDDEN)

        # history = BorrowHistory.objects.all().select_related("user", "book")
        history = BorrowHistory.objects.all()
        filterset = BorrowHistoryFilter(request.GET, queryset=history)

        if not filterset.is_valid():
            return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Apply pagination
        page = self.paginate_queryset(filterset.qs)
        if page is not None:
            return self.get_paginated_response([
                {
                    "user": h.user.username,
                    "book": h.book.title,
                    "borrowed_at": h.borrowed_at,
                    "returned_at": h.returned_at,
                }
                for h in page
            ])

        # If pagination not needed, return normally
        return Response([
            {
                "user": h.user.username,
                "book": h.book.title,
                "borrowed_at": h.borrowed_at,
                "returned_at": h.returned_at,
            }
            for h in filterset.qs
        ])
