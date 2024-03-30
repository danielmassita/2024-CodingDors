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





# https://www.codingdors.com/problem/246
"""
convert_fahrenheit_to_celsius
Show Solution
Given a float 'n' that represents the temperature in Fahrenheit, return the temperature converted to Celsius.

Hint: 1 Celsius = (Fahrenheit - 32) * 5/9

convert_fahrenheit_to_celsius(212) -> 100.0
convert_fahrenheit_to_celsius(194) -> 90.0
convert_fahrenheit_to_celsius(302) -> 150.0

Theory
convert_fahrenheit_to_celsius
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
convert_fahrenheit_to_celsius
1. You need to create a function convert_fahrenheit_to_celsius(n) that takes one argument, 'n', which represents the temperature in Fahrenheit.

2. Inside the function, you need to convert 'n' from Fahrenheit to Celsius. As per the hint provided, you can do this by subtracting 32 from 'n' and then multiplying the result by 5/9.

3. Remember to return the result which is the temperature in Celsius, and this should be of float data type.

Keep in mind that Python uses the standard arithmetic operators (+, -, *, /) for addition, subtraction, multiplication, and division respectively. The parentheses are used to change the precedence of the operations, ensuring the subtraction occurs before the multiplication and division.

The returned result should be rounded to one decimal place. Python's built-in round() function can be used for this purpose.
"""
# My Code
def convert_fahrenheit_to_celsius(n: float) -> float:
    fahrenheit = n
    celsius = (fahrenheit - 32)*5/9
    return celsius
	
# Solution
def convert_fahrenheit_to_celsius(n: float) -> float:
	return (n - 32) * 5/9
	
# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are a few alternative solutions in Python for converting Fahrenheit to Celsius:
# 1. Using a lambda function:
convert_fahrenheit_to_celsius = lambda n: (n - 32) * 5/9
# Using a lambda function is a more concise way to define a simple function like this. It takes a single parameter 'n' and returns the converted temperature in Celsius.

# 2. Using a one-liner function:
def convert_fahrenheit_to_celsius(n: float) -> float: return (n - 32) * 5/9
# This is another more concise way to define the function in a single line. It directly returns the converted temperature in Celsius without assigning variables.

# 3. Adding docstring for better documentation:
def convert_fahrenheit_to_celsius(n: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
    n (float): Temperature in Fahrenheit
    
    Returns:
    float: Temperature converted to Celsius
    """
    return (n - 32) * 5/9
# Adding a docstring to the function provides meaningful information about its purpose, parameters, and return value, making the function more self-explanatory and easier to understand for others.





# https://www.codingdors.com/problem/247
"""
convert_celsius_to_kelvin
Show Solution
Given a float 'n' that represents the temperature in Celsius, return the temperature converted to Kelvin.

Hint: 1 Kelvin = Celsius + 273.15

convert_celsius_to_kelvin(100) -> 373.15
convert_celsius_to_kelvin(170) -> 443.15
convert_celsius_to_kelvin(50) -> 323.15

Theory
convert_celsius_to_kelvin
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
convert_celsius_to_kelvin
1. You need to create a function convert_celsius_to_kelvin(n) that takes one argument, 'n', which represents the temperature in Celsius.

2. Inside the function, you need to convert 'n' from Celsius to Kelvin. As per the hint provided, you can do this by adding 273.15 to 'n'.

3. Remember to return the result which is the temperature in Kelvin, and it should be of float data type.

Take into account that Python uses the standard arithmetic operators (+, -, *, /) for addition, subtraction, multiplication, and division respectively.

The returned result should be rounded to two decimal places. You can use Python's built-in round() function to achieve this - round(number, digits). This function rounds a number to a specified number of decimal places, as indicated by the 'digits' argument.
"""
# My Code
def convert_celsius_to_kelvin(n: int)->float:
    kelvin = (n + 273.15)
    return kelvin
	
# Solution
def convert_celsius_to_kelvin(n: int)->float:
	return n + 273.15

# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here is an alternative solution using a lambda function in Python:
convert_celsius_to_kelvin = lambda n: n + 273.15
# In this solution, we define a lambda function called `convert_celsius_to_kelvin` that takes a parameter `n` representing the temperature in Celsius and returns the temperature converted to Kelvin by adding 273.15. Lambda functions are anonymous functions that can have any number of arguments but only one expression.
# Both the original solution and this alternative solution achieve the same result of converting Celsius to Kelvin.





# 
"""
calculate_average
Show Solution
Given 3 integers 'n1', 'n2' and 'n3', return the average of those 3 numbers.

calculate_average(5, 10, 15) -> 10.00
calculate_average(1, 1, 7) -> 3.00
calculate_average(-1, -5, -9) -> - 3.00

Theory
calculate_average
1. Variables are used to store data in Python. They are created by assigning a value to them. Example:

x = 10  # x is of type int
y = 20.5  # y is of type float
z = "OpenAI"  # z is of type str


2. An integer is a whole number, positive or negative, without decimals, of unlimited length. Example:

x = 10
y = -5


3. Python uses the basic arithmetic operators for performing arithmetic operations. For this problem, you'll need the addition operator (+) and division operator (/). Example:

x = 10
y = 5

print(x + y)  # prints 15, sum of x and y
print(x / y)  # prints 2.0, quotient of x and y


4. Functions: Functions in Python are blocks of reusable code that perform a specific task. You define a function using the def keyword, followed by the function name, a pair of parentheses which may enclose some parameters, and a colon. The code block within every function is indented. Examples:

def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(3, 5))  # prints 8, the sum of 3 and 5


