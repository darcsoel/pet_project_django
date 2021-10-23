from django.db import models

from account.models import Account
from user_profile.models import User


class Bill(models.Model):
    from_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="from_account")
    to_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="to_account")
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, related_name="to_user")
    payment = models.DecimalField(null=False, decimal_places=2, max_digits=15)
