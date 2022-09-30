"""
Add 'docstrings' to the following functions and classes.
Make sure to follow the Python conventions.
"""


# 1
def square(num):
    """Returns the square of a number."""
    return num * num


# 2
def count_vowels(word):
    """Return the total number of vowels"""
    number_of_vowels = 0
    for char in word.lower():
        if char in "aeiou":
            number_of_vowels += 1
    return number_of_vowels


# 3
class Dog:
    """A class to represent a dog."""

    def __init__(self, name):
        self.name = name

    def bark(self):
        """Method prints the instance barking."""
        print(f"{self.name} says whoof!")
