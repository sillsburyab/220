"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import math

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    x3 = p3.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    y3 = p3.getY()
    tri = Polygon(p1, p2, p3)
    tri.draw(win)
    # and display its area in the graphics window.
    dx = x2 - x1
    dy = y2 - y1
    dx2 = x3 -x1
    dy2 = y3 - y1
    dx3 = x3 - x2
    dy3 = y3 - y2
    lengthAB = math.sqrt((dx ** 2) + (dy ** 2))
    lengthAC = math.sqrt((dx2 ** 2) + (dy2 ** 2))
    lengthBC = math.sqrt((dx3 ** 2) + (dy3 ** 2))
    perimeter = lengthBC + lengthAB + lengthAC
    areaS = perimeter / 2
    area = math.sqrt(areaS * (areaS - lengthAB) * (areaS - lengthAC) * (areaS - lengthBC))
    point = Point(150, 10)
    point2 = Point(300,10)
    area_text = Text(point, ("Area = ", round(area, 2)))
    perimeter_text = Text(point2, ("Perimeter =", round(perimeter, 2)))
    area_text.draw(win)
    perimeter_text.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    red_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)

    red_box.draw(win)
    blue_box.draw(win)
    green_box.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = "Hello world"
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0] + s[-1])
    print(s[:3] * 10)
    for char in range(len(s)):
        print(s[char])
    print(len(s))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = (values[1] + values[3])
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2],values[3], values[0]]
    print(x)
    x = [values[2],values[0], float(values[-1])]
    print(x)
    x = values[0] + values[2] + float(values[-1])
    print(x)
    x = len(values)
    print(x)

def another_sequence():
    terms = eval(input("Number of terms: "))
    acc = 0
    for i in range(terms):
        y = 2 + (2 * (i % 3))
        print(y, end = " ")
        acc = acc + y
    print("")
    print("sum =", acc)


def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_sequence()


main()
