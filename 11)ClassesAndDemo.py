# A class variable and its scope

class MyClass:
    x = 5
    print(x)


p1 = MyClass()
print(p1.x)

print("-------------------------------------------")
print("__init__ function")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



#     def __str__(self):
#         return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# print(p1)

print("------------------------------------------")
print("The Pass Statement")


# class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.

class Person:
    pass
