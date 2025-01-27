from django.urls import path, include

urlpatterns = [
    path('book/', include('apps.books.urls')),
]