To solve the given problem, you need to define a function that takes three integer arguments (n1, n2, n3), adds these three numbers together, divides the sum by 3 to compute the average, and then returns the average. The function will return a float representing the average of the three numbers.

Hint
calculate_average
1. You need to create a function calculate_average(n1, n2, n3) that takes three arguments, 'n1', 'n2', and 'n3', which represent the numbers for which we want to calculate the average.

2. Inside the function, you need to calculate the average of the three numbers. You can do this by adding all the numbers together and then dividing the sum by the number of elements, which is 3 in this case.

3. Remember to return the result which is the average of the numbers, and it should be of float data type.

In Python, you use the standard arithmetic operators (+, -, *, /) for addition, subtraction, multiplication, and division respectively.

The returned result should be rounded to two decimal places. You can use Python's built-in round() function to achieve this - round(number, digits). This function rounds a number to a certain number of decimal places, specified by the 'digits' argument.
"""
# My Code
def calculate_average(n1: int, n2: int, n3:int)->float:
    average = (n1 + n2 + n3)/3
    return average

# Solution
def calculate_average(n1: int, n2: int, n3:int)->float:
	return (n1 + n2 + n3)/3
	
# IA's Solution
# Congrats, your answer is correct!
# Sure! Here are two alternative solutions in Python with explanations:
# 1. Using the mean function from the statistics module:
import statistics
def calculate_average(n1: int, n2: int, n3: int) -> float:
    average = statistics.mean([n1, n2, n3])
    return round(average, 2)
# In this solution, we use the mean function from the statistics module to calculate the average of the three numbers. We then round the result to two decimal places using the round function.

# 2. Calculating the average manually without using any external modules:
def calculate_average(n1: int, n2: int, n3: int) -> float:
    average = (n1 + n2 + n3) / 3
    return round(average, 2)
# In this solution, we manually calculate the average of the three numbers by adding them together and dividing by 3. We then round the result to two decimal places using the round function.
# Both of these alternatives will give you the same result as your original solution, but they show different ways to calculate the average of three numbers in Python.





# https://www.codingdors.com/problem/242
"""
volume_of_cylinder
Show Solution
Given an integer 'height' and an integer 'diameter', return the volume of a cylinder given its height and diameter. The volume will be in a format of a float.

Hint: the formula to calculate the volume of a cylinder is 3.14 * (diameter/2)^2 * height.

volume_of_cylinder(10, 4) -> 125.6
volume_of_cylinder(5, 2) -> 15.70
volume_of_cylinder(7, 4) -> 87.92

Theory
volume_of_cylinder
1. Variables in Python are containers for storing data values. They are created by assigning a value to them. Python is dynamically-typed, meaning that you don’t need to specify the data type of a variable when declaring one. Example:

x = 10  # x is of type int
y = 20.5  # y is of type float
z = "OpenAI"  # z is of type str


2. In Python, an integer is a whole number, positive or negative, without decimals, of unlimited length. Example:

x = 10
y = -5


3. Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Example:

x = 10.5
y = -5.6


4. Python has several arithmetic operators that you can use to perform mathematical operations like addition, subtraction, multiplication, division, etc. Example:

x = 10
y = 5

print(x + y)  # prints 15, sum of x and y
print(x - y)  # prints 5, difference of x and y
print(x * y)  # prints 50, product of x and y
print(x / y)  # prints 2.0, quotient of x and y


5. Python uses the ** operator for exponentiation. For example, 2 ** 3 returns 8. Another example:

x = 2
y = 3

print(x ** y)  # prints 8, 2 to the power of 3


6. A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # prints "Hello, Alice!"

Hint
volume_of_cylinder
1. You need to create a function volume_of_cylinder(height, diameter) that takes two arguments - 'height' and 'diameter', which represent the height and diameter of a cylinder, respectively.

2. Inside the function, you need to calculate the volume of the cylinder. As per the hint, the formula to calculate the volume of a cylinder is 3.14 * (diameter/2)^2 * height. In Python, you can use the * operator to perform multiplication, the / operator to perform division, and the ** operator to perform exponentiation.

3. After calculating the volume, return this result from your function. It should be a float value. In Python, dividing two integers using the / operator always results in a float.

