"""
CODING DORS
UNIT 1 - CONDITIONALS - https://cs50.harvard.edu/python/2022/notes/1/
WEEK 3 - Conditionals 2 - https://www.codingdors.com/week/3
"""





# https://www.codingdors.com/problem/11
"""
should_take_umbrella
Show Solution
The parameter 'is_raining' is True if it is raining, and the parameter 'is_sunny' is True if we have a sunny day. We should take an umbrella if it is not sunny or it is raining. Return True if we should take an umbrella.
should_take_umbrella(False, False) → False
should_take_umbrella(True, False) → True
should_take_umbrella(False, True) → False

Theory
should_take_umbrella
1. Boolean Operators - Boolean operations in Python are used to compare values for logical expressions. They are often used in conditional statements, loops, and functions to determine the behavior of the program based on certain conditions. Example: 
True and False
will evaluate to False.
2. If-Else Statements - If-else statements are used in Python to execute a block of code conditionally, based on whether a certain condition is true or false. Example: 
   if x % 2 == 0:
       print("Even")
   else:
       print("Odd")
3. Logical Operators - Logical operators are used in Python to combine two or more conditions to form a complex expression. There are three logical operators in Python: and, or, and not. Example: 
x > 5 and y < 10
will evaluate to true if x is greater than 5 and y is less than 10.
4. Functions - Functions in Python are blocks of reusable code that can be called with different sets of parameters and arguments. They are used to make the code more modular and easier to read, debug and maintain. Example: 
   def add_numbers(x, y):
       z = x + y
       return z
5. Variables - Variables in Python are used to store and manipulate data. They can hold different types of values such as number, string, list, dictionary, etc. Variable names are case sensitive and can contain letters, numbers, and underscores. Example: 
x = 5
will assign the value 5 to the variable x.

Hint
should_take_umbrella
Think about the conditions for when we should take an umbrella.
"""
# My Code
def should_take_umbrella(is_raining: bool, is_sunny: bool)->bool:
	# is_raining ? true / false
	# is_sunny ? true / false
	# take_umbrella ? if not sunny OR if is raining
  if is_raining == True:
    return True
  elif is_sunny == False:
    return True
  else:
    return False
    
# Solution
def should_take_umbrella(is_raining: bool, is_sunny: bool)->bool:
    if is_raining == True or is_sunny == False:
        return True
    else:
        return False

# IA's Solutions
def should_take_umbrella(is_raining: bool, is_sunny: bool) -> bool:
  return not is_sunny or is_raining

def should_take_umbrella(is_raining: bool, is_sunny: bool) -> bool:
  if is_raining or not is_sunny:
      return True
  else:
      return False

def should_take_umbrella(is_raining: bool, is_sunny: bool) -> bool:
  return True if not is_sunny or is_raining else False





# https://www.codingdors.com/problem/
"""

"""
# My Code
  
# Solution





# https://www.codingdors.com/problem/
"""

"""
# My Code
  
# Solution





# https://www.codingdors.com/problem/
"""

"""
# My Code
  
# Solution






# https://www.codingdors.com/problem/
"""

"""
# My Code
  
# Solution








