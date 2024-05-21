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





# https://www.codingdors.com/problem/123
"""
last_character
Show Solution
Write a function that returns the last character of a given string.

last_character('hello') -> 'o'

last_character('world') -> 'd'

last_character('CodingDors') -> 's'

Theory
last_character
1. Function Definition: This is defining the structure of our function, including its name, parameters, and what it returns. 
def last_character(string):

2. String Indexing: This allows us to access individual characters in a string using their index positions. 
string[-1]
 accesses the last character in the string.

3. Return Statement: This specifies the output of our function. 
return string[-1]
 returns the last character of the string which is stored at index position -1. Example: suppose we have a string 
example_string = 'Hello World!'
. 
1. Our function definition would be: 

def last_character(string):
 
2. We will access the last character of this string using indexing which gives us the character '!' 

example_string[-1]
Output: '!' 

3. We will use a return statement to output the result when the function is called. The complete function would be:

def last_character(string):
    return string[-1]

Now, when we call 
last_character('Hello World!')
, we'll get output: '!'

Hint
last_character
1. Strings can be indexed just like lists. 

2. The index for the last character of a string is always -1. 

3. To return a specific character from a string, use the indexing syntax string[index]. 

4. The index value can be both positive or negative.
"""
# My Code
def last_character(s: str) -> str:
    return s[-1]
 
# Solution
def last_character(s: str) -> str:
    return s[-1]
 
# IA's Solutions
### Alternative 1: Using Negative Indexing
# Your solution already uses negative indexing, which is both concise and widely used:
def last_character(s: str) -> str:
    return s[-1]

### Alternative 2: Using `len()` Function
# This solution utilizes the `len()` function to find the length of the string and subtracts one to get the last character:
def last_character(s: str) -> str:
    return s[len(s) - 1]
# Explanation: `len(s)` gives the length of the string, and `len(s) - 1` gives the index of the last character.

### Alternative 3: Using Slicing
# Slicing can also be used to extract the last character:
def last_character(s: str) -> str:
    return s[-1:]
# Explanation: `s[-1:]` slices the string from the second-to-last character to the end, but since there's only one character at `-1`, it effectively returns the last character.

### Alternative 4: Conditional Check for Empty String
# This method includes a check for an empty string to avoid potential errors:
def last_character(s: str) -> str:
    if s:
        return s[-1]
    return ''
# Explanation: This function first checks if the string is non-empty using `if s:`. If the string is empty, it returns an empty string.

### Alternative 5: Using Itertools (Redundant but Demonstrative)
# Using `itertools` to explicitly demonstrate iteration:
from itertools import islice
def last_character(s: str) -> str:
    last_char = next(islice(s, len(s) - 1, None), '')
    return last_char
# Explanation: This method makes use of `itertools.islice` to slice the string from `len(s)-1` to the end, then gets the next item from this slice, which will be the last character.

### Alternative 6: Using `reversed()` and `next()`
# Using `reversed()` and `next()` to get the last character:
def last_character(s: str) -> str:
    return next(reversed(s))
# Explanation: `reversed(s)` provides an iterator that yields the elements of the string in reverse order, and `next()` returns the first element of this reversed iterator, which corresponds to the last character of the original string.

### Alternative 7: Using Try-Except for Robustness
# Using a try-except block to handle potential cases where the string might be empty:
def last_character(s: str) -> str:
    try:
        return s[-1]
    except IndexError:
        return ''
# Explanation: The code tries to access the last character using `s[-1]`. If the string is empty, it raises an `IndexError`, and the except block catches this exception and returns an empty string.
# These are various ways to achieve the same functionality, showcasing both simplicity and robustness in handling different edge cases.





# https://www.codingdors.com/problem/124
"""
concatenate_strings
Show Solution
Write a function that concatenates two given strings.

concatenate_strings('hello', 'world') -> 'helloworld'

concatenate_strings('Coding', 'Dors') -> 'CodingDors'

concatenate_strings('apple', 'banana') -> 'applebanana'

Theory
concatenate_strings
1. Strings: A string is a sequence of characters that can be either letters, numbers, or symbols. They are enclosed in quotes and immutable. 
'Hello world'
 is an example of a string.

2. Concatenation: Concatenation is the process of combining two or more strings into a single string. It is done using the '+' operator in Python. Example: 

str1 = 'Hello'
str2 = 'World'
concatenated_string = str1 + str2
print(concatenated_string)

Output: 'HelloWorld'

3. Function: A function is a block of code that performs a specific task. It takes input, performs some operation on the input, and returns the output. In Python, a function is defined using the 'def' keyword, followed by the function name, input parameters, and colon. Example: 

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(3, 5)
print(result)

Output: 8

Hint
concatenate_strings
1. You will need to define a function with two parameters, one for each string.

2. You will need to use the concatenation operator (
+
) to join the two strings together.

3. Remember to return the concatenated string.
"""
# My Code
def concatenate_strings(s1: str, s2: str) -> str:
    return s1+s2
 
# Solution
def concatenate_strings(s1: str, s2: str) -> str:
	return s1 + s2
 
# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here is your initial solution for concatenating two strings in Python:
def concatenate_strings(s1: str, s2: str) -> str:
    return s1 + s2
# This solution uses the `+` operator to concatenate the two strings `s1` and `s2`. Here are a few more alternative solutions to achieve the same result, with explanations.

### 1. Using `join()` Method
# The `join()` method can be used with an empty string separator to concatenate two strings:
def concatenate_strings(s1: str, s2: str) -> str:
    return ''.join([s1, s2])
# **Explanation:**
# - `join()` is a string method that concatenates the strings in the iterable (in this case, a list) using the string it's called on as a separator. Here, the separator is an empty string `''`, so the strings are concatenated directly.

