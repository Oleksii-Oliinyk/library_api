from rest_framework import serializers
from apps.borrowing.models import Borrowing
from django.contrib.auth.models import User
from apps.books.models import Book

class BorrowingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_name = serializers.SerializerMethodField()

    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_name = serializers.SerializerMethodField()

    class Meta:
        model = Borrowing
        fields = ['id', 'user', 'user_name', 'book', 'book_name', 'borrow_date', 'due_date', 'is_returned', 'return_date']

    def validate(self, data):
        book = Borrowing.objects.filter(user=data['user'], book=data['book'], is_returned=False)
        if book.exists():
            raise serializers.ValidationError({'error':'You have already borrowed this book!'})
        return data
    
    def validate_book(self, value):
        if not value.available:
            raise serializers.ValidationError("This book is currently unavailable")
        return value

    def get_user_name(self, obj):
        return obj.user.username

    def get_book_name(self, obj):
        return obj.book.name
    