"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

import random


def main():
    """Converting file fahrenheit temperatures into celsius."""
    input_file = open("temps_input.txt.txt", "r")
    output_file = open("temps_output.txt.txt", "w")
    for converting in input_file:
        work = converting_fahrenheit_to_celsius(float(converting))
        print(work, file=output_file)
    input_file.close()
    output_file.close()


def new_input_file(write):
    """Write the number of temperatures to file"""
    temperatures_file = open("temps_input.txt.txt", "w")
    for ze in range(write):
        temp = random.uniform(-200, 200)
        print(temp, file=temperatures_file)
    temperatures_file.close()


def converting_fahrenheit_to_celsius(fahrenheit):
    """Converting fahrenheit to celsius"""
    return (fahrenheit - 32) * 5 / 9


def converting_celsius_to_fahrenheit(celsius):
    """Converting celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


main()
