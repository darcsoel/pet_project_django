from django import forms
from django.utils.translation import gettext_lazy as _

from account.models import Account


class AccountForm(forms.ModelForm):
    name = forms.CharField(label=_("Account name"), strip=True, min_length=1)
    email = forms.EmailField(label=_("Email"), required=False)
    address = forms.CharField(label=_("Address"), strip=False, required=False)

    class Meta:
        model = Account
        fields = ("name", "email", "address")
