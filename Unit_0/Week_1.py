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
2. You will need to use the concatenation operator (+) to join the two strings together.
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





# https://www.codingdors.com/problem/126
"""
uppercase_first
Show Solution
Write a function that returns the given string with its first character in uppercase.
uppercase_first('hello') -> 'Hello'
uppercase_first('coding') -> 'Coding'
uppercase_first('leo') -> 'Leo'

Theory
uppercase_first
1. Strings: A string is a sequence of characters enclosed in quotes. It can be manipulated using different string methods or operators. 
'hello'
2. Indexing: Indexing is used to access individual characters or a range of characters from a sequence. In Python, indexing begins at 0 and goes on until the length of the sequence decrementing by 1. Indexing is done using square brackets. 
'hello'[0] -> 'h'
3. Slicing: Slicing is used to get a range of characters from a sequence and returns a new sequence. The syntax is 
seq[start:stop:step]
By default, start=0, stop=end of sequence, and step=1. 
'hello'[1:3]
 Output: 'el'
4. String concatenation: Concatenation is used to join two or more strings together. This is done using the + operator. 
'hello' + 'world'
 Output: 'helloworld'
5. String methods: There are many built-in string methods to manipulate strings. One of which is the capitalize() method that returns a copy of the string with its first character capitalized. 
'hello'.capitalize()
 Output: 'Hello'

Hint
uppercase_first
1. You can access the first character of a string using the index 0. 
2. You can use the string method upper() to convert a character to uppercase. 
3. You can concatenate strings using the + operator.
"""
# My Code
	def uppercase_first(s: str) -> str:
	    return s.capitalize()

# Solution
	def uppercase_first(s: str) -> str:
		first = s[0].upper()
		others = s[1:]
		return first + others

# IA's Solutions
### Method 1: Using String Slicing and `upper()`
	def uppercase_first(s: str) -> str:
	    if not s:  # Check if the string is empty
	        return s
	    return s[0].upper() + s[1:]
# **Explanation:**
# - `s[0]` accesses the first character of the string.
# - `s[0].upper()` converts the first character to uppercase.
# - `s[1:]` gets the rest of the string starting from the second character.
# - Concatenate the uppercase first character with the rest of the string.

### Method 2: Using f-string (formatted string literals)
	def uppercase_first(s: str) -> str:
	    if not s:  # Check if the string is empty
	        return s
	    return f"{s[0].upper()}{s[1:]}"
# **Explanation:**
# - Use an f-string to format the string.
# - `{s[0].upper()}` converts the first character to uppercase inside the f-string.
# - `{s[1:]}` appends the rest of the string.

### Method 3: Using `str.replace()` Method (less efficient, but an interesting approach)
	def uppercase_first(s: str) -> str:
	    if not s:  # Check if the string is empty
	        return s
	    first_char_upper = s[0].upper()
	    return s.replace(s[0], first_char_upper, 1)
# **Explanation:**
# - Convert the first character to uppercase using `s[0].upper()`.
# - Use `str.replace(old, new, count)` to replace the first occurrence of the first character with its uppercase version.

### Method 4: Using Regular Expressions (regex)
	import re
	def uppercase_first(s: str) -> str:
	    return re.sub(r"^\w", lambda match: match.group(0).upper(), s)
# **Explanation:**
# - Use the `re.sub` function to substitute the first word character (`^\w`).
# - The lambda function converts the matched character (first character of the string) to uppercase.

### Method 5: Using `str.title()` and Pre/Post Processing
	def uppercase_first(s: str) -> str:
	    if not s:  # Check if the string is empty
	        return s
	    return s[:1].title() + s[1:]
# **Explanation:**
# - `s[:1]` gets the first character of the string (`s[0]`).
# - `s[:1].title()` converts the first character to uppercase.
# - Concatenate with the rest of the string `s[1:]`.

### Method 6: Using conditional ternary for Python version prior to 3.8 (ternary operator)
	def uppercase_first(s: str) -> str:
	    return (s[0].upper() + s[1:]) if s else s
# **Explanation:**
# - Use a ternary operator to check if the string is empty.
# - If not empty, convert the first character to uppercase and concatenate with the rest of the string.





# https://www.codingdors.com/problem/127
"""
lowercase_first
Show Solution
Write a function that returns the given string with its first character in lowercase.
lowercase_first('Hello') -> 'hello'
lowercase_first('CODING') -> 'cODING'
lowercase_first('LeO') -> 'leO'

Theory
lowercase_first
1. str.lower() method: This method returns a string in lowercase. Example: 
'Hello World'.lower()
 Output: 'hello world'
2. String indexing: This is a way of accessing individual characters within a string using their position. Example: 
'coding'[1]  #'o'
3. String slicing: This is a way of creating a substring from a string by specifying a range of indices. Example: 
'Hello World'[2:6]  #'llo '
4. String concatenation: This is a way of joining two or more strings together. Example: 
'Hello' + ' World' #'Hello World'

Hint
lowercase_first
- The function should start by getting the first character of the string.
- Check if the first character is already lowercase.
- If the first character is already lowercase, return the original string.
- If the first character is uppercase, convert it to lowercase.
- Combine the lowercase first character with the rest of the original string and return it.
"""
# My Code
	def lowercase_first(s: str) -> str:
	    return s[0].lower() + s[1:]
	
