"""
Name: Anastasia Sillsbury
traffic.py

Description: This program uses a loop to analyze traffic patterns.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed? "))
    acc = 0
    tot = 0
    for i in range(roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        for car in range(days):
            cars = eval(input("How many cars traveled on day " + str(car + 1) + "? "))
            tot = tot + cars
            acc = acc + cars
            average = acc / days
            average = round(average, 2)
        acc = 0
        print("Road " + str(i + 1) + " average vehicles per day: " + str(average))
    car_avg = tot / roads
    print("Total numbers of vehicles traveled on all roads:", tot)
    print("Average number of vehicles per road:", round(car_avg, 2))


if __name__ == '__main__':
    main()
