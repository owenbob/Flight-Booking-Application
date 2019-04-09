"""Application Utility Functions."""

import datetime


FORMAT = "%d-%m-%y %H:%M:%S"


def time_utility():
    """Function to generate and return current time in favourable format."""
    current_time = datetime.datetime.now()
    return current_time.strftime(FORMAT)
