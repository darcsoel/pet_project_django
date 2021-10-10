from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from account.forms import AccountForm
from account.models import Account


class AccountFormTest(TestCase):
    form = AccountForm

    def _check_correct_data(self, account_data):
        form = self.form(data=account_data)
        self.assertEqual(form.errors, {})
        account = form.save()
        self.assertTrue(account.id)

    def _check_incorrect_data(self, account_data, expected_errors):
        form = self.form(data=account_data)
        form.is_valid()
        self.assertEqual(form.errors, expected_errors)
        with self.assertRaises(ValueError):
            form.save()

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


class AccountModelTest(TestCase):
    model = Account

    def test_valid_model_create(self):
        data = {"name": "TestAccount", "email": "test@gmail.com", "address": "Some street"}
        account = self.model.objects.create(**data)
        self.assertTrue(account.id)

    def test_account_model_empty_name(self):
        data = {"name": None, "email": "test@gmail.com", "address": "Some street"}

        with self.assertRaises(IntegrityError):
            self.model.objects.create(**data)
