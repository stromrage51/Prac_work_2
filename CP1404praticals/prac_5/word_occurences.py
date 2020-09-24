"""
Subject: CP1404

Write a program to count the occurrences of words in a string.
The program should ask the user for a string,
then print the counts of how many of each word are in the file.

Student name: Matthew Ballarino
Student number: 13291475
"""

word_count = {}
text = input("please enter a sentence: ")

# this is a collection of words of nice words this is a fun thing it is
words = text.split()
for word in words:
    count = word_count.get(word, 0)
# get function works by
    word_count[word] = count + 1
print(words)
words = list(word_count.keys())
words.sort()


max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))

# this is a collection of words of nice words this is a fun thing it is
# a          : 2 there were two a
# collection : 1
# fun        : 1
# is         : 3  there were 3 is
# it         : 1
# nice       : 1
# of         : 2
# thing      : 1
# this       : 2
# words      : 2