# Solution
	def lowercase_first(s: str) -> str:
		first = s[0].lower()
		others = s[1:]
		return first + others
	
# IA's Solutions
### Alternative 1: Using String Slicing and Built-in Functions
# This method is quite similar to your approach but makes use of a different style of slicing.
	def lowercase_first(s: str) -> str:
	    return s[:1].lower() + s[1:]
# **Explanation:**
# - `s[:1]` gets the first character of the string.
# - `.lower()` converts this character to lowercase.
# - `s[1:]` gets the rest of the string.
# - Concatenating these two pieces gives the desired result.

### Alternative 2: Using the `replace` Method
# This method uses the `replace` function to replace the first character with its lowercase counterpart.
	def lowercase_first(s: str) -> str:
	    return s.replace(s[0], s[0].lower(), 1)
# **Explanation:**
# - `s.replace(s[0], s[0].lower(), 1)` replaces the first occurrence of the first character (`s[0]`) with its lowercase version.
# - The third argument `1` ensures that only the first occurrence is replaced.

### Alternative 3: Using Custom Function without String Slicing
# This method employs a more verbose approach without direct slicing.
	def lowercase_first(s: str) -> str:
	    if len(s) == 0:
	        return s  # Handle the edge case where the string is empty
	    first = s[0].lower()
	    rest = s[1:]
	    return first + rest
# **Explanation:**
# - This method first checks if the string is empty, returning it if it is.
# - Then it assigns `first` to the lowercase version of the first character.
# - `rest` is assigned the remainder of the string.
# - Finally, it concatenates `first` and `rest`.

### Alternative 4: Using `map` and `str.join`
# This method is a bit unconventional and uses `map` along with `str.join`.
	def lowercase_first(s: str) -> str:
	    if not s:
	        return s  # Handle the edge case where the string is empty
	    return ''.join(map(lambda x: x.lower() if i == 0 else x, s))

# Each string character is iterated upon using `map`. The lambda function applies `lower()` to the first character only.
def lowercase_first(s: str) -> str:
    if not s:
        return s  # Handle the edge case where the string is empty
    return ''.join(map(lambda x: x.lower() if idx == 0 else x, enumerate(s)))
# **Explanation:**
# - `enumerate(s)` is used to pair each character with its index.
# - The lambda function checks if the index is zero and applies `.lower()` to that character.
# - `str.join` concatenates the result into a single string.





# https://www.codingdors.com/problem/130
"""
replace_char
Show Solution
Write a function that replaces all occurrences of a specified character in a given string with another character.
replace_char('hello', 'l', 'w') -> 'hewwo'
replace_char('APPLE', 'P', 'Z') -> 'AZZLE'
replace_char('banana', 'a', '4') -> 'b4n4n4'

Theory
replace_char
1. String: A sequence of characters enclosed in quotation marks. 
'hello'
2. replace(): A built-in string method used to replace occurrences of a specified character or substring within a string with a given replacement string. 
'hello'.replace('l', 'w') #'hewwo'
3. for loop: A loop structure used for iterating through sequences, such as strings, where each element in the sequence is processed in turn. "hello"
# Example solution:
def replace_char(string, old_char, new_char):
    new_string = ''
    for char in string:
        if char == old_char:
            new_string += new_char
        else:
            new_string += char
    return new_string

Hint
replace_char
1. You will need to use a loop to iterate through each character in the string.
2. Use an if statement to check if the current character is the specified character that needs to be replaced.
3. If it is, replace that character with the new specified character.
4. If it's not, leave it as is.
5. Build a new string with the modified characters and return it.
"""
# My Code
	def replace_char(s: str, old_char: str, new_char: str) -> str:
	    return s.replace(old_char, new_char)
	
# Solution
	def replace_char(s: str, old_char: str, new_char: str) -> str:
		return s.replace(old_char, new_char)
	
# IA's Solutions
### 1. Using List Comprehension
# You can use a list comprehension to iterate through each character in the string, and replace the specified character when found. Finally, join the list back into a string.
	def replace_char(s: str, old_char: str, new_char: str) -> str:
	    return ''.join([new_char if char == old_char else char for char in s])
### Explanation:
# 1. Iterate through each character in the string `s`.
# 2. If the character equals `old_char`, replace it with `new_char`.
# 3. Join the list of characters back into a single string using `join`.

### 2. Using a For Loop
# You can achieve the same result using a simple for loop and string concatenation.
	def replace_char(s: str, old_char: str, new_char: str) -> str:
	    result = ''
	    for char in s:
	        if char == old_char:
	            result += new_char
	        else:
	            result += char
	    return result
