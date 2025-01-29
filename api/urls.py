from django.urls import path, include

urlpatterns = [
    path('book/', include('apps.books.urls')),
    path('account/', include("apps.users.urls")),
    path('borrow/', include('apps.borrowing.urls')),
    path('review/', include("apps.reviews.urls")),
]
