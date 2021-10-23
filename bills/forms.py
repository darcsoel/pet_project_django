from django import forms
from django.utils.translation import gettext_lazy as _

from account.models import Account
from bills.models import Bill
from user_profile.models import User


class BillForm(forms.ModelForm):
    from_account = forms.ModelChoiceField(queryset=Account.objects.all(), label=_("From account"))
    to_account = forms.ModelChoiceField(queryset=Account.objects.all(), label=_("To account"))
    from_user = forms.ModelChoiceField(queryset=User.objects.all(), label=_("From user"))
    to_user = forms.ModelChoiceField(queryset=User.objects.all(), label=_("To user"))
    payment = forms.IntegerField(label=_("Payment"))

    class Meta:
        model = Bill
        fields = ("from_account", "to_account", "from_user", "to_user", "payment")
