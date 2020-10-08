"""
Subject: CP1404

Creating a class to store day, month and year.

Student name: Matthew Ballarino
Student number: 13291475
"""

class Car:
    """Represent a Car object."""

    def __init__(self, day=0, month=0, year=0):
        """Initialise a Car instance.

        name: string name of the car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.day = day
        self.month = month
        self.year = year

    def _str_(self):
        return "day={0}, fuel={1}, year={2}".format(self.day, self.month, self.year)











