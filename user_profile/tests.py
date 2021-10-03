from http import HTTPStatus

from django.test import Client, TestCase

from user_profile.forms import RegistrationForm


class RegisterIntegrationTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_register_form_filled_ok(self):
        user_data = {"username": "test@mail.com", "password1": "password123!@#", "password2": "password123!@#"}
        response = self.client.post("/account/register/", user_data, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class RegisterUnitTest(TestCase):
    def test_register_form_correct(self):
        user_data = {
            "username": "test@mail.com",
            "first_name": "John",
            "last_name": "Doe",
            "password1": "password123!@#",
            "password2": "password123!@#",
        }

        form = RegistrationForm(data=user_data)
        self.assertEqual(form.errors, {})

    def test_register_form_no_username(self):
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "password1": "password123!@#",
            "password2": "password123!@#",
        }
        err = {"username": ["This field is required."]}

        form = RegistrationForm(data=user_data)
        self.assertEqual(form.errors, err)

    def test_register_form_no_first_name(self):
        user_data = {
            "username": "test@mail.com",
            "last_name": "Doe",
            "password1": "password123!@#",
            "password2": "password123!@#",
        }
        err = {"first_name": ["This field is required."]}

        form = RegistrationForm(data=user_data)
        self.assertEqual(form.errors, err)

    def test_register_form_no_last_name(self):
        user_data = {
            "username": "test@mail.com",
            "first_name": "John",
            "password1": "password123!@#",
            "password2": "password123!@#",
        }
        err = {"last_name": ["This field is required."]}

        form = RegistrationForm(data=user_data)
        self.assertEqual(form.errors, err)

    def test_register_form_no_password(self):
        user_data = {
            "username": "test@mail.com",
            "first_name": "John",
            "last_name": "Doe",
            "password1": "password123!@#",
        }
        err = {"password2": ["This field is required."]}

        form = RegistrationForm(data=user_data)
        self.assertEqual(form.errors, err)
