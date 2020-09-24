"""
Subject: CP1404

To create a program that error checks password
length to minimum length.

Student name: Matthew Ballarino
Student number: 13291475
"""

import random
LIST_RANDOM = [4, 5, 6, 8]
MINIMUM_LENGTH = random.choice(LIST_RANDOM)


def main():
    """Getting set up"""
    password = get_password(MINIMUM_LENGTH)
    print_password(password)



def get_password(length):
    """Getting user input and making sure it meets requriments"""
    password_input = input("Enter password that at least has {0} characters:".format(length))
    while len(password_input) < length:
        password_input = input("Please enter the correct amount of characters that least has {0} characters:".format(length))
    return password_input


def print_password(password_input):
    """Printing user input for password in asterisks"""
    print('*' * len(password_input))


main()
