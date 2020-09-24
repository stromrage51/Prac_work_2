"""
The create to calculator that can calcaulate the electrity bill.

Student name: Matthew Ballarino
Student number: 13291475
"""
commened= input("please enter task 1 or 2: ")
if commened == "1":
    Price_kwh = float(input("PLease enter cost of electricity per hour in cents: "))
    Daily_kwH = float(input("Please enter daily usage of using  electricty: "))
    Billing_days = float(input("Please enter number of billing days: "))
    Bill_cost = (Price_kwh / 100) * Daily_kwH * Billing_days
    print("Bill estimated to be: $ {:.2f} ".format(Bill_cost))

elif commened == "2":
    TARIFF = input("Please choose tariff 11 or tariff 31: ")
    if TARIFF == "11":
       TARIFF = 0.244618
       Daily_kwH = float(input("Please enter daily usage of using  electricty: "))
       Billing_days = float(input("Please enter number of billing days: "))
       Bill_cost = TARIFF * Daily_kwH * Billing_days
       print("Bill estimated to be: $ {:.2f} ".format(Bill_cost))
    elif TARIFF == "31":
          TARIFF = 0.136928
          Daily_kwH = float(input("Please enter daily usage of using  electricty: "))
          Billing_days = float(input("Please enter number of billing days: "))
          Bill_cost = TARIFF * Daily_kwH * Billing_days
          print("Bill estimated to be: $ {:.2f} ".format(Bill_cost))
    else:
           print("Error does not compute.")
else:
     commened = input("please try again and enter task 1 or 2: ")