Note: Python's precedence of arithmetic operators is like standard mathematics. Exponentiation is done first, then multiplication and division (from left to right), and finally addition and subtraction (from left to right). Parentheses can be used to force certain parts of an expression to be evaluated before others, and they can make the expression easier to read and understand.
"""
# My Code
def volume_of_cylinder(height: int, diameter: int)->float:
    volume = (3.14 * ((diameter/2)**2 ) * height)
    return volume
# def volume_of_cylinder(height: int, diameter: int)->float:
#     volume = (3.14 * (diameter/2)^2 * height)
#     return volume
# TypeError: unsupported operand type(s) for ^: 'float' and 'int'

# Solution
def volume_of_cylinder(height: int, diameter: int)->float:
	return 3.14 * (diameter/2)**2 * height
	
# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are two alternative solutions in Python for calculating the volume of a cylinder given its height and diameter:
# Alternative Solution 1: Using math.pi constant
import math
def volume_of_cylinder(height: int, diameter: int) -> float:
    radius = diameter / 2
    volume = math.pi * (radius ** 2) * height
    return volume
# Explanation:
# - This solution uses the `math.pi` constant for a more accurate representation of the value of pi.
# - The radius is calculated as half of the diameter.
# - The volume is calculated using the formula for the volume of a cylinder: pi * (radius^2) * height.

# Alternative Solution 2: Using f-strings for formatting the result
def volume_of_cylinder(height: int, diameter: int) -> float:
    volume = 3.14 * ((diameter / 2) ** 2) * height
    return float(f'{volume:.2f}')
# Explanation:
# - This solution calculates the volume of the cylinder in the same way as the original solution but uses f-strings to format the result to two decimal places.
# - The `f'{volume:.2f}'` syntax formats the volume to two decimal places before returning it.





# https://www.codingdors.com/problem/244
"""
calculate_area_of_circle
Show Solution
Given an integer 'n' that represents the radius of a circle, return the area of the circle.

Hint: the formula to calculate the area of a circle is 3.14 * radius^2

calculate_area_of_circle(5) -> 78.5
calculate_area_of_circle(2) -> 12.56
calculate_area_of_circle(9) -> 254.34

Theory
calculate_area_of_circle
1. Variables in Python are containers for storing data values. They are created by assigning a value to them. Python is dynamically-typed, meaning that you don’t need to specify the data type of a variable when declaring one. Example:

x = 10  # x is of type int
y = 20.5  # y is of type float
z = "OpenAI"  # z is of type str


2. In Python, an integer is a whole number, positive or negative, without decimals, of unlimited length. Example:

x = 10
y = -5


3. Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Example:

x = 10.5
y = -5.6


4. Python has several arithmetic operators that you can use to perform mathematical operations like addition, subtraction, multiplication, division, etc. Example:

x = 10
y = 5

print(x + y)  # prints 15, sum of x and y
print(x - y)  # prints 5, difference of x and y
print(x * y)  # prints 50, product of x and y
print(x / y)  # prints 2.0, quotient of x and y


5. Python uses the ** operator for exponentiation. For example, 2 ** 3 returns 8. Another example:

x = 2
y = 3

print(x ** y)  # prints 8, 2 to the power of 3


6. A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # prints "Hello, Alice!"

Hint
calculate_area_of_circle
1. You need to create a function calculate_area_of_circle(n) that takes one argument, 'n', which represents the radius of the circle.

2. Inside the function, you need to calculate the area of the circle. The formula to calculate the area of a circle is π*(radius^2), and you can use 3.14 as an approximation for π.

3. To calculate the square of the radius, use the ** operator in Python. This operator raises the number on its left to the power of the number on its right.

4. Remember to return the result which is the area of the circle, and it should be of float data type.

In Python, the standard arithmetic operators (+, -, *, /, **) are used for addition, subtraction, multiplication, division, and exponentiation, respectively.

The returned result should be rounded to two decimal places. You can use Python's built-in round() function to achieve this - round(number, digits). This function rounds a number to a certain number of decimal places, specified by the 'digits' argument.
"""
# My Code
def calculate_area_of_circle(n: int)->float:
    area = (3.14 * n ** 2)
    return round(area, 2)
	
# Solution
def calculate_area_of_circle(n: int)->float:
	return 3.14 * n**2
	
# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here is an alternative solution in Python using the math module:
import math
def calculate_area_of_circle(n: int) -> float:
    area = math.pi * n ** 2
    return round(area, 2)
# In this solution, we use the `math.pi` constant provided by the math module when calculating the area of the circle. The rest of the code is similar to the original solution, but using `math.pi` instead of the hardcoded value 3.14. This solution is more accurate and avoids potential rounding errors that could occur with using a hardcoded value for pi.





# https://www.codingdors.com/problem/241
"""
calc_bmi
Show Solution
Given an integer 'weight' and an integer 'height', return the Body Mass Index (BMI) of the person. The BMI will be in a format of a float.

Hint: the formula to calculate BMI is weight / (height/100)^2.

calc_bmi(75, 180) -> 23.15
calc_bmi(90, 190) -> 24.93
calc_bmi(80, 170) -> 27.68

Theory
calc_bmi
1. Variables in Python are containers for storing data values. They are created by assigning a value to them. Python is dynamically-typed, meaning that you don’t need to specify the data type of a variable when declaring one. Example:

