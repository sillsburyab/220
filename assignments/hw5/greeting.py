"""
Name: Anastasia Sillsbury
greeting.py

Description: This program displays a valentine's day card.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

import time
from graphics import GraphWin, Circle, Line, Text, Point, Polygon

def main():
    win = GraphWin("Valentine's Day Card", 400, 400)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("light yellow")

    def circle_draw(x_1, y_1):
        circle = Circle(Point(x_1, y_1), 1)
        circle.setFill("dark red")
        circle.setOutline("dark red")
        circle.draw(win)

    circle_draw(6, 6)
    circle_draw(4, 6)

    def line_draw(x_1, y_1, x_2, y_2):
        line = Line(Point(x_1, y_1), Point(x_2, y_2))
        line.setFill("light yellow")
        line.setWidth(10)
        line.draw(win)

    line_draw(2.90, 6, 3.50, 5)
    line_draw(7.20, 6, 6.52, 5)

    triangle = Polygon(Point(3, 6), Point(7, 6), Point(5, 3))
    triangle.setFill("dark red")
    triangle.setOutline("dark red")
    triangle.draw(win)

    happy = Text(Point(4.9, 9.5), "Happy")
    happy.setStyle("italic")
    happy.setSize(30)

    valentine = Text(Point(5, 8.5), "Valentine's")
    valentine.setStyle("bold italic")
    valentine.setFill("dark red")
    valentine.setSize(30)

    day = Text(Point(5, 7.5), "Day")
    day.setStyle("italic")
    day.setSize(30)

    for _ in range(1):
        happy.draw(win)
        time.sleep(0.60)
        valentine.draw(win)
        time.sleep(0.60)
        day.draw(win)
        time.sleep(0.6)

    arrow_initial = Line(Point(-1, 2), Point(3, 4))
    arrow_initial.setWidth(3)
    arrow_initial.setFill("sienna")
    arrow_initial.draw(win)
    arrow_head = Polygon(Point(2.8, 4.2), Point(3.1, 3.7), Point(3.5, 4.2))
    arrow_head.setFill("sienna")
    arrow_head.setOutline("sienna")
    arrow_head.draw(win)

    for _ in range(4):
        arrow_head.move(1, 0.6)
        arrow_initial.move(1, 0.6)
        time.sleep(0.8)

    close = Text(Point(5, 0.5), "Click anywhere to close")
    time.sleep(0.35)
    close.draw(win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
