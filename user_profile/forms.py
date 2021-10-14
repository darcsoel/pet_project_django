from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from account.models import Account
from user_profile.models import User, UserRolesEnum


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label=_("First name"), strip=False)
    last_name = forms.CharField(label=_("Last name"), strip=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First name"), strip=False)
    last_name = forms.CharField(label=_("Last name"), strip=False)
    username = forms.CharField(label=_("Username"), strip=False)
    email = forms.CharField(label=_("Email"), strip=False)
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    role = forms.ChoiceField(choices=UserRolesEnum.choices)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "role",
            "account",
            "first_name",
            "last_name",
        )

    def save(self, **kwargs):
        get_object_or_404(Account, pk=self.data["account"])
        return super().save(**kwargs)
