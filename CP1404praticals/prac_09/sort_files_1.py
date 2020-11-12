"""
Subject: CP1404

Use os.mkdir() to create a directory with for each new extension that your program finds and use shutil.move() to move files into these new directories.
E.g. move all files ending in ".txt" to a directory you create called "txt", and all ".doc" files to a "doc" directory.

Do not try and create directories you've already made.

Student name: Matthew Ballarino
Student number: 13291475
"""

import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        # We could maintain a list/set of extensions we've made folders for (LBYL)
        # Or we could just "try" making folders again and ignore errors (EAFP)
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()









