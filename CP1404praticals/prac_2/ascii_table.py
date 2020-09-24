"""
CP1404

To create a app that allows students input
a character and see the corresponding ASCII code
and vice versa.

Student name: Matthew Ballarino
Student number: 13291475
"""

user_input = input("Enter a character: ")
LOWEST = 33
HIGHEST = 127
print("The ASCII code for {0} is {1}". format(user_input, ord(user_input)))
# to convert character into ascii code

number = int(input("Enter a number between {0} and {1}: ".format(LOWEST, HIGHEST)))
while number < LOWEST or number > HIGHEST:
    number = int(input("Please enter a number between {0} and {1}: ".format(LOWEST, HIGHEST)))
print("The character for {0} is {1}".format(number, chr(number)))

# ASCII table (single column)
for value in range(LOWEST, HIGHEST + 1):
    print("{:3} {:>4}".format(value, chr(value)))

# Asking user for column's between 2 and 10

MIN_COLUMNS = 2
MAX_COLUMNS = 10

user_columns = int(input("Enter amount of columns between {0} and {1}: ".format(MIN_COLUMNS, MAX_COLUMNS)))
while user_columns < MIN_COLUMNS or user_columns > MAX_COLUMNS:
      user_columns = int(input("Please enter amount of columns between {0} and {1}: ".format(MIN_COLUMNS, MAX_COLUMNS)))
number_of_values = HIGHEST - LOWEST + 1
rows = number_of_values // user_columns
# // is floor division

for rows in range(rows +1):
    start_value = LOWEST + rows
    value = start_value
# print all columns expect last one.
    for user_columns in range(user_columns - 1):
        value_print = value + (user_columns * rows)
        print("{:6} {:>}".format(value_print, chr(value_print), end = ''))
        value += 1
# makes sure that last column exits.
    value_print = value + ((user_columns + 1) * rows)
    if value_print <= HIGHEST:
        print("{:6} {:>}".format(value_print, chr(value_print), end=''))
    print()



