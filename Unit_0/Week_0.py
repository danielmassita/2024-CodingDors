"""
CODING DORS
UNIT 0 - FUNCTIONS AND VARIABLES - https://cs50.harvard.edu/python/2022/notes/0/
WEEK 0 - Functions, Variables - https://www.codingdors.com/week/0
"""

# https://www.codingdors.com/problem/279
"""
return_two
Show Solution
This is a problem to get you started on CodingDors. 

On the second line, write 'return 2' (without the single quotes) and click on Run.

Remember do not use print! All our problems require a return at the end of it.

Theory
return_two
The return statement in Python is used to exit a function and return a value. 

If there is no expression in the statement or the return statement itself is not present inside a function, then the function will return the None object. For this problem, you need to return a specific integer.

Here's an example of using the return statement:

def return_two():
    return 2

Hint
return_two
The problem statement is asking for a function that always returns the integer 2, regardless of any other factors. Therefore, you don't have to consider any input or conditions in your function. 

All you need to do is to use the return statement to return the number 2. 

The return statement is used to exit a function and return a value. In this case, the value you need to return is 2.

The structure of the function would be like this:

def return_n():
    return 2

You just need to replace the function_name with return_two and add the return statement inside the function.
"""
# My Code
def return_two() -> int:
    return 2
  
# Solution
return_two():
    return 2

# IA's Solutions
def return_two_another_way() -> int:
    result = 2
    return result
# In this alternative solution, we assign the value 2 to a variable `result` and then return the value of `result`. This achieves the same outcome as the original solution by directly returning the integer 2.





# https://www.codingdors.com/problem/280
"""
return_n
Show Solution
Write a function that takes one argument called 'n' and always returns n back.

An argument is a fancy programming word for an input. In the background we are sending different inputs to check if the code you wrote is correct.

For example,  

If the inputs is 2, we expect 2 back. If you don't understand check the "Show Solution" button.

Theory
return_n
In Python, we define a function using the def keyword. The function takes the form def function_name(parameters):. In this case, your function will take one parameter, which we'll call n.

Here's an example of a function definition with one parameter:

def return_n(n):
    return n

This function takes one parameter, n, and returns it.

In the context of functions, a parameter is a variable listed inside the parentheses in the function definition, while an argument is the value that is sent to the function when it is called. In this case, n is a parameter of your function, and when you call your function with a specific value, that value is the argument.

Here's an example of calling the print_number function with an argument:

return_n(5)

In this case, 5 is the argument that we're passing to the return_n function.

The return statement is used in a function to send a result back to where the function was called. If a function does not have a return statement, it will return None by default.

Hint
return_n
1. Function Definition: Your first task is to define a function. Python provides the def keyword to define a function. As per the problem statement, your function should be named return_n, and it should take one argument, which we'll call n.

2. Using Parameters: After defining the function, remember that n is a parameter of your function. This n will take the value of whatever is passed as an argument when the function is called.

3. Return Statement: To complete the functionality of your function, you need to return n. Python provides the return keyword to do this. You should place this keyword in the body of your function, followed by the variable you want to return.
"""
# My Code
def return_n(n: int) -> int:
    return n
  
# Solution
return_n(n: int) -> int:
    return n

# IA's Solutions
def return_n(n):
    return n
# In this alternative solution, the function `return_n` takes one argument `n` and simply returns it back. The `-> int` in the original code specifies that the function should return an integer value. However, in Python, you can omit the type annotations as shown in this alternative solution. The function works the same way as the original code, taking an input `n` and returning it back.





# 
