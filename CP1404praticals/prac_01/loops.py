
"""""
Create a user menu that allow's for 5 different task's
invovled for loops. To grain an better understanding.

Name Matthew Ballarino
Student number:13291475
"""

Guide = """1 for task 1
2 for task 2
etc up to 5"""
print(Guide)

commened = input("Enter task: ")

if commened == '1':
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()
elif commened == '2':
    for v in range(0, 110, 10):
        print(v, end=' ')
    print()
elif commened == '3':
    for g in range(20, 0, -1):
        print(g, end=' ')
    print()

elif commened == '4':
    star_number = int(input("Enter Number of stars: "))
    for z in range(star_number):
        print('*', end=' ')
    print()

elif commened == '5':
    number_star = int(input("Please Enter of stars: "))
    for y in range(1, number_star + 1):
        print('*' * y)
    print()

else:
    print('computer says no')
