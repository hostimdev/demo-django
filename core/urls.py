# core/urls.py - Add these paths
from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_to_users, name="redirect_to_users"),  # Updated
    path("users/", views.user_management, name="user_management"),
    path("users/add/", views.add_user, name="add_user"),
]
