from django import forms
from django.utils.translation import gettext_lazy as _

from bills.models import Bill


class BillForm(forms.ModelForm):
    from_account = forms.IntegerField(label=_("From account"))
    to_account = forms.IntegerField(label=_("To account"))
    from_user = forms.IntegerField(label=_("From user"))
    to_user = forms.IntegerField(label=_("To user"))
    payment = forms.IntegerField(label=_("Payment"))

    class Meta:
        model = Bill
        fields = (
            "from_account",
            "to_account",
            "from_user",
            "to_user",
            "payment",
        )
