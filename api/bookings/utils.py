"""utility functions for books."""


def list_flights(flights):
    """List view for flights."""
    return [view_flight(flight) for flight in flights]


def view_flight(flight):
    """Return a dict obj of a flight."""
    return {
        "id": flight.id,
        "departure_time": flight.departure_time,
        "departure_from": flight.departure_from,
        "destination": flight.destination,
        "created_at": flight.created_at,
        "updated_at": flight.Updated_at,
        "seats": seats(flight)
    }


def seats(flight):
    """Return dict obj of a seat."""
    if flight.seats is None:
        return {}
    else:
        return {
            "id": flight.seats.id,
            "number_of_seats": flight.seats.number_of_seats,
            "booked_seats": flight.seats.booked_seats,
            "available_seats": flight.seats.available_seats,
            "created_at": flight.seats.created_at,
            "updated_at": flight.seats.Updated_at
        }
