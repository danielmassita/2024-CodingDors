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





# https://www.codingdors.com/problem/243
"""
convert_seconds
Show Solution
Given an integer 'n' that represents the minutes, return how many seconds that amount of minutes represent.

Hint: 1 minute = 60 seconds

convert_seconds(24) -> 1440
convert_seconds(59) -> 3540
convert_seconds(9) -> 540

Theory
convert_seconds
1. Float, or "floating point number" is a number, positive or negative, containing one or more decimals. For example:

x = 12.34
y = -9.87


2. Python uses the basic arithmetic operators for performing arithmetic operations. Here we are mainly interested in the multiplication operator *. For example:

x = 5
y = 4
print(x * y)  # prints 20, which is the product of x and y


3. A function is a named sequence of statements that performs a computation. You define a function with a specific name and call it using that name to use its computation. For example:

def square(n):
    return n ** 2

print(square(5))  # prints 25, which is the square of 5

Hint
convert_seconds
1. You need to create a function convert_seconds(n) that takes one argument, 'n', which represents the number of minutes.

2. Inside the function, you need to calculate the number of seconds that this amount of minutes represents. As per the hint, 1 minute equals 60 seconds. So, you need to multiply the input number by 60 to get the number of seconds.

3. Use the * operator in Python to multiply numbers.

4. After calculating the total seconds, return this result from your function. It should be an integer value.

Remember that basic arithmetic operations in Python include + for addition, - for subtraction, * for multiplication, / for division, and % for modulus operation (remainder of the division). Here, we need multiplication.

The * operator multiplies two numbers together. If both numbers are integers, it returns an integer. If at least one of them is a float, it returns a float. In this case, you are multiplying two integers so the result will be an integer.
"""
# My Code
def convert_seconds(n: int)->int:
    minutes = n
    seconds = (n*60)
    return seconds
    
# Solution
def convert_seconds(n: int)->int:
	return n * 60

# IA's Solutions
# 1. Using a one-liner with inline calculation:
def convert_seconds(n: int) -> int:
    return n * 60

# 2. Using a variable for clarity:
def convert_seconds(n: int) -> int:
    minutes = n
    seconds = minutes * 60
    return seconds

# 3. Using a lambda function:
convert_seconds = lambda n: n * 60





# https://www.codingdors.com/problem/250
"""
convert_lb_to_kg
Show Solution
Given a float 'n' that represents the weight in pounds (lb), return the weight converted to kilograms (kg).

Hint: 1 kg = lb * 0.453592

convert_lb_to_kg(10) -> 4.54
convert_lb_to_kg(180) -> 81.65
convert_lb_to_kg(220) -> 99.79

Theory
convert_lb_to_kg
1. Float, or "floating point number" is a number, positive or negative, containing one or more decimals. For example:

x = 12.34
y = -9.87


2. Python uses the basic arithmetic operators for performing arithmetic operations. Here we are mainly interested in the multiplication operator *. For example:

x = 5
y = 4
print(x * y)  # prints 20, which is the product of x and y


3. A function is a named sequence of statements that performs a computation. You define a function with a specific name and call it using that name to use its computation. For example:

def square(n):
    return n ** 2

print(square(5))  # prints 25, which is the square of 5


To solve the given problem, you would need to define a function that takes a single float argument (the weight in pounds), performs a multiplication operation on this argument using the provided conversion factor, and then returns the result. The returned result would be a floating-point number representing the equivalent weight in kilograms.

Hint
convert_lb_to_kg
1. You need to create a function convert_lb_to_kg(n) that takes one argument, 'n', which represents the weight in pounds.

2. Inside the function, you need to convert the 'n' from pounds to kilograms. You can do this by multiplying 'n' by 0.453592.

3. Remember to return the result, the weight in kilograms, which should be of float data type.

Keep in mind that you are expected to use multiplication operation to convert pounds to kilograms. The multiplication operator in Python is *.

The returned result should be rounded to two decimal places. Python's built-in round() function can help with this - round(number, digits). This function rounds a number to a certain number of decimal places, specified by the 'digits' argument.
"""
# My Code
def convert_lb_to_kg(lb: int)->float:
    libras = lb
    kilogramas = 0.453592 * libras
    return round(kilogramas, 2)
    
# Solution
def convert_lb_to_kg(lb: int)->float:
	return lb * 0.453592

# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here is an alternative solution in Python that achieves the same result:
def convert_lb_to_kg(lb: float) -> float:
    kilograms = lb * 0.453592
    return round(kilograms, 2)
# In this solution, we directly multiply the input weight in pounds by the conversion factor to obtain the weight in kilograms. The `round()` function is used to round the result to 2 decimal places, which ensures the output is a float with two decimal digits.
# Both solutions are correct and will produce the expected results.





# 
