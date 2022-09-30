import math
from datetime import datetime


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def age(self):
        age = datetime.today() - datetime.strptime(self.birth_date, '%Y-%m-%d')
        return math.floor(self.age.days / 365.25)

    def say_hello(self):
        """Person says hello"""
        print(f"{self.name} says hello")


class Student(Person):
    def learn(self, to_learn):
        print(f"{self.name} is learning {to_learn}")

