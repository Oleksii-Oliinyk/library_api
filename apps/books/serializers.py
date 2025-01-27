from rest_framework import serializers
from apps.books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description cannot be the same')
        else:
            return data 
        
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name is too short')
        return value