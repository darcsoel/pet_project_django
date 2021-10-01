from django.shortcuts import render
from django.views.generic import TemplateView

from account.models import Account


class AccountListView(TemplateView):
    template_name = "account/list.html"

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        return render(request, self.template_name, context={"accounts": accounts})
