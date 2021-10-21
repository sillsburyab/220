"""
Name: Anastasia Sillsbury
lab8.py
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    file_in = open(in_file_name, "r")
    file_out = open(out_file_name, "w+")
    i = 1
    for line in file_in:
        words = line.split()
        for word in words:
            file_out.write(str(i) + " " + word + "\n")
            i += 1


def hourly_wages(in_file_name, out_file_name):
    file_in = open(in_file_name, "r")
    file_out = open(out_file_name, "w+")
    for line in file_in:
        parts = line.split()
        wage = float(parts[2])
        new_wage = wage + 1.65
        full_wage = new_wage * int(parts[3])
        file_out.write(parts[0] + " " + parts[1] + " $" + str(full_wage) + "\n")



def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc = acc + (pos * int(isbn[i]))
    return acc


def send_message(file, friend):
    file_in = open(file, "r")
    file_out = open(friend, "w+")
    for line in file_in:
        file_out.write(line)


def send_safe_message(file, friend, key):
    file_in = open(file, "r")
    file_out = open(friend, "w+")
    for line in file_in:
        file_out.write(str(encode(line, key)))


def send_uncrackable_message(file, friend, pad):
    file_in = open(file, "r")
    file_out = open(friend, "w")
    file_pad = open(pad, "r")
    key = file_pad.read()
    for line in file_in:
        file_out.write(str(encode_better(line, key)))



def main():
    # number_words("walrus.txt", "walrus_out.txt")
    # hourly_wages("hourly_wages.txt", "new_wages.txt")
    # print(calc_check_sum("0072946520"))
    # send_message("message.txt", "jade.txt")
    # send_safe_message("secret_message.txt", "caralyn.txt", 5)
    send_uncrackable_message("safest_message.txt", "jordan.txt", "pad.txt")

main()
