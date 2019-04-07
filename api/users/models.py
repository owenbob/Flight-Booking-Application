""" User models module."""
import re
import uuid

from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

from api.common.models import BaseModel, db


class Users(BaseModel):
    """User Model."""
    __tablename__ = 'users'

    id = db.Column(
        db.String(80),
        nullable=False,
        primary_key=True,
        default=str(uuid.uuid4())
    )
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    profile_pic = db.Column(db.String(80), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def check_password(self, password):
        """Unhash password for easy reading."""
        return check_password_hash(password)

    def __repr__(self):
        """Return a string representation for the model."""
        return "User : {} {}".format(self.first_name, self.last_name)

    def set_password(self, password):
        """Hash password for security."""
        if not password:
            raise AssertionError("No password provided")
        if not re.match(r'\d.*[A-Z]|[A-Z].*\d', password):
            raise AssertionError(
                'Password must contain atleast a capital letter and a number'
            )
        if len(password) < 10 or len(password) > 30:
            raise AssertionError(
                'Password must be between 10 and 30 characters'
            )
        self.password_hash = generate_password_hash(password)

    @validates("email")
    def validate_email(self, key, email):
        """Validate email field input."""
        if not email:
            raise AssertionError("No email provided")
        query = Users.query.filter(Users.email == email).first()
        if query:
            raise AssertionError(
                "{} is already in use.Provide another email.".format(email)
            )

        pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        if not re.match(pattern, email):
            raise AssertionError("{} is an invalid email".format(email))
        return email

    @validates("first_name")
    def validate_first_name(self, key, first_name):
        """Validate first name field input."""
        first_name = Users.validate_entity(first_name, "First Name")
        return first_name

    @validates("last_name")
    def validate_last_name(self, key, last_name):
        """Validate first name field input."""
        last_name = Users.validate_entity(last_name, "Last Name")
        return last_name

    @staticmethod
    def validate_entity(entity, entity_name):
        """utility function for validating various entities."""
        if not entity:
            raise AssertionError("No {} provided".format(entity_name))
        if entity.split() == []:
            raise AssertionError("{} cannot be an empty string".format(
                entity_name
                )
            )
        if set(r'[~!@#$%^&*()_+{}":;\']+$').intersection(entity):
            raise AssertionError("{} cannot contain special characters".format(
                entity_name
                )
            )
        return entity
