from django.urls import path, include 
from apps.borrowing.views import BorrowingAV, ReturningAV

urlpatterns = [
    path('take/<int:id>', BorrowingAV.as_view(), name='borrowing-book'),
    path('return/<int:id>', ReturningAV.as_view(), name='returning-book'),
]
