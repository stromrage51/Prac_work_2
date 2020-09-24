"""
Subject: CP1404
Learning how to open files, writing in them and reading them.

Student name: Matthew Ballarino
Student number: 13291475
"""

# Part 1
user_name = input("Please enter a name: ")
out_file = open("user_name.txt", "w")
print(user_name, file=out_file)
out_file.close()

# Part 2
with open("user_name.txt","r") as out_file:
    # the with function opens and close file without specially telling
    user_name = out_file. read(). strip()
# read function allows to read the file in text.
# if you put read(5) it will read the first 5 strings.
# strip function removes all spaces from a string leading and tailing.
# if you do string = " hello world   " with strip it becomes "hello world".
    out_file.close()
print("Hello {} how are you today".format(user_name))

# Part 3
in_file_1 = open("numbers.txt.txt", "r")
number_1 = int(in_file_1.readline())
number_2 = int(in_file_1.readline())
in_file_1.close()

total = 0
in_file_1 = open("numbers.txt.txt", "r")
for line in in_file_1:
    total += 1
in_file_1.close()

print(number_1 + number_2)
print(total)