from django.test import TestCase

from account.forms import AccountForm


class AccountTest(TestCase):
    form = AccountForm

    def _check_correct_data(self, account_data):
        form = self.form(data=account_data)
        self.assertEqual(form.errors, {})

    def _check_incorrect_data(self, account_data, expected_errors):
        form = self.form(data=account_data)
        self.assertEqual(form.errors, expected_errors)

    def test_account_create_case1(self):
        account_data = {"name": "test account", "email": "test@mail.com", "address": "some street"}
        self._check_correct_data(account_data)

    def test_account_create_case2(self):
        account_data = {"name": "test account", "email": "test@mail.com", "address": ""}
        self._check_correct_data(account_data)

    def test_account_create_case3(self):
        account_data = {"name": "test account", "email": "", "address": "some street"}
        self._check_correct_data(account_data)

    def test_account_create_case4(self):
        account_data = {"name": "test account", "email": "", "address": ""}
        self._check_correct_data(account_data)

    def test_account_create_incorrect_case_empty_data(self):
        account_data = {"name": "", "email": "", "address": ""}
        expected_errors = {"name": ["This field is required."]}
        self._check_incorrect_data(account_data, expected_errors)

    def test_account_create_incorrect_case_wrong_email(self):
        account_data = {"name": "test account", "email": "test account", "address": ""}
        expected_errors = {"email": ["Enter a valid email address."]}
        self._check_incorrect_data(account_data, expected_errors)