### Explanation:
# 1. Initialize an empty string `result`.
# 2. Iterate through each character in the string `s`.
# 3. If the character equals `old_char`, append `new_char` to `result`; otherwise, append the original character.
# 4. Return the concatenated result.

### 3. Using `str.translate` and `str.maketrans`
# Python provides a `translate` method that can be used together with `maketrans` to carry out character replacements.
	def replace_char(s: str, old_char: str, new_char: str) -> str:
	    translation_table = str.maketrans(old_char, new_char)
	    return s.translate(translation_table)
### Explanation:
# 1. Create a translation table using `str.maketrans` that maps `old_char` to `new_char`.
# 2. Use `translate` method to apply the translation table to string `s`.

### 4. Using Regular Expressions (if multiple characters need to be replaced)
# This method can be overkill for single character substitutions but is useful when dealing with patterns.
	import re
	def replace_char(s: str, old_char: str, new_char: str) -> str:
	    # re.escape ensures that special characters are treated as literals
	    return re.sub(re.escape(old_char), new_char, s)
### Explanation:
# 1. Use `re.sub` from the `re` module to replace all occurrences of `old_char` with `new_char`.
# 2. `re.escape` is used to handle special characters by treating them as literals.

### Comparison:
# - The `replace` method is the most straightforward for simple character replacements.
# - List comprehension and for loop methods provide more control and can be more readable.
# - The `translate` method is efficient for single substitutions and can be extended easily for multiple substitutions.
# - The regular expression method is powerful but might be unnecessary for simple single-character replacements.





# https://www.codingdors.com/problem/131
"""
remove_char
Show Solution
Write a function that removes all occurrences of a specified character in a given string.
remove_char('hello', 'l') -> 'heo'
remove_char('apple', 'e') -> 'appl'
remove_char('BANANA', 'A') -> 'BNN'

Theory
remove_char
1. Strings: A string is a sequence of characters. In Python, strings are enclosed in either single or double-quotes. 
my_string = "Hello, world!"
2. Function Definition: A function is a block of reusable code used to perform a specific task. It takes some input, performs some operations, and returns an output. 
def remove_char(input_str, char_to_remove):
3. Iteration: Iteration refers to the process of repeating a set of instructions a specified number of times or until a condition is met. For instance, we can use a for loop to iterate over a string character by character. 
for char in my_string:
4. Conditional Statements: A conditional statement is used to perform different actions based on different conditions. For example, we might use an if statement to check if a given character matches the one we are trying to remove. 
if char != char_to_remove:
5. String Concatenation: String concatenation refers to the process of combining two or more strings into a single string. In Python, we can use the + operator to concatenate strings. 
new_string += char
6. Output: In Python, we can use the 'return' statement to specify the output of a function. 
return new_string

Hint
remove_char
- Think about iterating through the string and building a new string with the characters that don't match the specified character.
- You can use the built-in function replace()
- You can replace the char by an empty string ("")
"""
# My Code
	def remove_char(s: str, char_to_remove: str) -> str:
	    return s.replace(char_to_remove, "")

# Solution
	def remove_char(s: str, char_to_remove: str) -> str:
		return s.replace(char_to_remove, "")
	
# IA's Solutions
### 1. Using List Comprehension
# You can use list comprehension to filter out unwanted characters and then join the list back into a string.
	def remove_char(s: str, char_to_remove: str) -> str:
	    return ''.join([c for c in s if c != char_to_remove])
# **Explanation:**
# - `[c for c in s if c != char_to_remove]` creates a list of characters from `s` that are not equal to `char_to_remove`.
# - `''.join(...)` combines the list of characters back into a single string.

### 2. Using the `filter()` Function with a Lambda
# You can use the `filter()` function in combination with a lambda function to achieve the same result.
	def remove_char(s: str, char_to_remove: str) -> str:
	    return ''.join(filter(lambda c: c != char_to_remove, s))
# **Explanation:**
# - `filter(lambda c: c != char_to_remove, s)` filters out the characters where the condition is not met (`c != char_to_remove`).
# - `''.join(...)` combines the filtered list of characters back into a single string.

### 3. Using a For Loop
# You can use a for loop to iterate over the string and build the result manually.
	def remove_char(s: str, char_to_remove: str) -> str:
	    result = []
	    for c in s:
	        if c != char_to_remove:
	            result.append(c)
	    return ''.join(result)
# **Explanation:**
# - `result = []` initializes an empty list to store the characters that are not removed.
# - The for loop iterates over each character `c` in `s`.
# - If `c` is not equal to `char_to_remove`, it is added to the `result` list.
# - `''.join(result)` combines the list back into a single string.

### 4. Using Recursion
# Here's a recursive approach to remove the specified character:
	def remove_char(s: str, char_to_remove: str) -> str:
	    if s == "":
	        return s
	    if s[0] == char_to_remove:
	        return remove_char(s[1:], char_to_remove)
	    return s[0] + remove_char(s[1:], char_to_remove)
