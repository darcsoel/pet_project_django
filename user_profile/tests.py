import copy
import json
from http import HTTPStatus

from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from account.models import Account
from user_profile.forms import RegistrationForm, UserForm


class RegisterIntegrationTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_register_form_filled_ok(self):
        user_data = {"username": "test@mail.com", "password1": "password123!@#", "password2": "password123!@#"}
        response = self.client.post("/account/register/", user_data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class BaseUserFormTest(TestCase):
    form = RegistrationForm
    user_data = {
        "username": "test@mail.com",
        "first_name": "John",
        "last_name": "Doe",
        "password1": "password123!@#",
        "password2": "password123!@#",
    }

    def _check_correct_data(self, data):
        form = self.form(data=data)
        self.assertEqual(form.errors, {})
        user = form.save()
        self.assertTrue(user.id)

    def _check_incorrect_data(self, data, expected_errors):
        form = self.form(data=data)
        self.assertEqual(form.errors, expected_errors)
        with self.assertRaises(ValueError):
            form.save()


class RegisterFormUnitTest(BaseUserFormTest):
    def test_register_form_correct(self):
        self._check_correct_data(self.user_data)

    def test_register_form_no_username(self):
        user_data = copy.deepcopy(self.user_data)
        del user_data["username"]
        err = {"username": ["This field is required."]}
        self._check_incorrect_data(user_data, err)

    def test_register_form_no_first_name(self):
        user_data = copy.deepcopy(self.user_data)
        del user_data["first_name"]
        err = {"first_name": ["This field is required."]}
        self._check_incorrect_data(user_data, err)

    def test_register_form_no_last_name(self):
        user_data = copy.deepcopy(self.user_data)
        del user_data["last_name"]
        err = {"last_name": ["This field is required."]}
        self._check_incorrect_data(user_data, err)

    def test_register_form_no_password(self):
        user_data = copy.deepcopy(self.user_data)
        del user_data["password2"]
        err = {"password2": ["This field is required."]}
        self._check_incorrect_data(user_data, err)


class UserFormUnitTest(BaseUserFormTest):
    def test_with_existing_account(self):
        account_data = {"name": "test account", "email": "test@mail.com", "address": "some street"}
        account = Account.objects.create(**account_data)

        form = RegistrationForm(data=self.user_data)
        if not form.is_valid():
            raise ValidationError(message=json.dumps(form.errors))

        user = form.save()
        user_data = copy.deepcopy(self.user_data)
        user_data.update({"email": "test@gmail.com", "account": account.id, "role": "user"})

        user_form = UserForm(data=user_data, instance=user)
        if not user_form.is_valid():
            raise ValidationError(message=json.dumps(user_form.errors))

        user = user_form.save(commit=False)
        self.assertTrue(user.id)

    def test_with_not_existing_account(self):
        user_data = {
            "username": "test@mail.com",
            "first_name": "John",
            "last_name": "Doe",
            "account": 11111111111,
        }
        with self.assertRaises(ValidationError):
            user = UserForm(data=user_data).save()
            self.assertTrue(user.id)
