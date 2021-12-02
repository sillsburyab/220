"""
Name: Anastasia Sillsbury
lab13.py
"""

import random


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while mid != search_val and len(values) != 1:
        if mid < search_val:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values) / 2
    if search_val == mid:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def get_area(rect):
    return random(1, 100)


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]
    print(areas)


def trade_alert(filename):
    in_file = open(filename, "r")
    data = in_file.read().split()
    seconds = 0
    data = [int(i) for i in data]
    for num in data:
        seconds += 1
        if 500 < num < 800:
            print(seconds, "alert!")
        if num > 800:
            print(seconds, "Warning!!")


def main():
    is_in_binary(2, [1,3,4,5])
    selection_sort([1, 4, 2, 3, 5])
    rect_sort()
    trade_alert("trades.txt")



main()