# **Explanation:**
# - The base case checks if the string is empty (`s == ""`), in which case it returns the empty string.
# - If the first character of the string `s[0]` is equal to `char_to_remove`, it skips this character and calls the function recursively with the rest of the string `s[1:]`.
# - If the first character is not equal to `char_to_remove`, it concatenates the first character `s[0]` with the result of the recursive call on the rest of the string `s[1:]`.

### 5. Using String Translation
# You can use the `str.translate` method, which can be very efficient as it is implemented in C.
	def remove_char(s: str, char_to_remove: str) -> str:
	    return s.translate(str.maketrans('', '', char_to_remove))
# **Explanation:**
# - `str.maketrans('', '', char_to_remove)` creates a translation table that maps each character in `char_to_remove` to `None`.
# - `s.translate(...)` removes all characters in `char_to_remove` as specified by the translation table.





# https://www.codingdors.com/problem/134
"""
string_length
Show Solution
Write a function that returns the length of a given string.
string_length('hello') -> 5
string_length('code') -> 4
string_length('CodingDors') -> 10

Theory
string_length
1. Function: A function is a block of code that performs a specific task. In Python, we define functions using the 'def' keyword followed by the function name, parentheses, and a colon. Any code to be executed by the function is then indented. Example: 
def add_numbers(x, y):
    result = x + y
    return result
2. Strings: Strings are a sequence of characters enclosed in quotes. In Python, strings can be enclosed either in single quotes (' ') or double quotes (" "). Example: 
greeting = "Hello, world!"
3. Length: Length is a property of a string or a list that indicates the number of characters or items it contains. In Python, we can determine the length of a string or list using the 'len()' function. Example: 
my_list = [1, 3, 5, 7, 9]
list_length = len(my_list)  # list_length = 5
4. Return: The 'return' keyword is used to indicate the value that a function should return to its caller. A function can have multiple return statements, but once a return statement is executed, the function stops executing. Example: 
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
5. Argument: An argument is a value passed to a function when it's called. In Python, we can define functions that take any number of arguments using the '*args' and '**kwargs' syntax. Example: 
def greet(name):
    print("Hello, " + name + "!")
greet("Alice")  # prints "Hello, Alice!"
6. Method: A method is a function that is associated with an object and can be called on that object. In Python, we call methods using the dot notation. Example: 
my_sentence = "The quick brown fox jumps over the lazy dog."
sentence_length = my_sentence.count(" ")  # sentence_length = 9

Hint
string_length
1. Determine the data type of the input.

2. Use the appropriate built-in function to find the length of the string.

3. Return the length as an output.
"""
# My Code
	def string_length(s: str) -> int:
	    return len(s)
	
# Solution
	def string_length(s: str) -> int:
		return len(s)
	
# IA's Solutions
### 1. Iterative Approach Using a Loop
# You can manually iterate through each character in the string and count them.
	def string_length(s: str) -> int:
	    length = 0
	    for char in s:
	        length += 1
	    return length
# **Explanation:** 
# - Initialize a counter variable `length` to 0.
# - Loop through each character (`char`) in the string `s`.
# - For each character, increment the `length` counter by 1.
# - Finally, return the `length` counter.

### 2. Using a Recursive Function
# You can use a recursive approach to count the characters in the string.
	def string_length(s: str) -> int:
	    if s == "":
	        return 0
	    else:
	        return 1 + string_length(s[1:])
# **Explanation:** 
# - If the string `s` is empty (`""`), return 0.
# - Otherwise, return 1 plus the result of calling `string_length` on the remaining substring `s[1:]` (which is `s` without its first character).
# - This approach uses the principle of recursion to go through each character.

### 3. Using Built-in `sum` and `map`
# You can use the `sum` function and `map` to create a list of ones and sum them up.
	def string_length(s: str) -> int:
	    return sum(map(lambda x: 1, s))
# **Explanation:** 
# - `map(lambda x: 1, s)` creates an iterable where each character in string `s` is mapped to the number 1.
# - `sum` then adds up all the ones to get the total length of the string.

### 4. Using List Comprehension and `len`
# You can use list comprehension to create a list of ones and then calculate its length.
	def string_length(s: str) -> int:
	    return len([1 for char in s])
# **Explanation:**
# - `[1 for char in s]` creates a list with a `1` for each character in the string `s`.
# - `len` then calculates the length of this list, which is the same as the length of the string.

### 5. Using `collections.Counter`
# Although more complex than necessary, you can use `collections.Counter` to count the occurrences of each character.
	from collections import Counter
	def string_length(s: str) -> int:
	    return sum(Counter(s).values())
# **Explanation:**
# - `Counter(s)` creates a dictionary-like object where keys are characters and values are their counts in the string.
# - `sum(Counter(s).values())` sums up all the values, giving the total number of characters.
	




