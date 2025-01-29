from rest_framework import serializers

from apps.reviews.models import Review
from apps.borrowing.models import Borrowing

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
    def validate(self, data):
        borrowing = Borrowing.objects.filter(book = data['book'], user = data['user'])
        if not borrowing.exists():
            raise serializers.ValidationError({"error": "You haven't read this book!"})
        if not borrowing.last().is_returned:
            raise serializers.ValidationError({"error": "You haven't returned this books yet!"})
        if self.instance is None:
            review = Review.objects.filter(book = data['book'], user = data['user'])
            if review.exists():
                raise serializers.ValidationError({"error": "You have already reviewed this book!"})
        return data