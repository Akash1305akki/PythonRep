# In Python, polymorphism refers to the ability of objects to take on multiple
# forms or behaviors. Specifically, it allows different types of objects to be
# treated as if they were the same type of object.
#
# There are two main types of polymorphism in Python:
#             1)Duck Typing
#             2) Method Overriding

print("1) Duck Typing")


class Bird:
    def fly(self):
        print("The bird is flying")


class Airplane:
    def fly(self):
        print("The airplane is flying")


def airborne_thing(thing):
    thing.fly()


bird = Bird()
airplane = Airplane()

airborne_thing(bird)
airborne_thing(airplane)

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

print("2) Method Overriding")

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


my_animals = [Dog(), Cat()]

for animal in my_animals:
    animal.sound()