x = 10  # x is of type int
y = 20.5  # y is of type float
z = "OpenAI"  # z is of type str


2. In Python, an integer is a whole number, positive or negative, without decimals, of unlimited length. Example:

x = 10
y = -5


3. Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Example:

x = 10.5
y = -5.6


4. Python has several arithmetic operators that you can use to perform mathematical operations like addition, subtraction, multiplication, division, etc. Example:

x = 10
y = 5

print(x + y)  # prints 15, sum of x and y
print(x - y)  # prints 5, difference of x and y
print(x * y)  # prints 50, product of x and y
print(x / y)  # prints 2.0, quotient of x and y


5. Python uses the ** operator for exponentiation. For example, 2 ** 3 returns 8. Another example:

x = 2
y = 3

print(x ** y)  # prints 8, 2 to the power of 3


6. A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # prints "Hello, Alice!"


To solve the given problem, you'll need to define a function that takes two integer arguments (weight and height), performs some calculations using these arguments, and then returns the result. The calculations will involve using arithmetic operators and the exponentiation operator. The function will return a floating-point number, which is the Body Mass Index (BMI).

Hint
calc_bmi
1. You need to create a function calc_bmi(weight, height) that takes two arguments, 'weight' and 'height'.

2. Inside the function, you need to convert the 'height' from centimeters to meters. Since 1 meter is equal to 100 centimeters, you can do this by dividing the 'height' by 100.

3. You have to square the height in meters. Remember, Python uses ** for exponentiation.

4. After calculating the height in meters and squaring it, you divide the 'weight' by the squared height to get the Body Mass Index (BMI).

5. Remember to return the result. The BMI value should be of float data type.

Keep in mind that in Python, the division operator / always returns a float. This is convenient in this case, because the Body Mass Index is typically represented as a decimal number.
"""
# My Code
def calc_bmi(weight: int, height: int)->float:
    bmi = (weight / (height/100)**2)
    return bmi
	
# Solution
def calc_bmi(weight: int, height: int)->float:
	return weight / (height/100)**2
	
# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here is an alternative solution using type casting and division instead of exponentiation:
def calc_bmi(weight: int, height: int) -> float:
    bmi = (weight / ((height / 100) * (height / 100)))
    return bmi
# In this solution, we first convert the height to meters by dividing it by 100. Then we calculate the BMI using simple multiplication instead of exponentiation. The result will still be the same as the original solution.





# https://www.codingdors.com/problem/1
"""
return_hello
Show Solution
Given a string 's', return a new string with the word "hello" in front. 

return_hello("Gi") -> "hello Gi" 

return_hello("Leo") -> "hello Leo"

Theory
return_hello
1. Concatenation: Joining two or more strings together into one longer string using the "+" operator. 
Example: 

string1 = "hello"
string2 = "world"
new_string = string1 + string2
print(new_string) -> "hello world"


2. String interpolation: Inserting a variable into a string using {} and the ".format" method.
Example: 

name = "Gi"
greeting = "hello {}".format(name)
print(greeting) -> "hello Gi"


3. Return statement: A statement within a function that specifies the value that will be returned to the caller.
Example: 

def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(1, 2)) -> 3


4. Function parameters: Values that are passed into a function to be used within the function.
Example: 

def greet(name):
    return "hello {}".format(name)
print(greet("Leo")) -> "hello Leo"

Hint
return_hello
1. You need to use string concatenation to create the new string. 

2. The structure of the output string is "hello" followed by the input string. 

3. You can concatenate strings using the + operator. 

4. Make sure to add a space after "hello" so that the output string looks correct.
"""
# My Code
def return_hello(s: str)-> str:
    return f"hello {s}"
	
# Solution
def return_hello(s: str)-> str:
	return 'hello ' + s

# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here are a few alternative solutions in Python for the given question:

# 1. Using concatenation:
def return_hello(s: str) -> str:
    return "hello " + s
# This solution uses string concatenation to combine the word "hello" with the input string 's'.

# 2. Using format method:
def return_hello(s: str) -> str:
    return "hello {}".format(s)
# This solution uses the format method to insert the input string 's' into the placeholder {}.

# 3. Using f-string with string interpolation:
def return_hello(s: str) -> str:
    return f"hello {s}"
# This is the original solution you provided, which uses f-strings for string interpolation to insert the input string 's' into the final string.
# All of these solutions will return the same output, "hello [input string]", with variations in syntax and string manipulation techniques.





# https://www.codingdors.com/problem/2
"""
return_person_details
Show Solution
Write a Python function that takes two input strings 'name' and 'age', and returns a new string in the following format: '''name'' is ''age'''. For instance, if the name is 'Maria' and the age is 20, the function should return 'Maria is 20'.

return_person_details('Maria', 20) -> 'Maria is 20'

return_person_details('Gi', 25) -> 'Gi is 25'

Theory
return_person_details
1. String Concatenation: This operation is used to join two or more strings together into a new string. This can be achieved using the "+" operator. For example: 


name + " is " + age

will concatenate the strings 'name', ' is ', and 'age' into a new string.

