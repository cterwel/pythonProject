from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"Person name is {self.name} with height {self.height}"

    def __repr__(self):
        return f"Person(name={self.name}, height={self.height})"

    def __gt__(self, other):
        return self.height > other.height



