"""
Name: Anastasia Sillsbury
interest.py

Description: This program calculates monthly interest charge.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""


def main():
    interest_rate = eval(input("Enter the annual interest rate:"))
    cycle = eval(input("Enter the number of days in the billing cycle:"))
    net = eval(input("Enter the previous (net) balance:"))
    payment = eval(input("Enter the payment amount:"))
    day_payment = eval(input("Enter the day of the billing cycle in which the payment was made:"))
    balance = net * cycle
    received = payment * (cycle - day_payment)
    difference = balance - received
    daily_bal = difference / cycle
    monthly = (interest_rate / 12) / 100
    interest_charge = daily_bal * monthly
    interest_charge = str(round(interest_charge, 2))
    print(interest_charge)

if __name__ == '__main__':
    main()
