"""
Subject: CP1404

Created a program for SliverServiceTaxis

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ Creating a class for SilverServiceTaxi """
    flagfall = float(4.50)

    # SilverServiceTaxis also have an extra charge for each new fare,
    # so add a flagfall class variable set to $4.50

    def __init__(self, name, fuel, fanciness):
        # Add a new attribute, fanciness, which is a float that scales the price_per_km
        """ Init SilverServiceTaxi """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        # Pass the fanciness value into the constructor and multiply self.price_per_km by it.

    def __str__(self):
        """Return the string or in other words
        print the str value of SliverServiceTaxi"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
        # "{0}, fuel={1}, odo={2}, {3] on current fare" \
        #    ", {4} plus flagfall of ${5}".format(self.name, self.fuel)

    def get_fare(self):
        """ Return the current flare """
        return self.flagfall + super().get_fare()
