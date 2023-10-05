from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


d = Dog()
print(d.speak())  # Output: Woof!

c = Cat()
print(c.speak())  # Output: Meow!

print("------------------------------------------------------------------------")


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(shape.area())
