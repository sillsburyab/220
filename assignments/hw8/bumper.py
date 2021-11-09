""""
Name: Anastasia Sillsbury
bumper.py

Problem: creates a window that displays two balls bouncing around.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""
import math
from random import randint
from time import sleep
from graphics import GraphWin, Point, Circle, color_rgb


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball, ball2):
    center1 = ball.getCenter()
    center2 = ball2.getCenter()
    center1_x = center1.getX()
    center1_y = center1.getY()
    center2_x = center2.getX()
    center2_y = center2.getY()
    center1_radius = ball.getRadius()
    center2_radius = ball2.getRadius()
    distance = math.sqrt(((center2_x - center1_x) ** 2) + ((center2_y - center1_y) ** 2))
    if distance <= center1_radius + center2_radius:
        var = bool(True)
    else:
        var = bool(False)
    return var


def hit_vertical(ball, win):
    center = ball.getCenter()
    center_x = center.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    if center_x <= radius or center_x >= width - radius:
        var = bool(True)
    else:
        var = bool(False)
    return var


def hit_horizontal(ball, win):
    center = ball.getCenter()
    center_y = center.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    if center_y <= radius or center_y >= height - radius:
        var = bool(True)
    else:
        var = bool(False)
    return var


def get_random_color(ball):
    r_1 = randint(0, 255)
    g_1 = randint(0, 255)
    b_1 = randint(0, 255)
    ball.setFill(color_rgb(r_1, g_1, b_1))


def main():
    win = GraphWin("Bumper Circles", 600, 600)
    height = win.getHeight()
    width = win.getWidth()
    circle1 = Circle(Point(70, height/2), 40)
    circle2 = Circle(Point(width - 70, height/2), 40)
    get_random_color(circle1)
    get_random_color(circle2)
    circle1.draw(win)
    circle2.draw(win)
    for _ in range(100):
        sleep(0.35)
        circle1.move(get_random(10), get_random(10))
        circle2.move(get_random(10), get_random(10))
        if did_collide(circle1, circle2):
            center_1 = circle1.getCenter()
            circle1.move(center_1.getX() * -1, center_1.getY() * -1)
            center_2 = circle2.getCenter()
            circle2.move(center_2.getX() * -1, center_2.getY() * -1)
        if hit_vertical(circle1, win):
            center_1 = circle1.getCenter()
            circle1.move(center_1.getX() * -1, center_1.getY())
        if hit_vertical(circle2, win):
            center_2 = circle2.getCenter()
            circle2.move(center_2.getX() * -1, center_2.getY())
        if hit_horizontal(circle1, win):
            h_center_1 = circle1.getCenter()
            circle1.move(h_center_1.getX(), h_center_1.getY() * -1)
        if hit_horizontal(circle2, win):
            h_center_2 = circle2.getCenter()
            circle2.move(h_center_2.getX(), h_center_2.getY() * -1)

    win.getMouse()


if __name__ == "__main__":
    main()
