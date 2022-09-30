class Person:
    count = 0
    population = []

    def __init__(self, name):
        self.name = name
        Person.count += 1
        Person.population.append(self.name)



class Date:

    def __init__(self, year: int, month: int, day: int):
        try:
            year = int(year)
        except ValueError:
            ...         # To logger

        if not isinstance(month, int):
            raise ValueError

        if not isinstance(day, int):
            raise ValueError

        self.year = year
        self.month = month
        self.day = day
        self.validate_month()
        self.validate_day()

    def validate_month(self, month):
        if month < 0 or month > 12:
            raise ValueError

    def validate_day(self, day):
        if day < 0 or day > 31:
            raise ValueError

    @classmethod
    def from_string(cls, date_string):
        year, month, day = date_string.split('-')
        return cls(int(year), int(month), int(day))

    @classmethod
    def from_dict(cls, date_dict):
        return cls(int(date_dict['year']), int(date_dict['month']), int(date_dict['day']))

    def __repr__(self):
        return f"Date(year={self.year}, month={self.month}, day={self.day})"