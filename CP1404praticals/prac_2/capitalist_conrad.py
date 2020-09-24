"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100, or falls below $1, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)

Student name: Matthew Ballarino
Student number: 13291475
"""
import random

OUTPUT_FILE= 'stock_output.txt'
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
day = 0  # First day
# Constants are variables that can't be changed
price = INITIAL_PRICE
outfile= open(OUTPUT_FILE, 'w')
# This function opens a file and writes in it because of the w

print("Staring price: ${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    day +=1  # Allows the day to be updated and changed


    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        # For one it increase's the price
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # print("On day {1} price is: ${0:.2f}".format(price,day))
    print("On day {1} price is: ${0:.2f}".format(price, day), file=outfile)

outfile.close()
# closes the file