2. Function Definition: Functions are blocks of code that perform a specific task. They are defined using the "def" keyword. A function takes inputs as arguments and can produce an output using the "return" statement. For example: 


def print_person_details(name, age):
    return name + " is " + age


3. String Interpolation: This operation allows us to embed values within a string. This is achieved by using placeholders in the string, which are replaced with the values of variables when the string is printed. In Python, the most common form of string interpolation is using f-strings. For example: 


f"{name} is {age}"

Hint
return_person_details
1. The function should have two parameters: 'name' and 'age'

2. The output string should have the name and age variables interpolated

3. The output string should be returned by the function.
"""
# My Code
def return_person_details(name: str,age: str)->str:
    return f"{name} is {age}"
	
# Solution
def return_person_details(name: str,age: str)->str:
    return name + " is " + age

# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are a few alternative solutions in Python with explanations:
# 1. Using string concatenation:
def return_person_details(name: str, age: str) -> str:
    return name + ' is ' + str(age)
# Explanation: In this solution, we use string concatenation to combine the input strings 'name' and 'age' along with the phrase ' is '.

# 2. Using format method:
def return_person_details(name: str, age: str) -> str:
    return '{} is {}'.format(name, age)
# Explanation: In this solution, we use the format method to insert the values of 'name' and 'age' into the specified locations within the string using curly braces {}.

# 3. Using % operator for string formatting:
def return_person_details(name: str, age: str) -> str:
    return '%s is %s' % (name, age)
# Explanation: In this solution, we use the % operator for string formatting to insert the values of 'name' and 'age' into the specified locations within the string.
# All of these alternative solutions achieve the desired outcome of creating a new string in the specified format using the input 'name' and 'age'.





# https://www.codingdors.com/problem/3
"""
title_movie
Show Solution
Write a Python function that takes a string 'movie' and returns a new string with every word in the movie name capitalized. For instance, if the movie name is 'the lord of the rings', the function should return 'The Lord Of The Rings'.

title_movie('the lord of the rings') -> 'The Lord Of The Rings'

title_movie('star wars') -> 'Star Wars'

Theory
title_movie
1. Function: A function is a block of code that performs a specific task. Example: 


def add_numbers(num1, num2): 
    return num1 + num2


2. String: A string is a sequence of characters enclosed in either single or double quotes.  Example: 


name = "John"


3. Title: Title refers to the first letter of each word will be capitalized. Example: 


text = "hello world".title() # Hello World


4. Return: The return keyword is used to exit a function and return a value. Example: 


def square(num): 
    return num*num

Hint
title_movie
You can split the input string into a list of words and then capitalize the first letter of each word using the capitalize() method. 

Then join the words back together with a space separator.
"""
# My Code
def title_movie(movie: str)-> str:
    return movie.title()
	
# Solution
def title_movie(movie: str)-> str:
    upper = movie.title()
    return upper

# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are two alternative solutions to achieve the same outcome:
# 1. Using a list comprehension to capitalize each word individually:
def title_movie(movie: str) -> str:
    return ' '.join([word.capitalize() for word in movie.split()])
# Explanation: This solution splits the input string into individual words using the `split()` method, then uses a list comprehension to capitalize each word, and finally joins the capitalized words back together using the `join()` method.

# 2. Using the `title()` method along with a lambda function:
def title_movie(movie: str) -> str:
    return ' '.join(map(lambda x: x.capitalize(), movie.split()))
# Explanation: This solution is similar to the first one, but it uses the `map()` function with a lambda function to capitalize each word in the movie name. The rest of the process is the same as in the first solution.





# https://www.codingdors.com/problem/4
"""
upper_movie
Show Solution
Write a Python function that takes a string 'movie' and returns a new string with every character in the movie name converted to uppercase. For instance, if the movie name is 'The Lord of the Rings', the function should return 'THE LORD OF THE RINGS'.

upper_movie('The Lord of the Rings') -> 'THE LORD OF THE RINGS'

upper_movie('star wars') -> 'STAR WARS'

Theory
upper_movie
1. Function: A function is a block of code that performs a specific task. Example: 


def add_numbers(num1, num2): 
    return num1 + num2


2. String: A string is a sequence of characters enclosed in either single or double quotes.  Example: 


name = "John"


3. Uppercase: Uppercase refers to the capital letters in the English alphabet - A to Z. Example: 


text = "Hello World".upper() # HELLO WORLD


4. Return: The return keyword is used to exit a function and return a value. Example: 


def square(num): 
    return num*num

Hint
upper_movie
1. Use the built-in string method to convert a string to uppercase. 
 
2. Use the parameter 'movie' as input to the function.

