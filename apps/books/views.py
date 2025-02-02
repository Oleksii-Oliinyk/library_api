from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.books.models import Book
from apps.books.serializers import BookSerializer
from apps.books.permissions import IsAdminOrReadOnly

class BookListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
class BookDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try: 
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return Response({"Error":"No such book!"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)