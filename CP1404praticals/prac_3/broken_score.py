"""
CP1404/CP5632 - Practical
Broken program to determine score status

broken_score.py - main should ask the user for their score and print the result.
write a new function that takes in the user's score as a parameter and returns the result to be printed.
The function should not print it.

"""

import random
LIST_RANDOM = random.randrange(0, 100, 10)




def main():
            """Creating a random score"""
            score = LIST_RANDOM

            print(grade_statement(score))
            print("The score was {0} and grade was {1}".format(LIST_RANDOM, grade_statement(score)))

def grade_statement(score):
    """Finds out the score and giving a grade"""
    if score < 0:
        return "Invalid score"
    else:
         if score >= 90:
            return "Excellent"
         elif score >= 50:
              return "Passable"
         else:
               return "Bad"


main ()