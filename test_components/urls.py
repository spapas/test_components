"""
test_components URL Configuration
"""
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("", include("test_components.core.urls")),
    path("admin/", admin.site.urls),
]
