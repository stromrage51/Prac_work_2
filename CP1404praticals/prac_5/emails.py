"""
Subject: CP1404

Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to get the name from the email as in the example below.

Student name: Matthew Ballarino
Student number: 13291475
"""

email_to_name = {}
print("Enter a email or set of emails then please enter when finished")
email = input("Email: ")
while email != "":
    prefix = email.split('@')[0]
    print(prefix)
    parts = prefix.split('.')
    print(parts)
    name = " ".join(parts).title()
    print(name)
    confirmation = input("Is your name {}? (Y/n) ".format(name))
    if confirmation.upper() != "Y" and confirmation != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

    for email, name in email_to_name.items():
     print("{} ({})".format(name, email))
