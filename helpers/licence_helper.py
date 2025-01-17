import random
import string
from datetime import datetime, timedelta


def generate_multiple(amount: int) -> list:
    licenses = []
    for i in range(amount):
        licenses.append(generate_single())
    return licenses


def generate_single() -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=30))


def construct_expiration_date(license_duration_hours: int) -> datetime:
    """
     Return format:
    Y-M-D H:M:S.mS
    :param license_duration_hours: int hours to be added to current date
    :return: datetime current time incremented by param license_duration_hours

    """
    expiration_date = datetime.now() + timedelta(hours=license_duration_hours)
    return expiration_date


def get_remaining_time(expiration_date: str) -> str:
    """
    :param expiration_date: string in format Y-M-D H:M:S.mS
    :return: timedelta difference between expiration_date and current time

    """
    # Convert string to datetime
    expiration_datetime = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S.%f")
    # timedelta object
    difference = expiration_datetime-datetime.now()
    # difference has ms in it so we remove it here for nicer display
    difference = str(difference).split(".")[0]
    return difference
