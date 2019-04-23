"""Bookings class view."""

from flask import jsonify, request
from flask.views import MethodView

from api.auth.auth_utils import token_needed
from api.flight.models import Flight, Seats
from api.bookings.utils import list_flights, view_flight


class BookingView(MethodView):
    """ View to handle Flight functionality."""
    decorators = [token_needed]

    def get(self, current_user):
        query = Flight.query.all()
        data = list_flights(query)
        return jsonify(data), 200

    def post(self, current_user):
        pass

    def put(self, current_user):
        pass

    def delete(self, current_user):
        pass


class FlightBookingView(MethodView):
    decorators = [token_needed]

    def get(self, current_user, flight_id):
        flight = Flight.query.filter(Flight.id == flight_id).first()
        if flight:
            data = view_flight(flight)
            return jsonify(data), 200
        data = {
            "status": "Failure",
            "message": "Flight with id {} Not found".format(flight_id)
                }
        return jsonify(data), 404
