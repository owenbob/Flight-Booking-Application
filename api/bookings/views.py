"""Bookings class view."""

from flask.views import MethodView

from api.auth.auth_utils import token_needed


class Bookings(MethodView):
    """ View to handle Flight functionality."""
    decorators = [token_needed]

    def get(self, current_user):
        pass

    def post(self, current_user):
        pass

    def put(self, current_user):
        pass

    def delete(self, current_user):
        pass