# https://www.codingdors.com/problem/135
"""
substring
Show Solution
Write a function that returns a substring of a given string, starting from the specified start index and ending with the specified end index.
substring('hello', 1, 2) -> 'el'
substring('CodingDors', 6, 9) -> 'Dors'
substring('applebananaorange', 5, 10) -> 'banana'

Theory
substring
1. String: A string is a sequence of characters enclosed within quotes. A string can be created using single quotes ('), double quotes ("), or triple quotes (" " "). Strings are immutable, meaning the original string cannot be changed, but a new string can be created from the original.
"Hello World"
2. Substring: A substring is a portion of a string, defined by a start index and an end index. The start index specifies where the substring begins, and the end index specifies where it ends. The resulting substring includes all characters from the start index up to, but not including, the end index.
s = "Hello World"
substring = s[6:11]
3. Function:
A function is a block of code that performs a specific task. Functions can take inputs (arguments) and return outputs. Functions can also be reused and called multiple times throughout a program.
def add(num1, num2):
    return num1 + num2
4. Return:
Return is a keyword used in functions to indicate the value returned by the function. When the return statement is executed, the function stops executing and returns the value specified.
def multiply(num1, num2):
    return num1 * num2
5. Index:
An index is the position of a character within a string or a list. In Python, indexing starts at 0, meaning the first character of a string or list has an index of 0.
s = "Hello World"
index = s[6]
 # index is 'W'

Hint
substring
1. Consider using string slicing to retrieve the substring based on the start and end indices.
2. The start index should be included in the substring, while the end index should be excluded.
3. Make sure to check for edge cases such as empty strings, invalid indices, and indices that are out of range for the given string.
"""
# My Code
	def substring(s: str, start: int, end: int) -> str:
	    return s[start:end+1]
	
# Solution
	def substring(s: str, start: int, end: int) -> str:
		sub = s[start:end+1]
		return sub
	
# IA's Solutions
# 1. Using slicing directly in the return statement:
def substring(s: str, start: int, end: int) -> str:
    return s[start:end+1]
# 2. Using the `slice` function to create a slice object and then apply it to the string:
def substring(s: str, start: int, end: int) -> str:
    return s[slice(start, end+1)]
# Both solutions achieve the same result by extracting the substring from the original string based on the provided start and end indices.




# https://www.codingdors.com/problem/137
"""
remove_whitespace_str
Show Solution
Write a function that removes all leading and trailing whitespace from a given string.
remove_whitespace_str('     hello') -> 'hello'
remove_whitespace_str('apple     ') -> 'apple'
remove_whitespace_str('      CodingDors      ') -> 'CodingDors'

Theory
remove_whitespace_str
1. strip() method: The strip() method removes whitespace from both ends of a string. Example: 
text = "   Hello   "
text_strip = text.strip()
print(text_strip) # "Hello"
2. lstrip() method: The lstrip() method removes whitespace from the beginning of a string. Example: 
text = "   Hello   "
text_lstrip = text.lstrip()
print(text_lstrip) # "Hello   "
3. rstrip() method: The rstrip() method removes whitespace from the end of a string. Example: 
text = "   Hello   "
text_rstrip = text.rstrip()
print(text_rstrip) # "   Hello"

Hint
remove_whitespace_str
1. Look up how to remove leading and trailing whitespace in Python.
2. You will need to define a function that takes a string as input.
3. Use the appropriate Python method to remove both leading and trailing whitespace.
4. Return the modified string.
"""
# My Code
	def remove_whitespace_str(s: str) -> str:
	    return s.strip()
	
# Solution
	def remove_whitespace_str(s: str) -> str:
		return s.replace(" ", "")
	
# IA's Solutions
# 1. Using regular expressions:
import re
def remove_whitespace_str(s: str) -> str:
    return re.sub(r'^\s+|\s+$', '', s)
# Explanation: This solution uses the `re.sub()` function from the `re` module in Python to replace leading and trailing whitespace with an empty string. The regular expression `r'^\s+|\s+$'` matches one or more whitespace characters (`\s+`) at the beginning of the string (`^`) or one or more whitespace characters at the end of the string (`\s+$`).
# 2. Using slicing:
def remove_whitespace_str(s: str) -> str:
    start = 0
    end = len(s)
    while start < end and s[start].isspace():
        start += 1
    while end > start and s[end - 1].isspace():
        end -= 1
    return s[start:end]
# Explanation: This solution uses two `while` loops to find the start and end indices of the non-whitespace portion of the string. It increments the start index while the character at that index is a whitespace character, and decrements the end index while the character at that index is a whitespace character. Finally, it returns the substring of the original string from the start index to the end index.




