from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=120, null=False)
    email = models.CharField(max_length=120, null=True, default="")
    address = models.CharField(max_length=120, null=True, default="")
