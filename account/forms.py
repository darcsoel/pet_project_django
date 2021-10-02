from django import forms

from account.models import Account
from django.utils.translation import gettext_lazy as _


class AccountForm(forms.ModelForm):
    name = forms.CharField(label=_("Account name"), strip=True)
    email = forms.CharField(label=_("Email"), strip=True, required=False)
    address = forms.CharField(label=_("Address"), strip=False, required=False)

    class Meta:
        model = Account
        fields = ("name", "email", "address")