from django.urls import path, include 
from apps.books.views import BookListAV, BookDetailsAV

urlpatterns = [
    path('list/', BookListAV.as_view(), name='book-list'),
    path('<int:id>', BookDetailsAV.as_view(), name='book-details')
]
