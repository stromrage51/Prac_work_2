"""
Subject: CP1404

Writing a Guitar class that allows to store
one guitar with varies fields:

Student name: Matthew Ballarino
Student number: 13291475
"""

CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise conditons"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returning a string representation of a guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Getting the current age of guitar based off the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year









