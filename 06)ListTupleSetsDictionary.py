# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered and changeable. No duplicate members.

my_list = [ 1 , 34 , "Hello" , "world" , True]

# Accesing a list item

print(my_list)
print(my_list[2])
print(my_list[-1])
print(my_list[2:4])

# updating a list
my_list[2] = "HELLO"
print(my_list)
my_list[2:4] = ["hello", "WORLD"]
print(my_list)

my_list.insert(4, "Welcome")
print(my_list)

my_list.extend("everyone")
# thistuple = ("kiwi", "orange")
# my_list.extend(thistuple)
print(my_list)

my_list.append("Fruits")
print(my_list)

# Sorting a list
num = [1,5,2,62,2,43,5,6,2]
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]

num.sort()
print(num)
num.sort(reverse=True)
print(num)

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# copying a list
fruits1 = fruits.copy()
print(fruits1)

fruits2 = list(fruits1)
print(fruits2)

fruits0 = fruits1 + fruits2
print(fruits0)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

print("--------------------LIST IS OVER------------------------")


#  Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Updating a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
y[1] = "kiwi"
x = tuple(y)

print(x)

# thistuple = ("apple", "banana", "cherry")
# y = ("apple",)
# thistuple -= y
#
# print(thistuple)


# Joining a tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

print("--------------------TUPLE IS OVER------------------------")


# set2 = {1, 2, "world", 56, "hello"}
# print(set2)

# True and 1 are same hence not allowed
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Updating a set
thisset.add("orange")
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset.remove("banana")
print(thisset)

thisset.discard("orange")
print(thisset)


x = thisset.pop()
print(x)
x = thisset.pop()
print(x)
print(thisset)

# deleting a tuple

thisset.clear()
print(thisset)

this_tuple = ("apple", "banana", "cherry")
del this_tuple
# print(this_tuple)

# joining tuple

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

print("--------------------SET IS OVER------------------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Accesinng a dictionary
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)

# updating a dictionary

thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)

thisdict["color"] = "red"
print(thisdict)

# thisdict.update({"color": "red"})
# print(thisdict)

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary