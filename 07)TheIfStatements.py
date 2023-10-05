# If Statement

a = 33
b = 200

if b > a:
    print("b is greater than a")
print("The End")

print("-----------------------------------------------")

# If_Else Statement

if b > a:
    print("b is greater than a")
else:
    print("Inside If_Else Loop")
print("The End")

print("-----------------------------------------------")

# If_Elif_Else Statement

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print("The End")

print("-----------------------------------------------")

# Short_Hand If
if a > b: print("a is greater than b")

# Short_Hand If_Else
print("A is Greater") if a > b else print("B is Greater")

# Short_Hand If_Elif_Else
print("A is Greater") if a > b else print("Both were Equal") if a == b else print("B is Greater")

print("-----------------------------------------------")

# Nested_If

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Logical Operators with If
print("AND")
if x > 10 and x > 20:
    print("Above ten, and also above 20!")

print("NOT")
if not x < 40:
    print("Below 40")

print("OR")
if x > 10 or x < 20:
    print("Above ten, but not above 20.")