from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from apps.users.views import registration_view, logout_view


urlpatterns = [
    path("register/", registration_view, name="registration"),
    path('login/', obtain_auth_token, name="login"),
    path("logout/", logout_view, name="registration"),
]
