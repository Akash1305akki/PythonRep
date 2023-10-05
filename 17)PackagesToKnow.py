# PYTHON DATE AND TIME
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print(x)


# %a	Weekday, short version	-- Wed
# %A	Weekday, full version	-- Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday  -- 	3
# %d	Day of month 01-31	--  31
# %b	Month name, short version	--  Dec
# %B	Month name, full version	--  December
# %m	Month as a number 01-12   --	12
# %y	Year, short version, without century  --	18
# %Y	Year, full version	--  2018
# %H	Hour 00-23	--  17
# %I	Hour 00-12	--  05
# %p	AM/PM	--  PM
# %M	Minute 00-59	--  41
# %S	Second 00-59	--  08
# %f	Microsecond 000000-999999  --  	548513
# %z	UTC offset	--  +0100
# %Z	Timezone	--  CST
# %j	Day number of year 001-366  --	365
# %U	Week number of year, Sunday as the first day of week, 00-53	--  52
# %W	Week number of year, Monday as the first day of week, 00-53	--  52
# %c	Local version of date and time	Mon Dec 31 17:41:00 --  2018
# %C	Century	-- 20
# %x	Local version of date	--  12/31/18
# %X	Local version of time	--  17:41:00
# %%	A % character	--  %
# %G	ISO 8601 year	--  2018
# %u	ISO 8601 weekday (1-7)	 --  1
# %V	ISO 8601 weeknumber (01-53)	--  01


# PYTHON MATH

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)


x = abs(-7.25)
print(x)


x = pow(4, 3)
print(x)

import math


x = math.sqrt(64)
print(x) # returns 8


x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1


x = math.pi
print(x) # returns the value of pi

# MATH FUNCTIONS
# math.acos()	Returns the arc cosine of a number
# math.acosh()	Returns the inverse hyperbolic cosine of a number
# math.asin()	Returns the arc sine of a number
# math.asinh()	Returns the inverse hyperbolic sine of a number
# math.atan()	Returns the arc tangent of a number in radians
# math.atan2()	Returns the arc tangent of y/x in radians
# math.atanh()	Returns the inverse hyperbolic tangent of a number
# math.ceil()	Rounds a number up to the nearest integer
# math.comb()	Returns the number of ways to choose k items from n items without repetition and order
# math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter
# math.cos()	Returns the cosine of a number
# math.cosh()	Returns the hyperbolic cosine of a number
# math.degrees()	Converts an angle from radians to degrees
# math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
# math.erf()	Returns the error function of a number
# math.erfc()	Returns the complementary error function of a number
# math.exp()	Returns E raised to the power of x
# math.expm1()	Returns Ex - 1
# math.fabs()	Returns the absolute value of a number
# math.factorial()	Returns the factorial of a number
# math.floor()	Rounds a number down to the nearest integer
# math.fmod()	Returns the remainder of x/y
# math.frexp()	Returns the mantissa and the exponent, of a specified number
# math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
# math.gamma()	Returns the gamma function at x
# math.gcd()	Returns the greatest common divisor of two integers
# math.hypot()	Returns the Euclidean norm
# math.isclose()	Checks whether two values are close to each other, or not
# math.isfinite()	Checks whether a number is finite or not
# math.isinf()	Checks whether a number is infinite or not
# math.isnan()	Checks whether a value is NaN (not a number) or not
# math.isqrt()	Rounds a square root number downwards to the nearest integer
# math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
# math.lgamma()	Returns the log gamma value of x
# math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
# math.log10()	Returns the base-10 logarithm of x
# math.log1p()	Returns the natural logarithm of 1+x
# math.log2()	Returns the base-2 logarithm of x
# math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
# math.pow()	Returns the value of x to the power of y
# math.prod()	Returns the product of all the elements in an iterable
# math.radians()	Converts a degree value into radians
# math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
# math.sin()	Returns the sine of a number
# math.sinh()	Returns the hyperbolic sine of a number
# math.sqrt()	Returns the square root of a number
# math.tan()	Returns the tangent of a number
# math.tanh()	Returns the hyperbolic tangent of a number
# math.trunc()	Returns the truncated integer parts of a number


# MATH CONSTANTS
# math.e	Returns Euler's number (2.7182...)
# math.inf	Returns a floating-point positive infinity
# math.nan	Returns a floating-point NaN (Not a Number) value
# math.pi	Returns PI (3.1415...)
# math.tau	Returns tau (6.2831...)