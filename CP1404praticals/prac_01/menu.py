"""
This is for creating a ali menu system

Name: Matthew Ballarino
Student number: 13291475
"""


Menu= " (H)ello\n(G)oodybye\n(E)nd\n(W)eather "
Name_user= input('Please enter name: ')
print(Menu)
user_choice=input(("Enter commoned")).upper()
while user_choice != "E":
    if user_choice == "H":
        print("Hello",Name_user)
    elif user_choice == "G":
        print("Goodbye", Name_user)
    elif user_choice == "W":
        print("Isn't the weather nice today", Name_user)
    else:
        print("Computer says no")
    user_choice = input(("Enter commoned")).upper()
    print(Menu)
print("Ending program")