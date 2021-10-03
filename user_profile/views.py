from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as DefaultLogin
from django.shortcuts import redirect, render

from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from user_profile.forms import RegistrationForm


class LoginView(DefaultLogin):
    redirect_authenticated_user = True


class RegisterView(TemplateView):
    template_name = "registration/register.html"
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("user-profile")

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("user-profile")

        form = self.form_class(request.POST)

        if not form.is_valid():
            msg = _("Unsuccessful registration. Wrong form data")
            messages.error(request, msg)
            context = {"errors": form.errors, "filled": request.POST}
            return render(request, self.template_name, context=context)

        user = form.save()
        login(request, user)

        return redirect("user-profile")


class ProfileView(TemplateView):
    template_name = "user_profile/profile.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, self.template_name, context={"profile_data": user})
