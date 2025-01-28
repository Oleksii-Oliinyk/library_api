from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from apps.users.views import registration_view, logout_view, get_profile_info


urlpatterns = [
    path("register/", registration_view, name="registration"),
    path('login/', obtain_auth_token, name="login"),
    path("logout/", logout_view, name="registration"),
    path("profile/", get_profile_info, name="profile-info"),
]
