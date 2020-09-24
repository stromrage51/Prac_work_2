"""
Subject: CP1404

So to test that the get_age() method works,
you could test that the above example guitar
does indeed output 98 as expected.

Student name: Matthew Ballarino
Student number: 13291475
"""

from prac_06.guitar import Guitar


"""Tests for Guitar class."""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other = Guitar("Another Guitar", 2013, 1512.9)

print("{} get_age() - Expected {}. "
      "Got {}".format(guitar.name, 98, guitar.get_age()))

print("{} get_age() - Expected {}. "
      "Got {}".format(other.name, 7, other.get_age()))


print("{} is_vintage() - Expected {}. "
      "Got {}".format(guitar.name, True, guitar.is_vintage()))

print("{} is_vintage() - Expected {}. "
      "Got {}".format(other.name, False, other.is_vintage()))









