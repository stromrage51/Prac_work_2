"""
Subject: CP1404

Making our own simple class for a programming language

Student name: Matthew Ballarino
Student number: 13291475
"""

class Programing_Language:
    """Information about programing language"""


    def __init__(self, name, typing, reflection, year):
        """Creating a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    def __str__(self):
     """Return string representation of a ProgrammingLanguage."""
     return "{0}, {1} Typing, Reflection={2}, First appeared in {3}".format(
            self.name, self.typing, self.reflection, self.year)


    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