3. Return the uppercased string using the 'return' keyword.    
"""
# My Code
def upper_movie(movie: str)->str:
    return movie.upper()

# Solution
def upper_movie(movie: str)->str:
    final = movie.upper()
    return final

# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here are a couple of alternative solutions in Python:
# 1. Using a loop to iterate through each character in the string and convert it to uppercase:
def upper_movie(movie: str) -> str:
    uppercased = ''
    for char in movie:
        uppercased += char.upper()
    return uppercased
# This solution uses a `for` loop to iterate through each character in the input string `movie`. For each character, it converts it to uppercase using the `upper()` method and then concatenates it to the `uppercased` variable.

# 2. Using a list comprehension to convert each character to uppercase and join them back into a string:
def upper_movie(movie: str) -> str:
    return ''.join([char.upper() for char in movie])
# In this solution, a list comprehension is used to iterate through each character in the input string `movie`, convert it to uppercase using the `upper()` method, and return a list of uppercase characters. The `join` method is then used to join these characters back into a single string.
# Both of these solutions achieve the same result as your initial solution but use different methods to convert the characters to uppercase.





# https://www.codingdors.com/problem/5
"""
lower_movie
Show Solution
Write a Python function that takes a string 'movie' and returns a new string with every character in the movie name converted to lowercase. For instance, if the movie name is 'The Lord of the Rings', the function should return 'the lord of the rings'.

lower_movie('The Lord of the Rings') -> 'the lord of the rings'

lower_movie('STAR WARS') -> 'star wars'

heory
lower_movie
1. Function: A function is a block of code that performs a specific task. Example: 


def add_numbers(num1, num2): 
    return num1 + num2


2. String: A string is a sequence of characters enclosed in either single or double quotes.  Example: 


name = "John"


3. lower(): This method returns the string in lowercase letters. Example: 


text = "HELLO WORLD".lower() # hello world


4. Return: The return keyword is used to exit a function and return a value. Example: 


def square(num): 
    return num*num

Hint
lower_movie
1. Use the built-in function 
lower()
 to convert the string to lowercase. 

2. Make sure to return the new string. 

3. Take into account spaces and special characters in the movie name.

4. The function should take a string as input.
"""
# My Code
def lower_movie(movie: str)->str:
    return movie.lower()

# Solution
def lower_movie(movie: str)->str:
    result = movie.lower()
    return result

# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here is an alternative solution using a loop to iterate over each character in the movie name and convert it to lowercase:
def lower_movie(movie: str) -> str:
    converted_movie = ''
    for char in movie:
        converted_movie += char.lower()
    return converted_movie
# In this solution, we initialize an empty string `converted_movie` to store the lowercase version of the movie name. We then iterate over each character in the input `movie` using a loop and convert each character to lowercase using the `lower()` method. Finally, we concatenate the lowercase character to the `converted_movie` string. Once we have processed all characters in the `movie`, we return the final `converted_movie` string.




# https://www.codingdors.com/problem/6
"""
remove_whitespace
Show Solution
Given a string 's', return a new string without leading or trailing whitespace. 

remove_whitespace("     hi there") -> "hi there" 

remove_whitespace("hello world       ") -> "hello world"

Theory
remove_whitespace
1. String Methods: Strings in Python are objects that support a variety of built-in methods. These methods can be used for tasks such as finding substrings, converting the string to uppercase or lowercase, and removing whitespace. Example: 


s = "Hello, World!"
print(s.upper()) # outputs "HELLO, WORLD!"


2. strip(): This function returns a copy of the original string with all leading and trailing whitespace removed. Example: 


s = "  Remove whitespace  "
print(s.strip()) # outputs "Remove whitespace"


3. lstrip(): This function returns a copy of the original string with all leading whitespace removed. Example: 


s = "  Remove leading whitespace"
print(s.lstrip()) # outputs "Remove leading whitespace"


4. rstrip(): This function returns a copy of the original string with all trailing whitespace removed. Example: 


s = "Remove trailing whitespace    "
print(s.rstrip()) # outputs "Remove trailing whitespace"

Hint
remove_whitespace
- The function name suggests that you need to remove whitespace.

- Leading whitespace refers to the blank spaces at the beginning of a string.

- Trailing whitespace refers to the blank spaces at the end of a string. 

- You need to return a new string that has no leading or trailing whitespace. 

- The functions should preserve any whitespace in the middle of the string.
"""
# My Code
def remove_whitespace(s: str)->str:
    return s.strip()

# Solution
def remove_whitespace(s: str)->str:
    result = s.strip()
    return result
	
# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here are a few alternative solutions in Python:
# 1. Using regex:

import re
def remove_whitespace(s: str) -> str:
    return re.sub('^\s+|\s+$', '', s)
# Explanation: This solution uses the `re.sub()` function from the `re` module to replace leading and trailing whitespaces with an empty string.

# 2. Using slicing:
def remove_whitespace(s: str) -> str:
    start = 0
    end = len(s)
    while start < end and s[start].isspace():
        start += 1
    while end > start and s[end-1].isspace():
        end -= 1
    return s[start:end]
# Explanation: This solution manually loops through the string to find the first non-whitespace character from the start and the end, then slices the string accordingly.

# 3. Using split and join:
def remove_whitespace(s: str) -> str:
    return ' '.join(s.split()).strip()
# Explanation: This solution splits the string using whitespaces as separators, then re-joins the resulting list of words with a single space, and finally strips any remaining leading or trailing whitespace.
# All of these solutions will achieve the same result as your initial solution!




# https://www.codingdors.com/problem/7
"""
replace_words
Show Solution
Write a Python function that takes three input strings 'a', 'b', and 'c', and returns a new string obtained by replacing all occurrences of the string 'b' in the string 'a' with the string 'c'. For instance, if the string 'a' is 'the quick brown fox jumps over the lazy dog', string 'b' is 'fox', and string 'c' is 'cat', the function should return 'the quick brown cat jumps over the lazy dog'.

