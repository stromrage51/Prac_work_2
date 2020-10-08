"""
Subject: CP1404

Creating a class to store day, month and year.

Student name: Matthew Ballarino
Student number: 13291475
"""

class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def _str_(self):
        return "day={0}, fuel={1}, year={2}".format(self.day, self.month, self.year)

    def add_day(self, amount):
        """Add amount to the car's fuel."""
        self.day += amount