### 2. Using Formatted String Literals (f-strings)
# Formatted string literals (f-strings), introduced in Python 3.6, can also be used for concatenation:
def concatenate_strings(s1: str, s2: str) -> str:
    return f"{s1}{s2}"
# **Explanation:**
# - F-strings provide a way to embed expressions inside string literals, using curly braces `{}`. Here, we embed `s1` and `s2` within an f-string to concatenate them.

### 3. Using `%` Operator (Old-style string formatting)
# Using the `%` operator for string formatting:
def concatenate_strings(s1: str, s2: str) -> str:
    return "%s%s" % (s1, s2)
# **Explanation:**
# - The `%` operator is used for string formatting. `%s%s` is a format string, where both `%s` are placeholders for the strings within the tuple `(s1, s2)`.

### 4. Using `format()` Method
# The `format()` method can be used to concatenate strings:
def concatenate_strings(s1: str, s2: str) -> str:
    return "{}{}".format(s1, s2)
# **Explanation:**
# - The `format()` method allows replacement fields defined by `{}` to be replaced by the arguments (`s1` and `s2`). Here, `{}` placeholders are used to insert `s1` and `s2`.

### 5. Using String Builder with `io.StringIO` (Efficient for large concatenations)
# For large-scale string concatenation, using `StringIO` can be efficient:
import io
def concatenate_strings(s1: str, s2: str) -> str:
    output = io.StringIO()
    output.write(s1)
    output.write(s2)
    return output.getvalue()
# **Explanation:**
# - `io.StringIO` provides an in-memory stream for text I/O. Using `write()` methods allows appending strings efficiently, and `getvalue()` retrieves the concatenated string.
# All these methods serve to concatenate two strings but might vary in terms of performance and readability. For simple tasks, the `+` operator is usually the most straightforward method. For more complex or performance-intensive tasks, other methods like `StringIO` could be more appropriate.





# https://www.codingdors.com/problem/125
"""
repeat_string
Show Solution
Write a function that repeats a given string n times.

repeat_string('hi', 3) -> 'hihihi' 

repeat_string('code', 2) -> 'codecode' 

repeat_string('a', 5) -> 'aaaaa'

Theory
repeat_string
1. Parameters: Parameters are the values passed to a function to perform an action or a task inside the function. Example: 
function myFunction(parameter1, parameter2) { }

2. Return Statement: The return statement is used to return a value from a function. Example: 
return value;
 
3. Loops: Loops are used to repeatedly execute a set of statements until a certain condition is met. Example: 
for (i = 0; i < n; i++) { }
 
4. Concatenation: Concatenation is the process of joining two or more strings together into one string. Example: 
str1 + str2
 
5. Function Declaration: A function declaration is a block of code that defines a function and specifies its properties. Example: 
function myFunction() { }

Hint
repeat_string
- The function has two parameters: the string to be repeated and the number of times it should be repeated. 

- Use a loop to repeat the string and keep track of the result in a variable. 

- Return the final result.
"""
# My Code
def repeat_string(s: str, n: int) -> str:
    return s*n
 
# Solution
def repeat_string(s: str, n: int) -> str:
	return s * n
 
# IA's Solutions
### Alternative 1: Using a Loop
# You can use a loop to construct the repeated string manually. This approach is more verbose but can be useful if you want to do something more complex inside the loop.
def repeat_string(s: str, n: int) -> str:
    result = ''
    for _ in range(n):
        result += s
    return result
# Explanation: We initialize an empty string `result`. Then, we loop `n` times, appending `s` to `result` during each iteration.

### Alternative 2: Using List Comprehension and `str.join`
# This method uses list comprehension to create a list of the string `s` repeated `n` times, and then joins them into a single string.
def repeat_string(s: str, n: int) -> str:
    return ''.join([s for _ in range(n)])
# Explanation: We use a list comprehension to create a list containing `s` repeated `n` times. The `join` method is then used to concatenate all elements in the list into a single string.

### Alternative 3: Using Generator Expression and `str.join`
# Similar to the list comprehension method, but using a generator expression which is more memory-efficient.
def repeat_string(s: str, n: int) -> str:
    return ''.join(s for _ in range(n))
# Explanation: We use a generator expression to produce `s` repeated `n` times. The `join` method efficiently concatenates these values into a single string without constructing an intermediate list.

### Alternative 4: Using Recursion
# You can use recursion to repeatedly append the string until the base case is met.
def repeat_string(s: str, n: int) -> str:
    if n <= 0:
        return ''
    elif n == 1:
        return s
    else:
        return s + repeat_string(s, n - 1)
# Explanation: This function works recursively. If `n` is 0 or less, it returns an empty string. If `n` is 1, it returns the string `s`. Otherwise, it appends `s` to the result of recursively calling itself with `n` decreased by one.

### Alternative 5: Using Functional Programming (`functools.reduce`)
# You can use the `reduce` function to accumulate the repeated string.
from functools import reduce
def repeat_string(s: str, n: int) -> str:
    return reduce(lambda acc, _: acc + s, range(n), '')
# Explanation: The `reduce` function is used to accumulate the string `s` `n` times. The lambda function takes two arguments (the accumulator and an element from the range). We ignore the element and just concatenate `s` to the accumulator.

### Alternative 6: Using String Multiplication in More Verbose Form
# Even though string multiplication is the most straightforward method, you can make it a bit more verbose if you want.
def repeat_string(s: str, n: int) -> str:
    repeated_s = s * n
    return repeated_s
# Explanation: We use string multiplication to create the repeated string and then return it. This is similar to your original solution, but separates the steps explicitly.




# https://www.codingdors.com/problem/
"""

"""
# My Code

# Solution

# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

# Solution

# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

# Solution

# IA's Solutions
