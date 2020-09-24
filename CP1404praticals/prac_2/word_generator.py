"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.

Student name: Matthew Ballarino
Student number: 13291475
"""
import random

user_input = int(input("How many characters is in the password?: "))


VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARCTERS = '%$#@*&'
CAPTIAL_CONSONANTS = "BCDFGHJKLMNPRQRSTVWXYZ"
CAPTIAL_VOWELS = "AEIOU"

guessing = "cvdrh"
word_format = "".join(random.choice(guessing)for i in range(user_input))

print(word_format)

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "d":
         word += random.choice(SPECIAL_CHARCTERS)
    elif kind == 'r':
         word += random.choice(CAPTIAL_CONSONANTS)
    elif kind == 'h':
        word += random.choice(CAPTIAL_VOWELS)
    else:
        word += random.choice(VOWELS)

print("The password is {0} with a string length of {1}".format(word, user_input))