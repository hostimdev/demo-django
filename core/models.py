# core/models.py - Add this class
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    status = models.CharField(max_length=100, default="Active")

    def __str__(self):
        return f"{self.user.username}'s profile"
