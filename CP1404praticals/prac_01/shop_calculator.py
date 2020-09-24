"""
Create a progam that allows a discount for people that
spend more than $100 and adds up the different items.

Name: Matthew Ballarino
Student number: 13291475
"""

number_items = int(input("Please enter item amount: "))

total_price = 0

for k in range(number_items):
    price = float(input("Please enter price of item"))
    total_price += price
if total_price > 100:
    total_price += 0.10
print("Total price of item ", number_items, " items total price is $", total_price, sep='')

print("Total price for {} items is ${:.2f}".format(number_items, total_price))
