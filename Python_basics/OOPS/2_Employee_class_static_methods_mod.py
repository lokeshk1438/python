# creating a class with empty body and assigning values after creating the objects

class Employee:
    # class variables
    raise_amt = 1.04
    num_emps = 0 # calculate the total num of employees

    def __init__(self, fname, lname, salary):
        # instance variable
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@gmail.com'

        Employee.num_emps += 1 # need to give Employee instead of self as we need to have a constant value at a class level

    def getDetails(self):
        return "{0} {1}".format(self.fname, self.lname)

    def applyRates(self):
        self.salary = int(self.salary * self.raise_amt)

    # converting instance method to a class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        else:
            return True


emp1 = Employee('name1', 'last1', 20000)
emp2 = Employee('name2', 'last2', 30000)

Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

# another way of providing input values
emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-60000'
emp_str3 = 'Jane-Doe-70000'

new_emp11 = Employee.from_string(emp_str2)

print(new_emp11.email)
print(new_emp11.salary)

from datetime import date

myDate = date(2021, 12, 11)
print(Employee.is_workday(myDate))