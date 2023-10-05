x = "Hello World"	# String
print(x)

x = 20   # int
print(x)

x = 20.5  # float
print(x)

x = 1j    # complex
print(x)

x = ["apple", "banana", "cherry"]     # list - mutable - append & insert
print(x)

x = ("apple", "banana", "cherry")   # tuple - immutable
print(x)

x = range(6)	# range
print(x)

x = {"first_name" : "John", "age" : 36}	    # dict - create: x['last_name']='depp'- update: y = {'last_name' : 'depp'} - mutable
print(x)

x = {"apple", "banana", "cherry"}	# set - mutable
print(x)

x = frozenset ({"apple", "banana", "cherry"})	# frozenset - immutable
print(x)

x = True	# bool
print(x)

x = b"Hello"	# bytes
print(x)

x = bytearray(5)	# bytearray
print(x)

x = memoryview(bytes(5))	# memoryview
print(x)

x = None	# NoneType
print(x)