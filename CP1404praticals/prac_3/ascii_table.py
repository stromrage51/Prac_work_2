"""
CP1404 3

To create a app that allows students input
a character and see the corresponding ASCII code
and vice versa.

Student name: Matthew Ballarino
Student number: 13291475
"""

LOWEST = 33
HIGHEST = 127
LOW = 10
HIGH = 50


def main():
    """Print and determining asci character from numerical data"""
    number = 0
    try:
        number = get_number(LOWEST, HIGHEST)

    except ValueError:
        number = input("Please a number  {0} - {1}: ".format(LOWEST, HIGHEST))
        number = get_number(LOWEST, HIGHEST)
    print("The character for {0} is {1}".format(number, chr(number)))


def get_number(lower=LOWEST, upper=HIGHEST):
    """" Making sure number is 33 127"""
    number = int(input("Enter a number between {0} and {1}: ".format(LOWEST, HIGHEST)))
    while number < LOWEST or number > HIGHEST:
        number = int(input("Please enter a number between {0} and {1}: ".format(LOWEST, HIGHEST)))
    return number


main()


