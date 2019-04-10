"""Auth utility functions."""

import datetime
import jwt

from api import app
from api.users.models import Users


def generate_user_token(data):

    # Assign request body entities
    email = data.get("email")
    password = data.get("password")

    # Validate data
    if not (email or password):
        raise AssertionError("Please provide email and password.")

    # check if email is for a registered user

    user = Users.query.filter(Users.email == email).first()

    if not user:
        raise AssertionError(
            "Details provided do not match any registered user."
        )

    # check is the provided password matches that of the user
    verified_password = Users.check_password(user.password_hash, password)

    if not verified_password:
        raise AssertionError("Please provide the right password")

    token = jwt.encode(
        {
            "email": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=50)
            },
        app.config["SECRET_KEY"],
        algorithm='HS256'
    )
    return token
