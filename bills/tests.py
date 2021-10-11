from django.test import TestCase

from account.forms import AccountForm
from account.models import Account
from bills.forms import BillForm
from bills.models import Bill
from user_profile.forms import UserForm
from user_profile.models import User


class BillsTest(TestCase):
    account_model = Account
    account_form = AccountForm

    user_model = User
    user_form = UserForm

    bill_model = Bill
    bill_form = BillForm

    def test_valid_case(self):
        account_data = {"name": "from account", "email": "test1@mail.com", "address": "some street"}
        from_account_form = self.account_form(data=account_data)
        self.assertTrue(from_account_form.is_valid())
        from_account = from_account_form.save()

        account_data = {"name": "to account", "email": "test2@mail.com", "address": "some street"}
        to_account_form = self.account_form(data=account_data)
        self.assertTrue(to_account_form.is_valid())
        to_account = to_account_form.save()

        user_data = {}
