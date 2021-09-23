"""
Name: Anastasia Sillsbury
lab4.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY()-10), (Point(p.getX() + 10, p.getY() + 10)))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to Close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Lab 4", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(p1,p2)
    shape.draw(win)

    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getY() - p1.getY())
    area = length * width
    area_text = Text(Point(50, 150), "The area is: " + str(area))
    area_text.draw(win)
    perimeter = (2 * length) + (2 * width)
    per_text = Text(Point(60, 160), "The perimeter is: " + str(perimeter))
    per_text.draw(win)

    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Lab 4", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    radius = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    shape = Circle(p1, radius)
    shape.draw(win)
    rad_text = Text(Point(100, 350), "The radius is: " + str(radius))
    rad_text.draw(win)
    instructions = Text(Point(100, 300), "Click to exit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    num = eval(input("Number of terms: "))
    acc = 0
    for i in range(num):
        num = 4 * ((-1) ** i)
        denom = 1 + (2 * i)
        frac = num / denom
        acc = acc + frac
    print(acc)
    print(math.pi - acc)

def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
