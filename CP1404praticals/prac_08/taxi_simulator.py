"""
Subject: CP1404

Created a taxi simulator

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_08.taxi import Taxi
from CP1404praticals.prac_08.SliverServiceTaxis import SilverServiceTaxi

Menu = "(Q)uit\n(C)hoose taxi\n(D)rive"

def main():
    """Creating a taxi simulator"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(Menu)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi_driving = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi_driving.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi_driving.drive(distance_to_drive)
            trip_cost = current_taxi_driving.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi_driving.name,
                                                         trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(Menu)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))



main()