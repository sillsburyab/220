"""
Name: Anastasia Sillsbury
lab12.py
"""

from random import randint

def find_and_remove(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Anastasia"
    except:
        pass


def read_data(filename):
    file = open(filename, "r")
    data = file.read()
    split = data.split()
    i = 0
    while i < len(split):
        split[i] = int(i)
        i += 1


def is_in_linear(search_val, lst):
    i = 0
    while i < len(lst):
        if search_val == lst[i]:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("Enter number: "))
    while x < 10:
        x = eval(input("Enter number: "))
    return x


def num_digits():
    num = eval(input("Enter number: "))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print(digits)


def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("Enter number: "))
    while not(guess == num) and not(guesses == 7):
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        guesses += 1
        if not(guess == num) and not(guesses == 7):
            guess = eval(input("Enter number: "))
    if guess == num:
        print("You Won! You guessed in", guesses, "guesses!")
    else:
        print("You lost :(")


def main():
    find_and_remove([1, 2, 3, 4], 3)
    read_data("data.txt")
    is_in_linear(3, [1, 2, 3, 4])
    good_input()
    num_digits()
    hi_lo_game()


main()
