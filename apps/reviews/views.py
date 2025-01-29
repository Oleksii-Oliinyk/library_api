from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer

class ReviewListAV(APIView):
    permission_classes = [IsAuthenticated]
    
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
        
