from django.shortcuts import render
from django.views.generic import TemplateView

from account.models import Account
from user_profile.models import User


class AccountListView(TemplateView):
    template_name = "account/list.html"

    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        return render(request, self.template_name, context={"accounts": accounts})


class AccountUsersListView(TemplateView):
    template_name = "account/user_list.html"

    def get(self, request, *args, **kwargs):
        users = User.objects.filter(account=kwargs.get("account"))
        return render(request, self.template_name, context={"users": users})
