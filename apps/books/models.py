from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="borrowed_books"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BorrowHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.borrowed_at}"
