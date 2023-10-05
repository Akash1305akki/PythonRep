# single - multi line string

x = "Welcome"
y = """hello everyone....
Welcome to the workshop"""

print(x)
print(y)
print(y[5])

# Slicing operation
a = x[2:5]
print(a)
print(x[2:])
print(x[:5])
print(x[:-4])

# upper(), lower(), strip(), replace(), split()

A = " Welcome, Everyone !!! "

print(A.upper())
print(A.lower())
print(A.strip())
print(A.split(","))
print(A.replace("Everyone","All"))

# String Concatenation
A = " Welcome, Everyone !!! "
B = "To the class"

C = A + B
print(C)

C = A + B + " Let's Start."
print(C)

# Formatting a string

num = 10
# txt = "My age is {}" + num
# print(txt)

txt = "My age is {}"

print(txt.format(num))
print(txt)
# print(num.__format__(txt))
# print(num)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# escape characters in string

txt = "We are the so-called \nViking\' from the north."
print(txt)

# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed

# Methods in string

name = "harry"
print(name.title())


# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


# Booleans in python

x = "Hello"
y = 12

print(bool(x))
print(bool(y))

# Any string is True, except empty strings.
#
# Any number is True, except 0.
#
# Any list, tuple, set, and dictionary are True, except empty ones.

x = 200
print(isinstance(x, int))