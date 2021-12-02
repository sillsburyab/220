""""
Name: Anastasia Sillsbury
sales_force.py

Problem: creates SalesForce class.

got help from hunter :)

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    """
    Class that creates a sales force
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        data = open(file_name, "r")
        data = data.readlines()
        for line in data:
            # split the current line at ", "
            line = line.split(", ")
            # index 0 is id
            # index 1 is name
            # create a salesperson object using id, name
            person = SalesPerson(line[0], line[1])
            # index 2 is a list of sales separated by spaces
            # split sales
            sales = line[2].split()
            # loop through sales and add them to the current salesperson
            for sale in sales:
                person.enter_sale(float(sale))
            # once done, append the current salesperson to self.sales_people
            self.sales_people.append(person)

    def quota_report(self, quota):
        people = []
        for person in self.sales_people:
            people.append([person.get_id(), person.get_name(),
                           person.total_sales(), person.met_quota(quota)])
        return people

    def top_seller(self):
        top = []
        for i in range(len(self.sales_people)):
            highest = self.sales_people[i]
            pos = i
            for j in range(i + 1, len(self.sales_people)):
                if self.sales_people[j].get_sales() > highest:
                    highest = self.sales_people[j]
                    pos = j
        top.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() == top[0].total_sales():
                top.append(self.sales_people[pos])

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
