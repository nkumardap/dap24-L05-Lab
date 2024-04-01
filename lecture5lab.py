# Your names and CNET IDs here

"""
EXCERCISE 1

Create a function named calculate_average that that takes a list of numbers as 
an argument and returns the average. Ensure that the function returns 
an empty list by returning 0.

Hint: len(list) will return the length of a list
"""

"""
EXCERCISE 2

Create a function named is_prime that takes an integer as an input and returns
True (a boolean) if the number is a prime number and False if it is not. 
A prime number is a number that is only divisible by 1 and itself. Remember 
to include the following error messages:

    1. If the number is a float instead of an integer, return "Error 001"
    2. If the number is a string instead of an integer, return "Error 002"

Hint: x is divisible by y if and only if x % y = 0

Hint: You will, at some point, have to loop over all integers from 0 to x

Hint: the command isinstance(x, int) will return True if x is an instance of 
the int data type. The same is true for float and str data types
"""

"""
EXCERCISE 3

Create a function named valid_password that takes a string as an input. It will
return True if (1) the string is longer than 8 characters and (2) has at least
one upper case character and (3) has at least one lower case character and
(4) has one digit. Otherwise, it will return False.

Hint: A string is a container that contains characters. You can loop over 
these characters by using a for loop. Each character you loop over is a string

Hint: The line of code "return False" will end the function and can be used in
different lines - you don't have to reserve it for the very end!

Hint: The following methods belong to string objects and return True if the
string they are attached to contains only upper case letters, lower case letters,
and digits respectively: 
    .isupper()
    .islower()
    .isdigit()
"""