# https://www.codingdors.com/problem/251
"""
birthdate
Show Solution
Given two strings 'day' and 'month', return a new string with the birth date. 
Hint: birth date should be in the format 'month/day'
birthdate('03', '07') -> '07/03'
birthdate('29', '06') -> '06/29'
birthdate('01', '05') -> '05/01'

Theory
birthdate
1. String Concatenation: The ability to combine multiple strings into a single string. Example:
month = '07'
day = '03'
birth_date = month + '/' + day
print(birth_date)  # Output: '07/03'
2. String Formatting: The ability to create formatted strings by inserting values into specific placeholders. Example:
month = '07'
day = '03'
birth_date = '{}{}'.format(month, '/' + day)
print(birth_date)  # Output: '07/03'
month = '06'
day = '29'
birth_date = '{}/{}'.format(month, day)
print(birth_date)  # Output: '06/29'
3. String Operations: Performing operations on strings to manipulate or extract information. Example:
month = '05'
day = '01'
birth_date = month + '/' + day
print(birth_date)  # Output: '05/01'
month = '03'
day = '07'
birth_date = f'{month}/{day}'
print(birth_date)  # Output: '03/07'
These concepts will be useful in combining the month and day values into a single string with the desired format. By utilizing these techniques, you can implement the birthdate function to solve the problem.

Hint
birthdate
1. Use string concatenation to combine the 'month' and 'day' values.
2. Separate the 'month' and 'day' values with a forward slash (/) to form the desired format.
3. Return the combined string as the birth date.
"""
# My Code
	def birthdate(day: str, month: str) -> str:
	    return f"{month}/{day}"
	
# Solution
	def birthdate(day: str, month: str) -> str:
		return month + "/" + day
	
# IA's Solutions
# 1. Using f-string formatting:
def birthdate(day: str, month: str) -> str:
    return f"{month}/{day}"
# Explanation: In this solution, an f-string is used to directly format the output string with the values of `month` and `day`.
# 2. Using string concatenation:
def birthdate(day: str, month: str) -> str:
    return month + "/" + day
# Explanation: This solution uses the `+` operator to concatenate the strings `month`, "/", and `day` to form the birth date string.
# Both of these alternative solutions achieve the same result as the original solution provided.	




# https://www.codingdors.com/problem/252
"""
formatted_time
Show Solution
Given two strings 'hour' and 'minute', return a new string with the formatted time.
Hint: the time should be in the format 'hour:minute'
formatted_time('10', '15') -> '10:15'
formatted_time('05', '30') -> '05:30'
formatted_time('20', '00') -> '20:00'

Theory
formatted_time
1. String Concatenation: The ability to combine multiple strings into a single string. Example:
year = '2022'
day = '364'
result = year + '-' + day
print(result)  # Output: '2022-364'
2. String Formatting: The ability to create formatted strings by inserting values into specific placeholders. Example:
year = '2022'
day = '364'
result = '{}-{}'.format(year, day)
print(result)  # Output: '2022-364'
year = '2030'
day = '1'
result = '{0}-{1}'.format(year, day)
print(result)  # Output: '2030-1'
3. String Operations: Performing operations on strings to manipulate or extract information. Example:
year = '2022'
day = '364'
result = year + '-' + day
print(result)  # Output: '2022-364'
year = '2030'
day = '1'
result = f'{year}-{day}'
print(result)  # Output: '2030-1'
These concepts will be useful in combining the hour and minute values into a single string with the desired format. By utilizing these techniques, you can implement the formatted_time function to solve the problem.

Hint
formatted_time
1. Use string concatenation to combine the 'hour' and 'minute' values.
2. Separate the 'hour' and 'minute' values with a colon (:) to form the desired format.
3. Return the combined string as the formatted time.
"""
# My Code
	def formatted_time(hour: str, minute: str) -> str:
	    return f"{hour}:{minute}"
	
# Solution
	def formatted_time(hour: str, minute: str) -> str:
		return hour + ":" + minute

# IA's Solutions
	




# https://www.codingdors.com/problem/253
"""
full_name
Show Solution
Given two strings 'firstName' and 'lastName', return a new string with the full name.
Hint: the full name should be in the format 'firstName lastName'
full_name('John', 'Doe') -> 'John Doe'
full_name('Emma', 'Watson') -> 'Emma Watson'
full_name('Elon', 'Musk') -> 'Elon Musk'

Theory
full_name
1. String Indexing: The ability to access individual characters within a string using their positions (indices). Example:
name = 'John'
first_letter = name[0]
print(first_letter)  # Output: 'J'
2. String Concatenation: The ability to combine multiple strings into a single string. Example:
first_name = 'John'
last_name = 'Doe'
full_name = first_name + last_name
print(full_name)  # Output: 'JohnDoe'
3. String Formatting: The ability to create formatted strings by inserting values into specific placeholders. Example:
first_name = 'John'
last_name = 'Doe'
formatted_name = '{}.{}'.format(first_name[0], last_name[0])
print(formatted_name)  # Output: 'J.D.'
first_name = 'Emma'
last_name = 'Watson'
formatted_name = '{0}.{1}'.format(first_name[0], last_name[0])
print(formatted_name)  # Output: 'E.W.'
4. String Operations: Performing operations on strings to manipulate or extract information. Example:
first_name = 'Elon'
last_name = 'Musk'
initials = first_name[0] + '.' + last_name[0] + '.'
print(initials)  # Output: 'E.M.'
first_name = 'John'
last_name = 'Doe'
initials = f'{first_name[0]}.{last_name[0]}.'
print(initials)  # Output: 'J.D.'
These concepts will be useful in combining the first name and last name into a single string with the desired format. By utilizing these techniques, you can implement the full_name function to solve the problem.

Hint
full_name
1. Use string concatenation to combine the 'firstName' and 'lastName' values.
2. Separate the 'firstName' and 'lastName' values with a space to form the desired format.
3. Return the combined string as the full name.
"""
# My Code
	def full_name(firstName: str, lastName: str) -> str:
	    return f"{firstName} {lastName}"
	
