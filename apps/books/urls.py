from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowedBooksView

router = DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("borrowed-books/", BorrowedBooksView.as_view(), name="borrowed-books"),

]
