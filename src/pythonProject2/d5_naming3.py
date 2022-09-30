"""
This is an exercise to get familiar with Pylint.

You can install pylint with:
pip install pylint

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
"""


def main():
    """Main method."""
    name = input("What is your name?")
    greet(name)


def greet(name):
    """Greet method."""
    print(f"Hello %s, how are you, {name}?")


def make_percentage(number):
    """Make percentages method."""
    percentage = number / 100
    return f"{percentage}%"


if __name__ == "__main__":
    main()
