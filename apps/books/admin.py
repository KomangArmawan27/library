from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "is_borrowed", "borrowed_by")
    search_fields = ("title", "author")
    list_filter = ("is_borrowed",)

