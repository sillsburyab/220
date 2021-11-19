"""
Name: Anastasia Sillsbury
three_door_game.py

Description: This program creates a random door game.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Point, Text
from button import Button


def main():
    win = GraphWin("The Button Game")
    win.setCoords(0, 0, 20, 20)
    Text(Point(10, 7), "Choose a button").draw(win)

    door_1 = Button(Point(2, 5), Point(5, 2), "Door 1")
    door_1.draw(win)


if __name__ == "__main__":
    main()
