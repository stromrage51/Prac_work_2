"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Student name: Matthew Ballarino
Student number: 13292475
"""

denominator= 0
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
          denominator=int(input("Enter the denominator, no zero:"))


except ValueError:
    print("Numerator and denominator must be valid numbers!")
    # value error is what happens when put in a un numerical error.


except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

fraction = numerator / denominator
print(fraction)

# 1. When will a ValueError ouccur?
# When the numerator and/or denominator has a un-numerical value.

# 2. When will a ZeroDivision Error occur?
# When the neither numerator or denominator has a zero value.

