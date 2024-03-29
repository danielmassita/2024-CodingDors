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





# 
