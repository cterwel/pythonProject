"""
Rename the following variables and function names
"""
CONVERT_FACTOR = 1.8
LOWER_BOUND_FAHRENHEIT = 32


def rename_variables_in_this_function():
    # 1
    var = input("What is your first name? ")

    # 2
    last_name = "Johnson"

    # 3
    movie_title = "Pulp Fiction"

    # 4
    list_of_operating_systems = ["Windows", "Linux", "MacOS"]

    # 5
    list_of_actors = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

    # 6
    list_of_fruits = ["apple", "banana", "kiwi", "orange"]

    # 7
    grades_dict = {"English": 90, "Biology": 80, "Math": 100}


# Rename this function and its variables
def convert_temperature_celsius_to_fahrenheit(x):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (x * CONVERT_FACTOR) + LOWER_BOUND_FAHRENHEIT
    return fahrenheit


# Rename this class
class ElectricVehicle:
    """
    This class initializes an electric vehicle.
    """

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

