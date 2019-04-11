"""Initialize Flask Application."""

from flask import Flask

from api.configuration.config import ConfigureApplication

# Instantiate flask application
app = Flask(__name__)

# Set application environment configuration
app.config.from_object(ConfigureApplication.set_config())


# Set up application URLs
from api.auth.views import Register, Login # noqa E402
from api.flight.views import Flight # noqa E402

# Registration route
app.add_url_rule('/v1/auth/register/', view_func=Register.as_view("register"))

# Login route
app.add_url_rule('/v1/auth/login/', view_func=Login.as_view("login"))

# Flight route
app.add_url_rule('/v1/flight/', view_func=Flight.as_view("flight"))
