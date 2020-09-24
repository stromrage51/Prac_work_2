"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task

Student name: Matthew Ballarino
Student number: 13291475
"""

finished = False
result = 0
while not finished:
    try:
         result = int(input("Enter a number: "))
         finished= True
         # the true function ends the loop
    except:
            print("Please enter a valid integer.")
            result = int(input("Please enter a valid number: "))
print("Valid result is:", result)