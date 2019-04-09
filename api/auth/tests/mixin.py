"""Test Mixin Module for Auth Abstract class."""

from api.common.tests.basetest import BaseTestCase


class AuthAbstractClass(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.registration_url = "/v1/auth/register"

        self.user_data = {
            "first_name": "Owen",
            "last_name": "Byomuhangi",
            "email": "rolstar@gmail.com",
            "password": "12345Qwerty"
        }
