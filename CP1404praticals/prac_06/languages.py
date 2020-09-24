"""
Subject: CP1404

Created a  program to inmport the class,
then copy these 3 lines into your new program:

Student name: Matthew Ballarino
Student number: 13291475
"""

from prac_06.programming_language import Programing_Language


def main():
    ruby = Programing_Language("Ruby", "Dynamic", True, 1995)
    python = Programing_Language("Python", "Dynamic", True, 1991)
    visual_basic = Programing_Language("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()






