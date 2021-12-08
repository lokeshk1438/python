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


emp1 = Employee('name1', 'last1', 20000)
emp2 = Employee('name2', 'last2', 30000)
# print(emp1.getDetails())
# print(Employee.getDetails(emp1))
#
# print(emp1.salary)
# emp1.applyRates()
# print(emp1.salary)

# accessing class variables using class and object

# print(Employee.raise_amt)
# Employee.raise_amt = 2
# print(emp1.raise_amt)

# printing namespace of instance --> all the available attributes available
    # {'fname': 'name1', 'lname': 'last1', 'salary': 20000, 'email': 'name1.last1@gmail.com'}
print("before: ")
print(emp1.__dict__)

# printing namespace of class
    # {'__module__': '__main__', 'raise_amt': 2, '__init__': <function Employee.__init__ at 0x000001E48940EA60>, 'getDetails': <function Employee.getDetails at 0x000001E48940EAE8>, 'applyRates': <function Employee.applyRates at 0x000001E48940EB70>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
print(Employee.__dict__)

# changing raise amt for only instance
print(Employee.raise_amt)
emp1.raise_amt = 2
print(emp1.raise_amt)
print(Employee.raise_amt)

print("after")
# {'fname': 'name1', 'lname': 'last1', 'salary': 20000, 'email': 'name1.last1@gmail.com', 'raise_amt': 2} --> new field raise_amt is added to the instance
print(emp1.__dict__)


print("Employees: ", Employee.num_emps)