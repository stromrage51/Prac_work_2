"""
Subject: Cp1404

Created a program that uses the taxi class.

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_08.taxi import Taxi

def main():
    # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
    current_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40km
    current_taxi.drive(40)
    # the drive is used for stated reasons

    # Print the taxi's details and the current fare
    print(current_taxi)
    print("name = {}\nfuel = {}\ndistance = {}\nfuel_price = ${}\km".format(current_taxi.name,
        current_taxi.fuel, current_taxi.current_fare_distance, current_taxi.price_per_km))

    # Restart the meter (start a new fare)
    current_taxi.start_fare()
    # then drive the car 100km
    current_taxi.drive(100)
    print(current_taxi)






main()

