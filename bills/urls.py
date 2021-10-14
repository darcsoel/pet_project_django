from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", login_required(views.BillsListView.as_view()), name="bills-list")
]
