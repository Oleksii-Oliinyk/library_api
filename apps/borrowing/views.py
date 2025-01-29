import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.borrowing.serializers import BorrowingSerializer
from apps.borrowing.models import Borrowing
from apps.books.models import Book

class BorrowingAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            data = {
                'book': book.pk,
                'user': request.user.pk,
                'due_date': datetime.date.today() + datetime.timedelta(days=14),
            }
            serializer = BorrowingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                book.available = False
                book.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)     
        except Book.DoesNotExist:
            return Response({"error":"This book doesn't exists!"},status=status.HTTP_404_NOT_FOUND)
        
class ReturningAV(APIView):
    
    def post(self, request, id):
        try:
            borrowed_book = Borrowing.objects.filter(user=request.user, book=id).last()
            borrowed_book.is_returned = True
            borrowed_book.return_date = datetime.date.today()
            borrowed_book.save()
            
            book = Book.objects.get(pk=id)
            book.available = True
            book.save()
            
            serializer = BorrowingSerializer(borrowed_book)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Borrowing.DoesNotExist:
            return Response({"error":"You didn't borrow this book!"}, status=status.HTTP_404_NOT_FOUND)
        
class BorrowListAV(APIView):
    def get(self, request):
        borrowed_list = Borrowing.objects.filter(user=request.user)
        serializer = BorrowingSerializer(borrowed_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
            