import copy
import json

from django.core.exceptions import ValidationError
from django.test import TestCase

from account.forms import AccountForm
from account.models import Account
from bills.forms import BillForm
from bills.models import Bill
from user_profile.forms import UserForm
from user_profile.models import User
from user_profile.tests import UserFormUnitTest


class BillsTest(UserFormUnitTest):
    account_model = Account
    account_form = AccountForm

    user_model = User
    user_form = UserForm

    bill_model = Bill
    bill_form = BillForm

    def test_valid_case(self):
        account_data = {
            "name": "from account",
            "email": "test1@mail.com",
            "address": "some street",
        }
        from_account_form = self.account_form(data=account_data)
        self.assertTrue(from_account_form.is_valid())
        from_account = from_account_form.save()

        account_data = {
            "name": "to account",
            "email": "test2@mail.com",
            "address": "some street",
        }
        to_account_form = self.account_form(data=account_data)
        self.assertTrue(to_account_form.is_valid())
        to_account = to_account_form.save()

        user_data = copy.deepcopy(self.user_data)
        user_data.update(
            {
                "account": from_account.id,
                "email": "from@gmail.com",
                "role": "user",
            }
        )
        from_user_form = self.user_form(data=user_data)
        if not from_user_form.is_valid():
            raise ValidationError(message=json.dumps(from_user_form.errors))
        from_user = from_user_form.save()

        user_data = copy.deepcopy(self.user_data)
        user_data.update(
            {
                "username": "test_to@mail.com",
                "account": to_account.id,
                "email": "to@gmail.com",
                "role": "user",
            }
        )
        to_user_form = self.user_form(data=user_data)
        if not to_user_form.is_valid():
            raise ValidationError(message=json.dumps(to_user_form.errors))
        to_user = to_user_form.save()

        bill_form = self.bill_form(
            data={
                "from_account": from_account.id,
                "to_account": to_account.id,
                "from_user": from_user.id,
                "to_user": to_user.id,
                "payment": 100,
            }
        )
        if not bill_form.is_valid():
            raise ValidationError(message=json.dumps(bill_form.errors))
        bill = bill_form.save()
        self.assertTrue(bill.id)
