from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", login_required(views.AccountListView.as_view()), name="account-list"),
    re_path(r"(?P<account>\d+)/?$", login_required(views.AccountUsersListView.as_view()), name="account-users-list"),
]
