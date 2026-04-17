# config/urls.py
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
