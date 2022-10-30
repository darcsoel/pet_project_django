from django.contrib import admin

from .models import User


class UserExtended(admin.ModelAdmin):
    fields = ("role", "account")


admin.site.register(User, UserExtended)
