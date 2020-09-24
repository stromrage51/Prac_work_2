"""
Subject: CP1404

Gaining an better understanding on pycharm.

Student name: Matthew Ballarino
Student number: 13291475
"""
numbers = [3, 1, 4, 1, 5, 9, 2]



"""
numbers [0] = 3
numbers[-1] = 2
numbers[3]  = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = 1     
example if numbers is [2,4} then it is 4,1
5 in numbers = true there is a 5
7 in numbers = flase there is no 7 in numbers
"3" in numbers = flase
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

"""
numbers_2 = numbers
numbers_3 = numbers_2

"Problem 1"
" Change the first element of numbers to "
"ten"" (the string, not the number 10)"
numbers_4 = numbers_3
numbers_4[0] = "ten"
z = numbers_4
print(z)

"Problem 2"
"Change the last element of numbers to 1"
numbers_5 = numbers_3
numbers_5[-1] = 1
y = numbers_5
print(y)

"Problem 3"
# Get all the elements from numbers
# except the first two (slice)
numbers_6 = numbers_3
x = numbers_6[2:]
print(x)

"Problem 4"
# Check if 9 is an element of numbers
p = 9 in numbers
print(p)

