from django.urls import path, include 
from apps.reviews.views import ReviewListAV, ReviewDetalisAV, UserReviewsAV

urlpatterns = [
    path('<int:id>/list', ReviewListAV.as_view(), name='review-list'),
    path('<int:book_id>/<int:review_id>', ReviewDetalisAV.as_view(), name='review-details'),
    path('info/', UserReviewsAV.as_view(), name='user-reviews'),
]
