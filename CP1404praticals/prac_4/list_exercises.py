"""
Subject: CP1404

Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.

Student name: Matthew Ballarino
Student number: 13291475
"""
# 1 basic list operations


numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is:", numbers[0])
print("The last number is:", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of numbers is:", sum(numbers) / len(numbers))
# the formula for finding the average

# 2 Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Please enter a username:")

if user_input in usernames:
    print("Access granted")
else:
    print("Access not granted")
