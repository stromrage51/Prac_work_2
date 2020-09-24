
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








