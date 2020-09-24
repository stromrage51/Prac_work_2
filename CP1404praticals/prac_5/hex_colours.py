"""
Subject: CP1404

Creating a colour code program.

Student name: Matthew Ballarino
Student number: 13291475
"""

# dictorany don't have be constants
COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4", "bisque2": "#eed5b7",
                "black": "#000000"}

user_chosen_colour = input(str("Please pick a colour: "))
while user_chosen_colour != ' ':
    if user_chosen_colour in COLOUR_CODE:
        print("The code for \"{}\" is {}".format(user_chosen_colour,
                                                 COLOUR_CODE.get(user_chosen_colour)))
        user_chosen_colour = input(str("Please pick a colour: "))
    else:
        print("Computer says no")
        user_chosen_colour = input(str("Please pick a colour: "))

print("End program")










