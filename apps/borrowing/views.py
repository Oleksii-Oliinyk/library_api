from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.borrowing.serializers import BorrowingSerializer
from apps.books.models import Book

class BorrowingAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            serializer = BorrowingSerializer(book=book, user=request.user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
                
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
            