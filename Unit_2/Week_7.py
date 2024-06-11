"""
CODING DORS
UNIT 2 - LOOPS - https://cs50.harvard.edu/python/2022/notes/2/
WEEK 7 - Lists 2 - https://www.codingdors.com/week/7
"""





# https://www.codingdors.com/problem/81
"""
print_to_n_for_loop
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all numbers from 0 to n inclusive, using a for loop.
print_to_n_for_loop(5) -> [0, 1, 2, 3, 4, 5]
print_to_n_for_loop(3) -> [0, 1, 2, 3]
print_to_n_for_loop(1) -> [0, 1]

Theory
print_to_n_for_loop
1. For loop: A loop is a programming structure that repeats a block of code until a specific condition is met. 'for' loop is used to iterate over a sequence or until a certain condition is met. Example: 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
2. List: A list is a collection of values that are ordered and changeable. Lists are one of the most commonly used data types in Python. Example:
my_list = ["apple", "banana", "cherry"]
print(my_list)
3. Function: A function is a set of instructions that performs a specific task. Functions help break our program into smaller and modular chunks.  Example:
def my_function():
  print("Hello from a function")
my_function()
4. Range: 'range()' is a built-in function in python used to generate a sequence of numbers. It is often used with 'for' loop to iterate over the sequence.  Example:
for i in range(3):
    print(i)
Output:
0
1
2
5. List append: The 'append()' method is used to add elements to the end of a list. Example:
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)
Output:
['apple', 'banana', 'cherry', 'orange']

Hint
print_to_n_for_loop
1. Start by defining a function called "print_to_n_for_loop" that takes in a single parameter, n. 
2. Create an empty list inside the function to store the numbers. 
3. Use a for loop to iterate from 0 to n (inclusive). 
4. Append each number to the list inside the loop. 
5. Return the list at the end of the function.
"""
# My Code
  def print_to_n_for_loop(n: int):
      listinha = []
      for cada in range(0, n+1): # Começa index 0, e vai até n incluso = N+1
          listinha.append(cada) # .append() adiciona ao final da lista
      return listinha
        
# Solution
  def print_to_n_for_loop(n: int):
  	numbers = []
  	for i in range(0, n+1):
  	  numbers.append(i)
  	return numbers

# IA's Solutions
# Alternative Solution 1: Using list comprehension
def print_to_n_for_loop(n: int):
    numbers = [i for i in range(n+1)]
    return numbers
# This solution uses list comprehension to create a list of numbers from 0 to n inclusive. It is a more concise way to achieve the same result as using a for loop.
# Alternative Solution 2: Using range directly in the return statement
def print_to_n_for_loop(n: int):
    return list(range(n+1))
# In this solution, we eliminate the need for a separate list variable by directly using the range function inside the return statement. This also makes the code more succinct and easier to understand.





# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






# https://www.codingdors.com/problem/133
"""

"""
# My Code


# Solution


# IA's Solutions






