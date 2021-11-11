"""
Name: Anastasia Sillsbury
lab11.py
I was not able to finish it within the time in lab :)
"""

import random


def word():
    # Read in file of words
    file = open("wordlist.txt", "r")
    words = file.readlines()
    return words


def random_choice(words):
    random_word = random.choice(words)
    return random_word.strip()


def guessed(letter, random_word, past):
    acc = ""
    for char in random_word:
        acc = acc + " " + char
    blanks = []
    for i in range(len(random_word)):
        if letter == random_word[i]:
            blanks.append(letter)
        elif random_word[i] in past:
            blanks.append(random_word[i])
        else:
            blanks.append("_")
    print(blanks)


# def used():
#     # loop


def play_game():
    words = word()
    random_word = random_choice(words)
    for i in range(len(random_word)):
        letter = input("\nEnter a letter: \n")
        guessed(letter, random_word)


def main():
    play_game()


main()
