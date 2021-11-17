"""
Name: Anastasia Sillsbury
lab9.py
"""
import math

from graphics import Circle, GraphWin, Text, Point


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    print(acc)


def to_numbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def write_sum_of_squares():
    input_file = input()
    in_file = open(input_file, "r")
    out_file = open("output.txt", "w+")
    for line in in_file:
        nums = line.split("")
        nums = int(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    out_file.write("Sum of squares = ", acc)


def starter():
    weight = float(input("Weight: "))
    num_wins = int(input("Number of wins: "))
    if 150 <= weight < 160 and num_wins >= 5:
        print("Player is a starter")
    elif weight > 199 or num_wins > 20:
        print("Player is a starter")
    else:
        print("Player is not a starter")


def leap_year(year):
    return(year % 4 == 0 and (year % 100 == 0 or year % 400 == 0))


def circle_overlap():
    win = GraphWin("Circle_stuff", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX()- p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius1)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle = Circle(p3, radius2)
    circle.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    if distance <= radius1 + radius2:
        text1 = Text(Point(200, 350), "The circles overlap")
        text1.draw(win)
    else:
        text2 = Text(Point(200, 350), "The do not circles overlap")
        text2.draw(win)
    win.getMouse()


def main():
    add_ten([5,2,-3])
    square_each([3,5.7,2])
    sum_list([1,2,3])
    to_numbers(["3", "5.7", "2"])
    write_sum_of_squares()
    starter()
    leap_year(2010)
    circle_overlap()


main()
