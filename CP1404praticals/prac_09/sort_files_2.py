"""
Subject: CP1404

Let the user categorise different extensions as the program encounters
these, then move them all into those subdirectories. E.g.
one user might want a category "docs" containing all .doc, .docx, .rtf, .txt...
and an "images" folder containing .jpg, .gif, .png.
another user might want a category "office" containing .doc, .docx, .xls,
but put the .txt files in a "text" category directory.
Tip: Add the extensions to a dictionary and make a list of the categories
as you process the files.

Student name: Matthew Ballarino
Student number: 13291475
"""

import os


def main():
    """Move files into where user wants to store them based on extension."""
    # The following dictionary will allow us to map extensions to the destination folder names
    extension_to_category = {}
    os.chdir("FilesToSort_2")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))

main()