replace_words('the quick brown fox jumps over the lazy dog', 'fox', 'cat') -> 'the quick brown cat jumps over the lazy dog'

Theory
replace_words
1. string: A string is a sequence of characters, enclosed in either single quotes (') or double quotes ("). In Python, strings are immutable. Example:


'Hello, World!'`


2. replace(): The replace() method in Python is used to replace all occurrences of a string with another string. It takes two arguments, the first one being the string to be replaced and the second one being the string to replace it with. 


'abcdef'.replace('c', 'z') #returns 'abzdef'.


3. function: In Python, a function is a named block of code that performs a specific task. It typically takes some input, processes it, and returns some output. Functions help in modularizing code and making it reusable. An example of a Python function is:


def add(a, b):
    return a + b


4. parameters: Parameters are input variables that are defined in the function definition. They are enclosed in parentheses after the function name. They represent the values that are passed into the function when it is called. In the function definition 

def add(a, b):

, 'a' and 'b' are the parameters.

5. return: The return statement in Python is used to exit a function and return a value. It returns the value or expression provided as an argument. For example, 


def add(a, b): 
    return a + b
 
returns the sum of the two input values.

Hint
replace_words
Remember that there is a built-in string method that can be used to replace all occurrences of a substring in a string.
"""
# My Code
def replace_words(a: str,b:str,c: str)->str:
    return a.replace(b, c)
	
# Solution
def replace_words(a: str,b:str,c: str)->str:
    jump = a.replace(b, c)
    return jump

# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here are two alternative solutions to achieve the same functionality as the provided Python function using different approaches
# 1. Using string split and join:
def replace_words(a: str, b: str, c: str) -> str:
    words = a.split()  # Split the string into a list of words
    replaced_words = [word if word != b else c for word in words]  # Replace 'b' with 'c' in the words
    return " ".join(replaced_words)  # Join the list of words back into a string
# Explanation:
# - The function first splits the input string 'a' into a list of words using the `split()` method.
# - Then, it iterates through each word in the list and checks if the word is equal to the string 'b'. If it is, the word is replaced with the string 'c'.
# - Finally, the modified list of words is joined back into a string using the `join()` method with space as the separator.

# 2. Using regular expressions:
import re
def replace_words(a: str, b: str, c: str) -> str:
    return re.sub(r'\b' + re.escape(b) + r'\b', c, a)
# Explanation:
# - This solution uses the `re.sub()` function from the `re` module to perform a regular expression-based substitution.
# - The regular expression pattern `r'\b' + re.escape(b) + r'\b'` is used to match the exact word 'b' in the input string 'a'. The `\b` represents word boundaries to ensure exact matches.
# - The `re.escape()` function is used to escape special characters in the string 'b' to avoid any unintended patterns in the regular expression.
# - The `re.sub()` function replaces all occurrences of the matched word 'b' with the string 'c' in the input string 'a' and returns the modified string.
# These alternative solutions provide different ways to achieve the desired string replacement functionality in Python.





# https://www.codingdors.com/problem/8
"""
round_floats
Show Solution
Given a float 'n', return the number with only two decimal places. 

round_floats(3.141) -> 3.14 

round_floats(75.123456) -> 75.12

Theory
round_floats
1. Floats: A float is a numerical data type in Python that is capable of representing rational numbers with decimal values. 5.6 is an example of a float.

2. Rounding: Rounding a float means reducing the number of digits after the decimal point to a desired number. The round() function in Python can be used to round numbers. 

round(3.141, 2)    
 
would give 3.14

3. String formatting: String formatting is a way to format string output in a more readable and attractive way. The format() method in Python can be used for string formatting. Example:

 
"The value is {:.2f}".format(3.141) 

would give "The value is 3.14".

Hint
round_floats
1. You can use Python's built-in round() function. 

2. The round() function takes two arguments: the float you want to round, and the number of decimal places you want to round to. 

3. To round to two decimal places, you should use round(n, 2). 

4. Note that the function should return a float, not a string.
"""
# My Code
def round_floats(n: float)->float:
    return round(n, 2)
	
# Solution
def round_floats(n: float)->float:
    result = round(n, 2)
    return result
	
# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are two alternative solutions in Python with explanations:
# 1. Using string formatting:
def round_floats(n: float) -> float:
    return float(f'{n:.2f}')
# Explanation: In this approach, we use f-string formatting to format the float 'n' to two decimal places using "{n:.2f}". Then, we convert the formatted string back to a float using the float() function and return the result.

# 2. Using math module:
import math
def round_floats(n: float) -> float:
    return math.floor(n * 100) / 100
# Explanation: In this approach, we first multiply the float 'n' by 100 to shift the decimal point two places to the right. Then, we use math.floor() to round the number down to the nearest integer. Finally, we divide the result by 100 to shift the decimal point back to its original position, effectively rounding the number to two decimal places.
# Both of these alternative solutions achieve the same result as your original solution, rounding the float 'n' to two decimal places.





# https://www.codingdors.com/problem/9
"""
remove_letter_g
Show Solution
Write a Python function that takes a string 's' and returns a new string obtained by removing all occurrences of the letter 'g' from the string. For instance, if the string is 'going to the grocery store', the function should return 'oin to the rocery store'.

remove_letter_g('going to the grocery store') -> 'oin to the rocery store'

Theory
remove_letter_g
1. String Methods: Strings in Python are objects that support a variety of built-in methods. These methods can be used for tasks such as finding substrings, converting the string to uppercase or lowercase, and removing whitespace. Example: 


s = "Hello, World!"
print(s.upper()) # outputs "HELLO, WORLD!"


2. strip(): This function returns a copy of the original string with all leading and trailing whitespace removed. Example: 


s = "  Remove whitespace  "
print(s.strip()) # outputs "Remove whitespace"



s = "banana"
print(s.strip('a')) # outputs "bnn"

Hint
remove_letter_g
- The function name suggests that you need to remove the letter 'g'.

- You need to return a new string that has no letter 'g'. 

- Remember to use the 'strip()' function
"""
# My Code
	def remove_letter_g(s: str)->str:
	    return s.strip('g')
# Your solution is not correct because the `strip()` method removes leading and trailing characters (in this case, 'g') from the string. However, it does not remove all occurrences of the letter 'g' throughout the string. 
# To remove all occurrences of a specific letter from a string, you can use the `replace()` method. The corrected solution using `replace()` method is shown below:
def remove_letter_g(s: str)->str:
    return s.replace('g', '')

# Solution
def remove_letter_g(s: str)->str:
    return s.replace("g", "")
	
# IA's Solutions
# Congrats, your answer is correct!
# Certainly! Here are a few alternative solutions to remove all occurrences of the letter 'g' from a given string in Python:
# 1. Using List Comprehension:
def remove_letter_g(s: str) -> str:
    return ''.join([char for char in s if char != 'g'])
# Explanation: This solution uses list comprehension to iterate over each character in the input string 's'. It only includes characters in the new list that are not equal to 'g'. Finally, it joins the characters back into a single string and returns it.

# 2. Using a for loop:
def remove_letter_g(s: str) -> str:
    result = ''
    for char in s:
        if char != 'g':
            result += char
    return result
# Explanation: This solution iterates over each character in the input string 's' using a for loop. It appends characters that are not equal to 'g' to the 'result' string. Finally, it returns the 'result' string.

# 3. Using filter() function:
def remove_letter_g(s: str) -> str:
    return ''.join(filter(lambda x: x != 'g', s))
# Explanation: This solution uses the `filter()` function with a lambda function to filter out all occurrences of the letter 'g' from the input string 's'. Finally, it joins the remaining characters into a single string and returns it.





# https://www.codingdors.com/problem/10
"""
convert_miles
Show Solution
Given an integer 'n', return the kilometers that this number of miles represents. Hint: 1 mile = 1.60934 kilometers. 

convert_miles(1) -> 1.60934 

convert_miles(0.4) -> 0.643736

Theory
convert_miles
1. Variable: A container that holds a value that can be changed or referenced. 


n = 10


2. Function: A reusable block of code that performs a specific task. 


def multiply(x, y): 
    return x*y


3. Float: A numeric data type that represents decimals or fractions. 


n = 3.14


4. Constant: A fixed value that cannot be changed. 


PI = 3.14159


5. Conversion: The process of changing the form or unit of a value. int("3") converts the string "3" to the integer 3.

Hint
convert_miles
- You need to multiply the number of miles by a conversion factor to get the kilometers. 

- The conversion factor is 1.60934 kilometers per mile. 

- Use the formula: kilometers = miles * conversion factor.
"""
# My Code
def convert_miles(n: float)->float:
    miles = n
    kilometers = miles * 1.60934
    return kilometers
	
# Solution
def convert_miles(n: float)->float:
    return n * 1.60934
	
# IA's Solutions
# Congrats, your answer is correct!
# Sure! Here are a few alternative solutions in Python for the given problem:

# 1. Using a lambda function:
convert_miles = lambda n: n * 1.60934
# This solution uses a lambda function to directly calculate the kilometers from miles using the conversion factor.

# 2. Using a single line function:
def convert_miles(n: float) -> float: return n * 1.60934
# This solution combines the function definition and return statement into a single line, making it more concise.

# 3. Using math library:
import math
def convert_miles(n: float) -> float:
    return math.prod([n, 1.60934])
# This solution utilizes the math library to calculate the product of the miles and the conversion factor.
# All of these solutions achieve the same result as the original solution, but offer different ways to express the logic for converting miles to kilometers in Python.
