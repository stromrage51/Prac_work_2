"""
Subject:CP1404

Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Student name:Matthew Ballarino
Student number:1329475
"""

import random
MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_LINES = 6


def main():

    user_number_chosen = int(input("How many numbers to you want to pick: "))
    while user_number_chosen < 0:
        user_number_chosen=int(input("error can't choose a negative number.Please try again"))


    for i in range(user_number_chosen):
        user_number_chosen = []
        for z in range(NUMBER_OF_LINES):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in user_number_chosen:
                number = random.randint(MINIMUM, MAXIMUM)
            user_number_chosen.append(number)
        user_number_chosen.sort()
        print(" ".join("{:2}".format(number) for number in user_number_chosen))




main()

