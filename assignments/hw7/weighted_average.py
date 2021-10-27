"""
Name: Anastasia Sillsbury
weighted_average.py

Problem: creates a file with the weighted averages of each student.

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    file_in = open(in_file_name, "r")
    file_out = open(out_file_name, "w+")
    file_in = file_in.readlines()
    acc2 = 0
    for line in file_in:
        file_in = line.split(": ")
        name = file_in[0]
        numbers = file_in[1].split(" ")
        numbers = [int(i) for i in numbers]
        grades = numbers[1::2]
        grades[-1] = str(grades[-1]).strip()
        grades = [int(i) for i in grades]
        weights = numbers[0::2]
        weights = [int(i) for i in weights]
        student_grades = [a * b for a, b in zip(grades, weights)]
        acc = 0
        sum_weights = sum(weights)
        if sum_weights > 100:
            file_out.write(name + "'s average: Error: The weights are more than 100." + "\n")
        elif sum_weights < 100:
            file_out.write(name + "'s average: Error: The weights are less than 100." + "\n")
        else:
            for number in student_grades:
                acc = acc + number
            student_average = acc / 100
            file_out.write(name + "'s average: " + str(round(student_average, 1)) + "\n")
            acc2 = acc2 + student_average
    class_average = acc2 / len(file_in)
    file_out.write("Class average: " + str(round(class_average, 1)))


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
