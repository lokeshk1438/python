# creating a class with empty body and assigning values after creating the objects

class Employee:
    # class variables
    raise_amt = 1.04
    num_emps = 0 # calculate the total num of employees

    def __init__(self, fname, lname):
        # instance variable
        self.fname = fname
        self.lname = lname

    # defining getters
    @property   # makes the email function to be accessed as an attribute(as str) without function call
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    # to set the fullname and get the fname, lname and email use setter decorator on the particular property
    # in this case use @fullname.setter
    # defining setters
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    # defining deleters
    @fullname.deleter
    def fullname(self):
        print("Deleting the Name...")
        self.fname = None
        self.lname = None
        print("Name is Deleted.")



emp1 = Employee('John', 'Smith')
emp1.fname = 'Jim'

emp1.fullname = 'Lokesh Koturu'

print(emp1.fname)
print(emp1.email)    # changed from emp1.email()
print(emp1.fullname) # changed from emp1.fullname()

del emp1.fullname # delete the name
