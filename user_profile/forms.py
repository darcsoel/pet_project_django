from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from account.models import Account
from user_profile.models import User, UserRolesEnum


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


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First name"), strip=False)
    last_name = forms.CharField(label=_("Last name"), strip=False)
    username = forms.CharField(label=_("Username"), strip=False)
    email = forms.CharField(label=_("Email"), strip=False)
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    role = forms.ChoiceField(choices=UserRolesEnum.choices)

    class Meta:
        model = User
        fields = ("username", "email", "role", "account", "first_name", "last_name")

    def save(self, **kwargs):
        if not Account.objects.filter(id=self.data["account"]).count():
            raise ValidationError(message="Account do not exists")

        return super().save(**kwargs)
