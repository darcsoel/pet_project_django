from django.contrib.auth.decorators import login_required
from django.urls import re_path, path

from . import views

urlpatterns = [
    path("", login_required(views.ProfileView.as_view()), name="user-profile"),
    re_path(r"register/?$", views.RegisterView.as_view(), name="register"),
    re_path(r"login/?$", views.LoginView.as_view(), name="login"),
]
