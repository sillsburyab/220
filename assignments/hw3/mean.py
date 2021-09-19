"""
Name: Anastasia Sillsbury
mean.py

Description: This program calculates rms average, harmonic mean, and geometric mean.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""
# 1. The program will take user input and output 3 types of averages.
# 2. The inputs will be numbers and the amount of numbers
# 3. Get input on how many values, and what the values are. Use the inputs
#    to calculate root mean square, the harmonic
#    mean, and the geometric mean, using a for loop.

import math

def main():
    num = eval(input("Enter the values to be entered:"))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(num):
        value = eval(input("Enter value " + str(i + 1) + ":"))
        acc = acc + ((value ** 2))/num
        rms_average = math.sqrt(acc)
        acc2 = acc2 + (1/value)
        harmonic_mean = num / acc2
        acc3 = acc3 * value
        geometric_mean = (acc3 ** (1/num))

    print(round(rms_average, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))
if __name__ == '__main__':
    main()