# Solution
	def full_name(firstName: str, lastName: str) -> str:
		return firstName + " " + lastName
	
# IA's Solutions
	




# https://www.codingdors.com/problem/254
"""
year_day
Show Solution
Given two strings 'day' and 'year', return a new string with the year and day of the year.
Hint: the output should be in the format 'year-day'
year_day('364', '2022') -> '2022-364'
year_day('1', '2030') -> '2030-1'
year_day('123', '2021') -> '2021-123'

Theory
year_day
1. String Concatenation: The ability to combine multiple strings into a single string. Example:
year = '2022'
day = '364'
result = year + '-' + day
print(result)  # Output: '2022-364'
2. String Formatting: The ability to create formatted strings by inserting values into specific placeholders. Example:
year = '2022'
day = '364'
result = '{}-{}'.format(year, day)
print(result)  # Output: '2022-364'
year = '2030'
day = '1'
result = '{0}-{1}'.format(year, day)
print(result)  # Output: '2030-1'
3. String Operations: Performing operations on strings to manipulate or extract information. Example:
year = '2022'
day = '364'
result = year + '-' + day
print(result)  # Output: '2022-364'
year = '2030'
day = '1'
result = f'{year}-{day}'
print(result)  # Output: '2030-1'
These concepts will be useful in combining the year and day values into a single string with the desired format. By utilizing these techniques, you can implement the year_day function to solve the problem.

Hint
year_day
1. Use string concatenation to combine the 'year' and 'day' values.
2. Separate the 'year' and 'day' values with a hyphen (-) to form the desired format.
3. Return the combined string as the year and day of the year.
"""
# My Code
	def year_day(day: str, year: str) -> str:
	    return f"{year}-{day}"
	
# Solution
	def year_day(day: str, year: str) -> str:
		return year + "-" + day
	
# IA's Solutions
	




# https://www.codingdors.com/problem/255
"""
initials
Show Solution
Write a function that takes two string parameters, 'firstName' and 'lastName'. The function should return a string that displays the initial of the first and last name.
Hint: The output should be in the format 'F.L.' where F is the first letter of firstName and L is the first letter of lastName.
initials('John', 'Doe') -> 'J.D.'
initials('Emma', 'Watson') -> 'E.W.'
initials('Elon', 'Musk') -> 'E.M.'

Theory
initials
1. String Indexing: The ability to access individual characters within a string using their positions (indices). Example:
name = 'John'
first_letter = name[0]
print(first_letter)  # Output: 'J'

2. String Concatenation: The ability to combine multiple strings into a single string. Example:
first_name = 'John'
last_name = 'Doe'
full_name = first_name + last_name
print(full_name)  # Output: 'JohnDoe'

3. String Formatting: The ability to create formatted strings by inserting values into specific placeholders. Example:
first_name = 'John'
last_name = 'Doe'
formatted_name = '{}.{}'.format(first_name[0], last_name[0])
print(formatted_name)  # Output: 'J.D.'
first_name = 'Emma'
last_name = 'Watson'
formatted_name = '{0}.{1}'.format(first_name[0], last_name[0])
print(formatted_name)  # Output: 'E.W.'

4. String Operations: Performing operations on strings to manipulate or extract information. Example:
first_name = 'Elon'
last_name = 'Musk'
initials = first_name[0] + '.' + last_name[0] + '.'
print(initials)  # Output: 'E.M.'

first_name = 'John'
last_name = 'Doe'
initials = f'{first_name[0]}.{last_name[0]}.'
print(initials)  # Output: 'J.D.'
These concepts will be useful in extracting the first letters of the first name and last name, and combining them to form the initials. By leveraging these techniques, you can implement the initials function to solve the problem.

Hint
initials
1. Access the first letter of the 'firstName' and 'lastName' strings.
2. Combine the first letters using string concatenation.
3. Separate the initials with a period (.) to form the desired format.
4. Return the combined string as the initials.
"""
# My Code
	def initials(firstName: str, lastName: str) -> str:
	    return f"{firstName[0]}.{lastName[0]}."
	
# Solution
	def initials(firstName: str, lastName: str) -> str:
		initialFirst = firstName[0]
		initialLast = lastName[0]
		return initialFirst + '.' + initialLast + '.'
	
# IA's Solutions
	




