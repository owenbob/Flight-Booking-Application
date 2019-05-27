""" Module to generate email messages."""


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from api.emails.email_fixtures import generate_html_email


def flight_booking_confirmation(user, seats_booked, flight):
    """Generate an email to confirm a flight."""
    message = MIMEMultipart("alternative")
    message["Subject"] = "Flight Booking Confirmation"
    message["From"] = os.getenv("APP_EMAIL")
    message["To"] = user.email
    html = generate_html_email(user, seats_booked, flight)

    email_body = MIMEText(html, "html")
    message.attach(email_body)

    return message
