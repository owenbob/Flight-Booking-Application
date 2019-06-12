
from api.common.tests.basetest import BaseTestCase


class GrantAdminTestCase(BaseTestCase):
    """Test whether on can grant user admin rights."""

    def test_granting_admin_rights_is_successful(self):
        # grant user admin rights
        self.test_user_one.is_admin = True
        self.test_user_one.save(self.test_user_one)

        # attempt to grant admin rights
        resp = self.make_flight_request(
            operation="post",
            url=self.grant_admin_url,
            content_type="application/json",
            headers=self.headers
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json.get("message"),
            "{} granted admin rights.".format(self.test_user_two)
        )
        self.assertEqual(resp.json.get("status"), "Success")

    def test_granting_admin_rights_is_unsuccessful(self):
        with self.subTest("With Invalid user id"):
            # attempt to grant admin rights
            resp = self.make_flight_request(
                operation="post",
                url="/v1/users/99a0-4d9f-b748-bbcec21/",
                content_type="application/json",
                headers=self.headers
            )
            self.assertEqual(resp.status_code, 404)
            self.assertEqual(resp.json.get("status"), "Failure")
            self.assertEqual(
                resp.json.get("message"),
                "{} not found.".format(self.test_user_two)
            )

        with self.subTest("With user who has no admin rights"):
            # revoke user admin rights
            self.test_user_one.is_admin = False
            self.test_user_one.save(self.test_user_one)

            # attempt to grant admin rights
            resp = self.make_flight_request(
                operation="post",
                url=self.grant_admin_url,
                content_type="application/json",
                headers=self.headers
            )

            self.assertEqual(resp.status_code, 403)
