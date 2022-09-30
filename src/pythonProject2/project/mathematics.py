import math


def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 1)


def round_up(x):
    rounded = math.ceil(x)
    return rounded


def hypotenuse(x: float, y: float) -> float:
    return math.sqrt(x**2 + y**2)


def count_registrations(registrations: dict) -> int:
    return len(registrations)


def create_attendee_list(registrations: dict) -> list:
    attendees: list = []
    for attendee in registrations:
        attendees.append(str(attendee['first_name'] + str(' ') + attendee['last_name']))
    return attendees
