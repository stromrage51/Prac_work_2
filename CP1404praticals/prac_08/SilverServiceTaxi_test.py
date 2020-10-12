"""
Subject: CP1404

Testing SilverServiceTaxi class

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_08.SliverServiceTaxis import SilverServiceTaxi

def main():

    taxi = SilverServiceTaxi("SilverServiceTaxi_1", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()


