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

    def applyRaise(self):
        self.salary = int(self.salary * self.raise_amt)



class Developer(Employee):
    # class variable
    raise_amt = 1.10

    def __init__(self, fname, lname, salary, prg_lang):
        super().__init__(fname, lname, salary) # or
        # Employee.__init__(self, fname, lname, salary)
        # instance variable
        self.prg_lang = prg_lang


class Manager(Employee):

    def __init__(self, fname, lname, salary, employees=None): # dont pass mutable objects(list) to init method
        super().__init__(fname, lname, salary)  # or
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def display_emp(self):
        for emp in self.employees:
            print('--> ' + emp.getDetails())
        # print(['-->' + emp.getDetails() for emp in self.employees])


dev1 = Developer('name1', 'last1', 20000, 'Python')
dev2 = Developer('name2', 'last2', 30000, 'Java')

# print(help(Developer)) #usefull cmd to check all the inherited attributes that an Empty Sub-Class gets from Parent Class

# print(Employee.raise_amt)
# print(dev1.salary)
# dev1.applyRaise()
#
# print(dev1.salary)

# print(dev1.email)
# print(dev1.prg_lang)
#
# print(help(type(Developer)))
# help(type(Developer))

# manager details
mgr1 = Manager('lokesh', 'K', '90000', [dev1])
mgr1.add_employee(dev2)
mgr1.remove_employee(dev1)
# print(mgr1.__dict__)
# print(help(Manager))
print(mgr1.email)
mgr1.display_emp()

print(isinstance(mgr1, Manager))    # check if mgr1 is an instance of Manager Class

print(issubclass(Manager, Employee)) # check if Manager is an subclass of Employee Class