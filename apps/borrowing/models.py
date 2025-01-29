from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from apps.books.models import Book

class Borrowing(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowed_books")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=None)
    is_returned = models.BooleanField(default=False)
    return_date = models.DateField(blank=True, null=True)
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review_book")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    