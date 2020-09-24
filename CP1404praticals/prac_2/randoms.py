"""
Testing the import function seeing how no functions work.

Student name: Matthew Ballarino
Student number: 13291475
"""
import random
# import import a file that contains a selection of functions

print(random.randint(5, 20))  # line 1
# the smallest number was 5 in line 1
# the largest number was 20 in line 1
# randit chose a random number between two end points (a and b).

print(random.randrange(3, 10, 2))  # line 2
# the smallest number was 3 in line 2
# the largest number was 9 in line 2
# line 2 couldn't produce four beacuse line 2 goes up in two's starting from 3 to 9 in order
# randrange works simlarly to randit function expect it choose's a number from the start (a) -
# - and goes up in two's until it can not go anymore.
# 3,5,7,9

print(random.uniform(2.5, 5.5))  # line 3
# the smallest number will be 2.5
# the largest number wil be 5.5
# the uniform function produces a random float value between two different end points.

print(random.randint(1, 100))
