# creating a class with empty body and assigning values after creating the objects

class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp1)

emp1.fname = 'user1'
emp1.lname = 'test1'
emp1.salary = 20000

emp2.fname = 'user2'
emp2.lname = 'test2'
emp2.salary = 30000

print(emp2.salary)
print(emp1.salary)