from rest_framework import serializers
from apps.borrowing.models import Borrowing

class BorrowingSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    # book = serializers.SerializerMethodField()
    
    class Meta:
        model = Borrowing
        fields = '__all__'
        
    def validate(self, data):
        book = Borrowing.objects.filter(user=data['user'], book=data['book'], is_returned=False)
        if book.exists():
            raise serializers.ValidationError({'error':'You have already borrowed this book!'})
        return data
    
    def validate_book(self, value):
        if not value.available:
            raise serializers.ValidationError("This book is currently unavailable")
        return value
    
    # def get_user(self, obj):
    #     return obj.user.username
    
    # def get_book(self, obj):
    #     return obj.book.name
    