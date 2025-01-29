from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer
from apps.reviews.permissions import IsReviewUserOrReadOnly

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReviewDetalisAV(APIView):
    permission_classes = [IsReviewUserOrReadOnly]
    
    def get(self, request, book_id, review_id):
        try:
            review = Review.objects.get(pk=review_id, book=book_id)
        except Review.DoesNotExist:
            return Response({"error":"No such review!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, book_id, review_id):
        review = Review.objects.get(pk=review_id, book=book_id)
        data = {
            "book":book_id,
            "user": request.user.pk,
            "rating": request.data['rating'],
            "comment": request.data.get('comment', '')
        }
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id, review_id):
        try:
            review = Review.objects.get(pk=review_id, book=book_id)
        except Review.DoesNotExist:
            return Response({"Error":"No such review!"}, status=status.HTTP_404_NOT_FOUND)
        
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserReviewsAV(APIView):
    permission_classes = [IsReviewUserOrReadOnly]

    def get(self, request):
        review = Review.objects.filter(user=request.user)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)