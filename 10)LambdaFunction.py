# A lambda function can take any number of arguments,
# but can only have one expression.
from typing import Callable, Any

# Syntax: lambda arguments : expression

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(6, 5))

print("----------------------------------------------")
print("Lambda inside function block")


def myfunc(n):
    print(n)
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))

# def myfunc(n):
#     print(n)
#     return n * 2
#
#
# mydoubler = myfunc(5)
#
# print(mydoubler)




