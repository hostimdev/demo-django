# core/forms.py - Add this class
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["name", "email", "avatar"]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["email"],
            email=self.cleaned_data["email"],
            first_name=self.cleaned_data["name"],
        )

        profile = UserProfile(user=user)
        if "avatar" in self.cleaned_data and self.cleaned_data["avatar"]:
            profile.avatar = self.cleaned_data["avatar"]
        profile.save()

        return user
