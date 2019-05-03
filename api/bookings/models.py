"""Booking model module"""

import uuid

from api.common.models import BaseModel, db


class Booking(BaseModel):
    """Booking Model."""
    __tablename__ = "booking"
    id = db.Column(
        db.String(80),
        nullable=False,
        primary_key=True,
        default=str(uuid.uuid4())
    )
    flight_id = db.Column(db.String(50), db.ForeignKey('flight.id'))
    flight = db.relationship('Flight')
    customer = db.Column(db.String(50), db.ForeignKey('users.id'))
    seats_to_book = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Return a string representation for the model."""
        return "Booking: {} on {}".format(self.customer, self.flight_id)
