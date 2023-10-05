# There are 2 types of inheritance in python

# -Single Inheritance
# -Multiple Inheritance

print("Single Inheritance")


class Animal1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Screams")
        # return "Scream"
        # raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal1):
    def speak(self):
        # print("Woof")
        return "Woof!!!!"


class Cat(Animal1):
    def speak(self):
        return "Meow!"


d = Dog("Fido")
print(d.name)
print(d.speak())

c = Cat("Fluffy")
print(c.name)
print(c.speak())

a = Animal1("Tiger")
print(a.name)
# print(a.speak())

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

print("Multiple Inheritance")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Flyer:
    def fly(self):
        print(f"{self.name} is flying.")


class Swimmer:
    def swim(self):
        print(f"{self.name} is swimming.")


class Duck(Animal, Flyer, Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def quack(self):
        print(f"{self.name} is quacking.")


# Create a duck instance and call its methods
donald = Duck("Donald")
donald.eat()  # Output: Donald is eating.
donald.fly()  # Output: Donald is flying.
donald.swim()  # Output: Donald is swimming.
donald.quack()  # Output: Donald is quacking.
