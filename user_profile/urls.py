from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", login_required(views.ProfileView.as_view()), name="user-profile"),
    path("profile-edit", login_required(views.ProfileEditView.as_view()), name="user-profile-edit"),
    re_path(r"register/?", views.RegisterView.as_view(), name="register"),
    re_path(r"login/?", views.LoginView.as_view(), name="login"),
]
