"""
Name: Anastasia Sillsbury
lab3.py
"""

def average():
    number = eval(input("How many assignments: "))
    acc = 0
    for i in range(1, number + 1):
        grade = eval(input("Enter your grade on HW " + str(i)))
        acc = acc + grade
    print("The average is:", acc / number)
average()

def tip_jar():
    acc = 0
    for i in range(0, 5):
        tip = eval(input("Amount of donation:"))
        acc = acc + tip
    print("The total is: $", acc)
tip_jar()

def newton():
    x = eval(input("What is the number? "))
    improve = eval(input("How many times to improve? "))
    approx = x/2
    for i in range(improve):
        approx = (approx + (x/approx)) / 2
    print("The number used was ", x, "The approximation is:", approx)
newton()

def sequence():
    num = eval(input("How many numbers in sequence? "))
    for i in range(1, num + 1):
        y = 1 + (i//2 * 2)
        print(y)

sequence()

def pi():
    n = eval(input("What is n? "))
    acc = 1
    for i in range(n):
        numer = 2 + (i//2 * 2)
        denom = 1 + ((1 + i)//2 * 2)
        frac = numer / denom
        acc = acc * frac
    print(acc * 2)

pi()