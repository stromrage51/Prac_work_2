"""
Subject: CP1404

Testing the class for Date.py file

Student name: Matthew Ballarino
Student number: 13291475
"""

from CP1404praticals.prac_06.Date import Date


def main():
    """Demo test code to show how to use car class."""
    my_date = Date(180, 0, 5)
    print("Month =", my_date.month)

    print("year =", my_date.year)

    print(my_date)

    print("{} {}, {}".format(my_date.day, my_date.month, my_date.year))
    print("{self.day} {self.month}, {self.year}".format(self=my_date))

    test_days = Date(100, 5, 6)
    test_days.add_day(20)
    print(test_days.month)
    print(test_days.day)
    print("{} days {} month, {} year".format(test_days.day, test_days.month, test_days.year))

main()











