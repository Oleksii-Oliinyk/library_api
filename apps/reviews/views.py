from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.books.models import Book
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer
from apps.reviews.permissions import IsReviewUserOrReadOnly

def update_book_avg_rating(book_id):
    book = Book.objects.get(pk=book_id)
    avg = Review.objects.filter(book=book_id).aggregate(Avg('rating'))['rating__avg']
    book.avg_rating = avg if avg is not None else 0.0
    book.save()

class ReviewListAV(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, id):
        reviews = Review.objects.filter(book = id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        data = {
            "book":id,
            "user": request.user.pk,
            "rating": request.data['rating'],
            "comment": request.data.get('comment', '')
        }
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            update_book_avg_rating(id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReviewDetalisAV(APIView):
    permission_classes = [IsReviewUserOrReadOnly]
    
    def get(self, request, book_id, review_id):
        print(f"Received book_id: {book_id}, review_id: {review_id}")
        try:
            review = Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return Response({"error":"No such review!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, book_id, review_id):
        review = Review.objects.get(pk=review_id)
        data = {
            "book":book_id,
            "user": request.user.pk,
            "rating": request.data['rating'],
            "comment": request.data.get('comment', '')
        }
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            update_book_avg_rating(book_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            return Response({"Error":"No such review!"}, status=status.HTTP_404_NOT_FOUND)
        review.delete()
        update_book_avg_rating(book_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserReviewsAV(APIView):
    permission_classes = [IsReviewUserOrReadOnly]

    def get(self, request):
        review = Review.objects.filter(user=request.user)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)