"""Module to host sendgrid client."""

import os
import smtplib, ssl

from api.emails.email_message import flight_booking_confirmation


def send_mail(user, seats_booked, flight):
    try:
        sender_email = os.getenv("APP_EMAIL")
        context = ssl.create_default_context()
        message = flight_booking_confirmation(user, seats_booked, flight)
        with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), os.getenv("SSL_PORT"), context=context) as server:  # noqa: E501
            server.login(os.getenv("APP_EMAIL"), os.getenv("MAIL_KEY"))
            server.sendmail(
                sender_email, user.email, message.as_string()
            )
            server.close()
    except Exception as e:
        print("...Failed to send email because: {}".format(e))
