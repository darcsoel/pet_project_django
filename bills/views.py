from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from bills.models import Bill


class BillsListView(TemplateView):
    template_name = "bills/list.html"

    def get(self, request, *args, **kwargs):
        bills = Bill.objects.filter(Q(from_user_id=self.request.user) | Q(to_user_id=self.request.user))
        return render(request, self.template_name, context={"bills": bills})
