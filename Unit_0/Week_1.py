"""
CODING DORS
UNIT 0 - FUNCTIONS AND VARIABLES - https://cs50.harvard.edu/python/2022/notes/0/
WEEK 1 - Strings - https://www.codingdors.com/week/1
"""

# https://www.codingdors.com/problem/121
"""
first_character
Show Solution
Write a function that returns the first character of a given string.

first_character('hello') -> 'h'

first_character('world') -> 'w'

first_character('CodingDors') -> 'C'

Theory
first_character
1. A block of organized, reusable code that performs a single, related action. 
''.capitalize()
 is an example of a built-in function in Python.

2. A sequence of characters enclosed in single or double quotes. 
'hello'
 is an example of a string.

3. Refers to accessing an individual element within a string or a list by its position. In Python, indexing starts at 0. For example, 
'hello'[0]
 returns 'h'.

4. A statement used inside a function to output a value (or values) to the calling function. In Python, 'return' statement is used as follows:

def my_function():
    ...
    return value

where 'value' is the output that the function returns. Example:

def first_character(string):
    return string[0]

Hint
first_character
- You will need to define a function that takes in a string as a parameter.

- Recall that indexing starts at 0 in Python. 

- To access the first character of a string, you will need to use the index 0.

- You can use string slicing to extract the first character of the string.
"""
# My Code
def first_character(s: str) -> str:
    return s[0]
  
# Solution
def first_character(s: str) -> str:
    first = s[0]
    return first
  
# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here are a few alternative solutions in Python with explanations:

# 1. Using string indexing without a separate function:
s = 'hello'
first_char = s[0]
print(first_char)  # Output: 'h'
# In this approach, instead of creating a separate function, you directly access the first character of the given string using index `[0]`.

# 2. Using the `charAt()` method (similar to Java):
def first_character(s: str) -> str:
    return s.charAt(0)
# print(first_character('hello'))  # Output: 'h'
# This approach uses the `charAt()` method to extract the first character of the string. Though not native to Python, you can define a function to replicate this behavior.

# 3. Using string slicing with a range of [0:1]:
def first_character(s: str) -> str:
    return s[0:1]
# print(first_character('hello'))  # Output: 'h'
# This approach uses string slicing with a range of `[0:1]` to extract the first character of the string. It's a more explicit way of achieving the same result as direct indexing.
# These are just a few alternative solutions to get the first character of a string in Python. The original function you provided (`s[0]`) is concise and efficient for this task.





# https://www.codingdors.com/problem/122
"""

"""
