"""
Name: Anastasia Sillsbury
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math

def cash_conversion():
    dollar = eval(input("Enter an integer: "))
    print("$" + '{:.2f}'.format(dollar))

def encode():
    sentence = input("Enter message to be encoded: ")
    key = eval(input("Enter integer key value: "))
    acc = ""
    for c in sentence:
        i = ord(c)
        k = key + i
        c = chr(k)
        acc = acc + c
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

def sum_n(n):
    for i in range(n):
        sum = (n *(n + 1))/ 2
    return sum

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + (i ** 3)
    return acc

def encode_better():
    sentence = input("Enter sentence: ")
    k = input("Enter key: ")
    acc = ""
    for i in range(len(sentence)):
        c = sentence[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        c = chr(c + key)
        acc = acc + c
    print(acc)


def main():
    cash_conversion()
    encode()
    print(round(sphere_area(2), 3))
    print(round(sphere_volume(2), 2))
    print(sum_n(5))
    print(sum_n_cubes(5))
    encode_better()


main()
