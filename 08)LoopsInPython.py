i = 0
while i < 6:
    print(i)
    i += 1

print("------------------------")
print("For with break")
i = 0
while i < 6:
    print(i)
    if i == 3:
        print("Loop Ends")
        break
    i += 1

print("------------------------")
print("For with continue")

i = 0
while i < 6:
    i += 1
    if i == 3:
        print("i is 3")
        continue
    print(i)

print("------------------------")
print("For with else")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print("------------------------")
print("------------------------")
print("For Loops")

for x in range(6):
    print(x)

print("------------------------")
print("Comprehension methods in For")

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        print("Inside IF")

print("------------------------")
print("Double/Nested For Loops")

for x in range(5):
    for y in range(5):
        print(x, y)
        
print("------------------------")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
