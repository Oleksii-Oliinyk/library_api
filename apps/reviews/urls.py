from django.urls import path, include 
from apps.reviews.views import ReviewListAV

urlpatterns = [
    path('<int:id>/list', ReviewListAV.as_view(), name='review-list'),
]
