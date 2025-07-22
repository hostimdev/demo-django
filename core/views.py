# core/views.py - Add these functions
from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import UserProfile
from .forms import UserCreationForm


def redirect_to_users(request):
    return redirect("user_management")


def user_management(request):
    # Try to get users from Redis cache
    cache_key = "users_list"
    cached_users = cache.get(cache_key)
    data_source = "cache"

    if cached_users is None:
        # If not in cache, get from database
        users = UserProfile.objects.all().select_related("user")
        data_source = "database"

        # Store in Redis for 1 hour (3600 seconds)
        cache.set(cache_key, users, 3600)
    else:
        users = cached_users

    return render(
        request,
        "core/user_management.html",
        {"title": "User Management", "users": users, "data_source": data_source},
    )


def add_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Invalidate cache
            cache.delete("users_list")
            return redirect("user_management")
    else:
        form = UserCreationForm()

    return render(
        request, "core/user_management.html", {"title": "User Management", "form": form}
    )
