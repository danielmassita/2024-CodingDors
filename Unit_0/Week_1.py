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
second_character
Show Solution
Write a function that returns the second character of a given string.

second_character('hello') -> 'e'

second_character('world') -> 'o'

second_character('CodingDors') -> 'o'

Theory
second_character
1. String: A sequence of characters wrapped in quotes. 
"Hello, World!"

2. Indexing: Accessing individual items in a collection by their position. 
"Coding"[2]
 returns "d".

3. Function: A block of reusable code that performs a specific task and returns a value. 

def add_numbers(x, y):
    return x + y

4. Return statement: Specifies the value that a function should return when called. 

def square(x):
    return x * x

5. Method: A function associated with an object that can modify or access the state of the object.
"hello".upper()
 returns "HELLO".

 Hint
second_character
1. Remember that characters in a string are indexed starting from 0.

2. To access a specific character in a string, use square brackets and the index number of the desired character.

3. The index of the second character is 1, since we start counting from 0.

4. The function should take in a string as an argument.
"""
# My Code
def second_character(s: str) -> str:
    return s[1]
 
# Solution
def second_character(s: str) -> str:
    second = s[1]
    return second
 
# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are a few alternative solutions for the function that returns the second character of a given string, along with explanations for each:

### Solution 1: Using List Indexing
# Similar to your original solution, but with additional checks for robustness.
def second_character(s: str) -> str:
    if len(s) < 2:
        raise ValueError("String must have at least two characters.")
    return s[1]
# **Explanation:** 
# - This version adds a check to ensure the input string has at least two characters. If it doesn't, it raises a `ValueError`.

### Solution 2: Using a Function with Try-Except Block
# This approach uses a try-except block to handle errors gracefully.
def second_character(s: str) -> str:
    try:
        return s[1]
    except IndexError:
        raise ValueError("String must have at least two characters.")
# **Explanation:** 
# - This version attempts to access the second character and catches any `IndexError` that might occur for strings shorter than two characters. It raises a `ValueError` in such cases.

### Solution 3: Using Slicing
# You can also use slicing to achieve the same result.
def second_character(s: str) -> str:
    if len(s) < 2:
        raise ValueError("String must have at least two characters.")
    return s[1:2]
# **Explanation:** 
# - This version slices the string to extract the second character. The slicing `s[1:2]` ensures that you get the second character in the form of a string, though it's essentially the same as `s[1]` in this case.

### Solution 4: Using a For Loop (General Example)
# This might be overkill but illustrates the flexibility of using loops.


def second_character(s: str) -> str:
    second_char = ""
    for index, char in enumerate(s):
        if index == 1:
            second_char = char
            break
    if not second_char:
        raise ValueError("String must have at least two characters.")
    return second_char
# **Explanation:**
# - This version uses a `for` loop with `enumerate` to iterate through the string. When it finds the second character (`index == 1`), it breaks the loop and returns the character.
# - If no second character is found, it raises a `ValueError`.

### Solution 5: Using functools.reduce (Functional Programming Approach)
# This is a functional programming approach, though not the most practical for this simple task.
from functools import reduce
def second_character(s: str) -> str:
    if len(s) < 2:
        raise ValueError("String must have at least two characters.")
    return reduce(lambda acc, char: (acc + 1, char) if acc[0] == 0 else acc, s, (0,))[1]
# **Explanation:**
# - This version uses `functools.reduce` to iterate through the string while keeping a count of the current position. It returns the second character once the count reaches the necessary position.
# - Again, it checks for string length at the beginning to handle short strings gracefully.
# Each of these solutions showcases different aspects of Python's capabilities, from simple indexing to more complex error handling and functional programming. The choice of which to use depends on your specific requirements and coding style preferences.





# 
