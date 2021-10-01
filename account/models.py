from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=120, null=None)
    email = models.CharField(max_length=120, null=True, default="")
    address = models.CharField(max_length=120, null=True, default="")
