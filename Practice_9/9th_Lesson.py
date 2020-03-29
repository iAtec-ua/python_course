"""class Employee:
    # Common base class for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        Employee.empCount -= 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# Create a new employee with name Zara and salary 2000
emp1 = Employee("Zara", 2000)
# Create a new employee with name Manni and salary 5000
emp2 = Employee("Manni", 5000)
emp3 = Employee("Max", 15000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

del emp3

print("Total employees", Employee.empCount)


class Parent:  # define parent class 
    def parentMethod(self):
        print("Calling parent method")

    def set_attr(self, attr):
        Parent.parentAttr = attr

    def get_attr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def childMethod(self):
        print("Calling child method")


    def getAttr(self):
        print("Hello kitty")

obj1 = Parent()
obj1.set_attr(123)
obj1.get_attr()
#obj1.parentMethod()

obj2 = Child()
#obj2.setAttr(123)
#obj2.getAttr()
obj2.childMethod()
obj2.parentMethod()"""