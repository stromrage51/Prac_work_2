"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Name: Matthew Ballarino

Student number:13291475
"""
sales = float(input("Please enter sales: $"))
while sales >= 0:
    if sales <= 1000:
      bouns= sales*0.10
      print("Bouns sales earnings: $ {:.2f}  ".format(bouns))
      sales = float(input("Please enter sales again: $"))
    else:
      bouns = sales*0.15
      print("Bouns sales earnings: $ {:.2f} ".format(bouns))
      sales = float(input("Please enter sales again: $"))
else:
     print("error negative sales need to see offical")




