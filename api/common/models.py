"""Application Parent Model."""
import uuid

from flask_sqlalchemy import SQLAlchemy

from api import app

from api.common.utils import time_utility

# Wrap app in ORM
db = SQLAlchemy(app)


class BaseModel(db.Model):
    """Parent Model for Application."""
    __abstract__ = True
    id = db.Column(
        db.String(80),
        nullable=False,
        primary_key=True,
        default=str(uuid.uuid4())
    )
    created_at = db.Column(db.DateTime, nullable=False, default=time_utility())
    Updated_at = db.Column(db.DateTime, nullable=False, default=time_utility())

    def save(self, obj):
        """Method to save values to the database."""
        db.session.add(obj)
        db.session.commit()
