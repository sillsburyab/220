"""

Name: Anastasia Sillsbury
lab2.py

"""

import math

def sum_of_threes():
    upper = eval(input("Upper bound:"))
    acc = 0
    for x in range(0, upper + 1, 3):
        acc = (acc + x)
    print(acc)

sum_of_threes()

def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
          print(h * l, end=" ")
        print()

multiplication_table()

def triangle_area():
    a = eval(input("What is a:"))
    b = eval(input("What is b:"))
    c = eval(input("What is c:"))
    s = (a + b + c)/2
    x = s * (s-a) * (s-b) * (s-c)
    area = math.sqrt(x)
    print(area)
triangle_area()

def sumSquares():
    start = eval(input("Starting number:"))
    end = eval(input("Ending number:"))
    a = 0
    for i in range(start, end + 1):
        a = a + (i ** 2)
    print(a)

sumSquares()

def power():
    base = eval(input("What is the base:"))
    exponent = eval(input("What is the exponent:"))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print(base, "^", exponent, "=", acc)

power()