# https://www.codingdors.com/problem/256
"""
get_extension
Show Solution
Write a function get_extension() that accepts a file name as a string and returns the file extension. The file name will always have an extension and will not contain any spaces.
Hint: all the extensions will end with a dot (.) and 3 letters.
get_extension('image.jpg') -> 'jpg'
get_extension('document.pdf') -> 'pdf'
get_extension('hello.txt') -> 'txt'

Theory
get_extension
1. The ability to extract a portion of a string using start and end indices. Example:
file_name = 'image.jpg'
extension = file_name[6:9]
print(extension)  # Output: 'jpg'
file_name = 'document.pdf'
name = file_name[:8]
print(name)  # Output: 'document'
2. Performing operations on strings to modify, concatenate, or extract information. Example:
file_name = 'hello.txt'
uppercase_name = file_name.upper()
print(uppercase_name)  # Output: 'HELLO.TXT'
file_name = 'image.jpg'
parts = file_name.split('.')
extension = parts[-1]  # Get the last item in the parts list
print(extension)  # Output: 'jpg'
These concepts will be useful in extracting the file extension from the given file name. By combining these techniques, you can solve the problem by implementing the get_extension function.

Hint
get_extension
1. Find the position of the dot (.) character in the file name.
2. Extract the substring from the position of the dot (.) character to the end of the file name.
3. Remove the dot (.) from the extracted substring to get the file extension.
4. Return the file extension as the result.
"""
# My Code
	def get_extension(file: str) -> str:
	    return file[-3:]
	
# Solution
	def get_extension(file: str) -> str:
		extension = file[len(file)-3:]
		return extension
	
# IA's Solutions
	




# https://www.codingdors.com/problem/18
"""
missing_chars
Show Solution
Write a Python function that takes a string 's' and two integers 'a' and 'b', and returns a new string where the character at index 'a' and the character at index 'b' have been removed.  For example, if the string 's' is 'hello' and 'a' is 1 and 'b' is 3, the function should return the string 'hlo', where the characters at indices 1 and 3 (i.e. 'e' and 'l') have been removed.
missing_chars('hello', 1, 3) -> 'hlo'
missing_chars('coding', 0, 4) -> 'odig'

Theory
missing_chars
1. Strings in Python are arrays of bytes representing Unicode characters. Strings are immutable, meaning they cannot be changed once they are created. Example: 
string = "hello"
2. Indexing in Python starts from 0. We can access an element in a string using its index. Example: 
print(string[1])
3. Slicing in Python refers to extracting a specific part of a string. We can extract a substring from a string using slicing. Example: 
print(string[1:4])
4. Concatenation in Python is the process of joining two or more strings together to create a new string. Example: 
string1 = "world"
new_string = string + " " + string1
5. To remove a character from a string, we can create a new string without the character by concatenating the parts of the original string before and after the character. Example: 
new_string = string[:index] + string[index+1:]

Hint
missing_chars
1. You can use string slicing to remove the characters at the given indices. 
2. Remember that Python starts counting the index from 0.
3. You can concatenate the left and right parts of the string.
"""
# My Code
	def missing_chars(s: str,a: int,b: int)-> str:
	    first = s[:a] 
	    mid = s[a+1:b]
	    end = s[b+1:]
	    return first+mid+end
	
# Solution
	def missing_chars(s: str,a: int,b: int)-> str:
	    first = s[0:a]
	    middle = s[a+1:b]
	    last = s[b+1:]
	    return first + middle + last
	
# IA's Solutions
	




# https://www.codingdors.com/problem/19
"""
front_back
Show Solution
Given a string 's', return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'

Theory
front_back
1. String slicing: A string can be sliced using square brackets to select a specific subset of characters. 
s[0:3]
 returns the characters starting from the first index up to, but not including, the third index. 
s[-3:]
 returns the last three characters in the string.
2. String concatenation: Two strings can be concatenated using the + operator. 
"hello " + "world"
 returns the string "hello world".
3. String indexing: The individual characters of a string can be accessed using their indices. 
s[2]
 returns the third character in the string.
4. String length: The length of a string can be calculated using the len() function. 
len(s)
 returns the number of characters in the string.
Example:
s = "hello world"
first_char = s[0]
last_char = s[-1]
new_string = last_char + s[1:-1] + first_char
print(new_string)
Output:
dello worlh

Hint
front_back
1. The length of the string should be checked first. 
2. If the length is one or less, return the original string. 
3. Otherwise, swap the first and last characters of the string.
"""
# My Code
	def front_back(s: str)-> str:
	    tamanho = len(s)
	    first = s[0]
	    mid = s[1:-1]
	    end = s[-1]
	    return end+mid+first

# Solution
	def front_back(s: str)-> str:
	    first = s[0]
	    last = s[-1]
	    middle = s[1:-1]
	    return last + middle + first

# IA's Solutions
	




# https://www.codingdors.com/problem/
"""

"""
# My Code

# Solution

# IA's Solutions
