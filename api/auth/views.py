from flask import jsonify, request
from flask.views import MethodView

from api.users.models import Users


class Register(MethodView):
    """ View to handle user registration"""
    def post(self):
        data = request.get_json()

        # Assign request body entities
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        try:
            user = Users(
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password)

            # save user to database
            user.save(user)
            return jsonify(
                {
                    "status": "Success",
                    "message": "New user created successfully.",
                    "details": "{}".format(user),
                }), 201

        except AssertionError as error:
            return jsonify(
                {
                    "status": "Failure",
                    "Error": "{}".format(error)
                }
            ), 400


class Login(MethodView):
    """ View to handle user login"""
    def post(self):
        pass
