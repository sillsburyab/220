"""
Name: Anastasia Sillsbury
lab6.py
"""


def name_reverse():
    name = input("Enter name (First, Last): ")
    name = name.split()
    print(name[1] + ", " + name[0])

def company_name():
    company = input("Enter three part internet domain: ")
    company = company.split(".")
    print(company[1])

def initials():
    name = eval(input("How many names: "))
    for i in range(name):
        first = input("Enter the first name of student: ")
        last = input("Enter " + first + "'s last name: ")
        print(first[0][0] + last[0][0])

def names():
    x = input("Enter a list of names, separated by commas: ")
    x = x.split(",")
    for name in x:
        parts = name.split()
        print(parts[0][0] + parts[1][0], end=" ")
        print()

def thirds():
    sentences = eval(input("Enter number of sentences: "))
    for x in range(sentences):
        s = input("Enter sentence: ")
        print(s[2::3])

def word_average():
    sentence = input("Write a sentence: ")
    acc = 0
    sentence = sentence.split()
    for word in sentence:
        acc = acc + len(word)
    print(acc/len(sentence))

def pig_latin():
    sentence = input("Enter sentence: ")
    sentence = sentence.split()
    for word in sentence:
        print(word[1:] + word[0] + "ay", end = " ")




def main():
   name_reverse()
   company_name()
   initials()
   names()
   thirds()
   word_average()
   pig_latin()



main()
