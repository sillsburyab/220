""""
Name: Anastasia Sillsbury
button.py

Problem: creates button class.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""


from graphics import *


class Button:
    def __init__(self, point_1, point_2, label):
        self.button = Rectangle(point_1, point_2)
        self.label = Text(Point((point_2.getX() - point_1.getX()) / 2, (point_2.getY() - point_1.getY())), label)

    def get_label(self):
        return self.label()

    def draw(self, win):
        return self.draw(win)

    def undraw(self):
        return self.undraw()

    def is_clicked(self, point):
        return self.is_clicked(point)

    def color_button(self, color):
        return self.color_button(color)

    def set_label(self, label):
        return self.set_label(label)
