from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from user_profile.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label=_("First name"), strip=False)
    last_name = forms.CharField(label=_("Last name"), strip=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user
