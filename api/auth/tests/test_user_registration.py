"""Test User Registration."""

import json

from copy import copy

from api.auth.tests.mixin import AuthAbstractClass
# from api.users.models import Users  


class UserRegistrationTestCase(AuthAbstractClass):
    """Class to test user registration."""

    def generate_user_data_fixture(self):
        """Generate various copies of user_data."""
        return copy(self.user_data)

    def make_registration_request(self, data):
        """Make request for user registration with invalid user data."""
        return self.client.post(
                self.registration_url,
                content_type='application/json',
                data=json.dumps(data)
            )

    def test_user_registers_sucessfully(self):
        """Test that a user is created succesfully."""
        resp = self.make_registration_request(self.user_data)
        self.assertEqual(resp.status_code, 201)
        self.assertIn(self.user_data["first_name"], resp.json.get("details"))
        self.assertIn(self.user_data["last_name"], resp.json.get("details"))

    def test_user_registration_fails(self):
        """Test that user registration fails when invalid data is provided."""

        with self.subTest("With no password provided"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data.pop("password")
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn("No password provided", resp.json.get("Error"))

        with self.subTest("With password that contains no capital letter or number"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["password"] = "qwertyasdfgzxcvb"
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "Password must contain atleast a capital letter and a number",
                resp.json.get("Error")
            )

        with self.subTest("With password length not between 10 or 30 characters"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["password"] = "Qwerty123"
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "Password must be between 10 and 30 characters",
                resp.json.get("Error")
            )

        with self.subTest("With no email provided"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data.pop("email")
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn("No email provided", resp.json.get("Error"))

        with self.subTest("With email already used"):

            # register user
            self.make_registration_request(self.user_data)

            invalid_user_data = self.generate_user_data_fixture()
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "rolstar@gmail.com is already in use.Provide another email.",
                resp.json.get("Error")
            )

        with self.subTest("With an invalid email"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["email"] = "qwertyasdfgzxcvb.com"
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "qwertyasdfgzxcvb.com is an invalid email",
                resp.json.get("Error")
            )
        with self.subTest("With no first name provided"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data.pop("first_name")
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn("No First Name provided", resp.json.get("Error"))

        with self.subTest("With an empty string provided for first name"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["first_name"] = " "
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "First Name cannot be an empty string",
                resp.json.get("Error")
            )

        with self.subTest("With first name containing special characters"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["first_name"] = "S@den!"
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "First Name cannot contain special characters",
                resp.json.get("Error")
            )

        with self.subTest("With no last name provided"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data.pop("last_name")
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn("No Last Name provided", resp.json.get("Error"))

        with self.subTest("With an empty string provided for last name"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["last_name"] = " "
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "Last Name cannot be an empty string",
                resp.json.get("Error")
            )

        with self.subTest("With last name containing special characters"):
            invalid_user_data = self.generate_user_data_fixture()
            invalid_user_data["last_name"] = "R!ch@rl!$on"
            resp = self.make_registration_request(invalid_user_data)
            self.assertEqual(resp.status_code, 400)
            self.assertIn(
                "Last Name cannot contain special characters",
                resp.json.get("Error")
            )
