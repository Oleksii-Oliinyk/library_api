from django.urls import path, include 
from apps.books.views import BookListAV

urlpatterns = [
    path('list/', BookListAV.as_view(), name='books-list'),
]
