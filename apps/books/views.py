from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.books.models import Book
from apps.books.serializers import BookSerializer

class BookListAV(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class BookDetailsAV(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
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
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)