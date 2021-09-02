"""
Name: Anastasia Sillsbury
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

calc_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

calc_volume()

def shooting_percentage():
    shots_made = eval(input("Enter the shots made: "))
    total_shots = eval(input("Enter the total shots: "))
    shot_percent = ((shots_made / total_shots) * 100)
    print("Shooting Percentage =", shot_percent, "%")

shooting_percentage()

def coffee():
    coffee_cost = 10.50
    shipping = 0.86
    overhead = 1.50
    lbs = eval(input("How many pounds: "))
    total_cost = (overhead + (lbs * (coffee_cost + shipping)))
    print("Total Cost: $", total_cost)

coffee()

def kilometers_to_miles():
    kilo = eval(input("How many kilometers? "))
    kilo_convert = 1.61
    conversion = kilo / kilo_convert
    print("You traveled:", conversion, "miles!")

kilometers_to_miles()


