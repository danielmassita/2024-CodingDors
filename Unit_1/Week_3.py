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





# https://www.codingdors.com/problem/12
"""
team_trouble
Show Solution
Suppose we have a team of employees, and the parameters 'employee_a' and 'employee_b' indicate if each employee is present or absent from work. We are in trouble if both employees are absent or if both employees are present. Write a function to return True if we are in trouble.
team_trouble(False, False) → True
team_trouble(True, False) → False
team_trouble(True, True) → True

Theory
team_trouble
1. Boolean operators: Boolean operators are used to combine multiple conditions and evaluate if the resulting expression is True or False. The common boolean operators are 'and', 'or', and 'not'. 
Example: 
x = 10
y = 5
if x > 5 and y < 8:
    print("Both conditions are True")
2. If statement: The 'if' statement is used to test a condition and execute a block of code only if the condition is True. Example: 
x = 5
if x > 3:
    print("x is greater than 3")
3. Function definition: Functions are reusable blocks of code that perform specific tasks. They are defined using the 'def' keyword followed by the function name and parameters. Example: 
def add_numbers(x, y):
    sum = x + y
    return sum
4. Comparison operators: Comparison operators are used to compare two values and determine if they are equal, not equal, greater than, less than, greater than or equal to, or less than or equal to. The common comparison operators are '==', '!=', '>', '<', '>=', and '<='. Example: 
x = 5
y = 7
if x < y:
    print("x is less than y")

Hint
team_trouble
1. Focus on the two scenarios where we are in trouble: both employees are absent or both employees are present. 
2. Remember that the function should return True if we are in trouble. 
3. Consider using logical operators to check if both employees are absent or present. 
4. Think about the input parameters and how they can be used in the function to determine if we are in trouble or not.
"""
# My Code
def team_trouble(employee_a: bool, employee_b: bool)-> bool:
	# True trouble IF True emp_a AND True emp_b
	# IF A == B (tru, true) or (false, false) .:. True Trouble
	return True if employee_a == employee_b else False

# Solution
def team_trouble(employee_a: bool, employee_b: bool)-> bool:
  if employee_a == True and employee_b == True:
    return True
  elif employee_a == False and employee_b == False:
    return True
  else:
    return False





# https://www.codingdors.com/problem/13
"""
sum_or_half_sum
Show Solution
Write a Python function that takes two input integers 'a' and 'b', and returns their sum unless the two values are the same, in which case it should return half of their sum. For instance, if 'a' is 4 and 'b' is 5, the function should return 9. If 'a' and 'b' are both 3, the function should return 3.
sum_or_half_sum(4, 5) -> 9
sum_or_half_sum(3, 3) -> 3


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








