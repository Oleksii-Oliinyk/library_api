from rest_framework import serializers
from apps.borrowing.models import Borrowing

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'
    
    def validate_book(self, value):
        if value.available == False:
            raise serializers.ValidationError("This book is currently unavailable")
        return value