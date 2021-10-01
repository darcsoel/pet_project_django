from django.test import TestCase

from account.forms import AccountForm


class AccountTest(TestCase):
    def test_account_create_case1(self):
        account_data = {"name": "test account", "email": "test@mail.com", "address": "some street"}
        form = AccountForm(data=account_data)
        self.assertEqual(form.errors, {})

    def test_account_create_case2(self):
        account_data = {"name": "test account", "email": "test@mail.com", "address": ""}
        form = AccountForm(data=account_data)
        self.assertEqual(form.errors, {})

    def test_account_create_case3(self):
        account_data = {"name": "test account", "email": "", "address": "some street"}
        form = AccountForm(data=account_data)
        self.assertEqual(form.errors, {})

    def test_account_create_case4(self):
        account_data = {"name": "test account", "email": "", "address": ""}
        form = AccountForm(data=account_data)
        self.assertEqual(form.errors, {})

    def test_account_create_incorrect_case(self):
        account_data = {"name": "", "email": "", "address": ""}
        form = AccountForm(data=account_data)
        self.assertEqual(form.errors, {"name": ["This field is required."]})
