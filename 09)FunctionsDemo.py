# function syntax
# (def) (function name):
#   (function block)
#
# (function call)


def my_first_function():
    print("my_first_function")


print("before function")
my_first_function()
print("after function")

print("---------------------------------------------")
print("passing arguments in function")


def family_name(fname):
    print(fname + "Dunphy")


family_name("Phil")
family_name("Claire")
# family_name()

print("---------------------------------------------")
print("Arbitrary Arguments")


def youngest_kid_name(*kids):
    print("The youngest child is " + kids[2])


youngest_kid_name("Emil", "Tobias", "Linus")

print("---------------------------------------------")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

print("---------------------------------------------")
print("default arguments")


def my_country(country="Norway"):
    print("I am from " + country)


my_country("Sweden")
my_country("India")
my_country()
my_country("Brazil")

print("---------------------------------------------")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print("---------------------------------------------")
print("Returning a value")

def my_function(x):
    return 5 * x


print(my_function(2))
print(my_function(5))
print(my_function(9))
