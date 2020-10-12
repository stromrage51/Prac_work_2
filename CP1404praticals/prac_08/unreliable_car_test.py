"""
Subject: CP1404

Created a program for unreliable_car class

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_08.unreliable_car import Unreliablecar

def main():
    car_1 = Unreliablecar("Car 1", 200, 50)
    car_2 = Unreliablecar("Car 2", 100, 80)

    for i in range(1, 10):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(car_1.name, car_1.drive(i)))
        print("{:12} drove {:2}km".format(car_2.name, car_2.drive(i)))

        # print the final states of the cars
    print(car_1)
    print(car_2)



main()










