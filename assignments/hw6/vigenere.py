"""
Name: Anastasia Sillsbury
vigenere.py

Description: This program encodes a statement using a message and keyword.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Entry, Point, Rectangle, Text


def code(message, keyword):
    message = "".join(message.split(" "))
    message = message.upper()
    keyword = keyword.upper() * 16
    acc = ""
    for i in range(len(message)):
        c = ord(message[i])
        key = ord(keyword[i])
        char = c + key - 91
        if char <= 64:
            new = chr(char + 26)
        else:
            new = chr(char)
        acc = acc + new
    return acc


def main():
    win = GraphWin("Vigenere", 450, 300)

    sentence = Text(Point(60, 35), "Message to Code")
    sentence.draw(win)
    enter_1 = Entry(Point(251, 35), 35)
    enter_1.draw(win)

    key_space = Text(Point(65, 70), "Enter Keyword")
    key_space.draw(win)
    enter_2 = Entry(Point(183, 70), 15)
    enter_2.draw(win)

    box = Rectangle(Point(180, 90), Point(250, 125))
    box.draw(win)
    box_text = Text(Point(215, 107.5), "Encode")
    box_text.draw(win)

    win.getMouse()

    box.undraw()
    box_text.undraw()

    result_message = Text(Point(185, 130), code(enter_1.getText(), enter_2.getText()))
    result_message.draw(win)
    result = Text(Point(200, 115), "Resulting Message")
    result.draw(win)

    close = Text(Point(200, 275), "Click Anywhere to Exit")
    close.draw(win)

    win.getMouse()


if __name__ == "__main__":
    main()
