from django.contrib.auth.models import User as DefaultUser
from django.db import models

from account.models import Account


class UserRolesEnum(models.TextChoices):
    USER = "user", "User"
    CUSTOMER = "customer", "Customer"
    DRIVER = "driver", "Driver"
    DISPATCHER = "dispatcher", "Dispatcher"
    MANAGER = "manager", "Manager"
    ADMIN = "admin", "Admin"


class User(DefaultUser):
    role = models.CharField(max_length=15, choices=UserRolesEnum.choices, default=UserRolesEnum.USER)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True)
