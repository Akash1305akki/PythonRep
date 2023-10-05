class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("Myname is", self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Parent("Phil", "Dunphy")
x.printname()


# A child class with pass statement
class Child(Parent):
    pass


x = Child("Luke", "Dunphy")
x.printname()


# A child class without pass statement

class Child(Parent):
    def __init__(self, fname, lname):
        Parent.__init__(self, fname, lname)


x = Child("Luke", "Dunphy")
x.printname()


# A child class with additional methods

class Student(Parent):
    def __init__(self, fname, lname, year):
        Parent.__init__(self,fname, lname)
        # super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# x = Child("Luke", "Dunphy", 2019)
# x.printname()
# x.welcome()
# y = Parent("Phil", "Dunphy")
# y.printname()
