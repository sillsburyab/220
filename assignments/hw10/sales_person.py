""""
Name: Anastasia Sillsbury
sales_person.py

Problem: creates person class.

Got help from hunter :)

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    Class that creates a sales person class
    """

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(0, len(self.sales)):
            total += self.sales[i]
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return str(self.employee_id) + "-" + self.name + ": " + str(self.total_sales())
