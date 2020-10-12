"""
Subject: CP1404

Created a program that can use car class.

Student name: Matthew Ballarino
Student number: 13291475
"""

from random import randint
from CP1404praticals.prac_08.car_2 import Car


class Unreliablecar(Car):
    """ Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        """ Init unreliable car class """
        super().__init__(name, fuel)
        # super is used for inheritance for a patent class
        # or multiple classes without explicitly naming them
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        # generate a random number between 0 and 100,
        # and only drive the car if that number is less than the car's reliability.
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
