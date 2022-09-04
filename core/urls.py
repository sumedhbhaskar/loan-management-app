"""
core URL Configuration
user app and loan apps are connected with core urls.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/",include("user.urls")),
    path("loan/",include("loan.urls"))
]
