"""
Subject: CP1404

Created a car simulator program.

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_06.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nu) update\nq) quit"


def main():
    """Car simulator program, demonstrating use of Car class."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            driving_distance = int(input("How many km's do you wish to drive?: "))
            while driving_distance < 0:
                print("Distance must be >= 0")
                driving_distance = int(input("How many km do you wish to drive?: "))
            distance_driven = car.drive(driving_distance)
            print("This car has driven {0}km".format(distance_driven), end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".")
            print("\n Car's name:{} \n Fuel in car: {} \n odo = {}".format(car.name, car.fuel, car.odometer))
        elif choice == "u":
            print("\n Car's name:{} \n Fuel in car: {} \n odo = {}".format(car.name, car.fuel, car.odometer))
        elif choice == "r":
            added_fuel = int(input("How many units of fuel do you want to add to the car?: "))
            while added_fuel < 0:
                print("Fuel amount must be >= 0")
                added_fuel = int(input("How many units of fuel do you want to add to the car?: "))
            car.add_fuel(added_fuel)
            print("Added {0} units of fuel.".format(added_fuel))
            print("\n Car's name:{} \n Fuel in car: {} \n odo = {}".format(car.name, car.fuel, car.odometer))
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGood bye {0}'s driver.".format(car.name))


main()


















