"""
Subject: CP1404

The purpose of these program is to Ask the user for a number of scores
Generate that many random numbers (scores) between 0 and 100 inclusive
For each of those scores, write the "result" to a file called results.txt.

Student name: Matthew Ballarino
Student number: 13291475
"""

import random

"""Creating a random score"""

def main():
    """Finds out the score and giving a grade"""
    number_of_grades = int(input("How many grades are their: "))
    results_file = open("scores.txt.txt", "w")
    for k in range(number_of_grades):
        score = random.randint(0, 100)
        grade = finding_grade(score)
        print("The score was {0} and grade was {1}".format(score, grade), file=results_file)
        print("The score was {0} and grade was {1}".format(score, grade))
    results_file.close()


def finding_grade(score):
    "Determining the grade of random score"
    if score < 0 or score > 100:
        output = "Invalid score"

    elif score >= 90:
        output = "Excellent"

    elif score >= 50:
        output = "Passable"

    else:
        output = "Bad"

    return output


main()
