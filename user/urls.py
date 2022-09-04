"""
user app url configurations:
/user/register-admin -> register new admins
/user/register-user  -> register new users
/get-auth-token      -> provide auth token on valid credentials 
"""

from django.urls import path
from .views import AdminRegistrationView, UserRegistrationView, CustomAuthToken


urlpatterns = [
    path("register-admin",AdminRegistrationView.as_view()),
    path("register-user",UserRegistrationView.as_view()),
    path("get-auth-token",CustomAuthToken.as_view())
]

