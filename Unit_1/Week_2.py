"""
CODING DORS
UNIT 1 - CONDITIONALS - https://cs50.harvard.edu/python/2022/notes/1/
WEEK 2 - Conditionals 1 - https://www.codingdors.com/week/2
"""





# https://www.codingdors.com/problem/101
"""
is_even
Show Solution
Write a function that checks if a given number is even.
is_even(5) -> False
is_even(10) -> True
is_even(99) -> False

Theory
is_even
1. Boolean: a data type that has two possible values, usually called "true" and "false." 'True', 'False'
2. If statement: a control flow statement that allows a program to execute different code depending on whether a specific condition is true or false. 
if x < 5: print("x is less than 5")
3. Modulo operator: an arithmetic operator that returns the remainder of a division operation (%). Example: 
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
This function takes a number as an argument and checks if it's even using the modulo operator. If the result is zero (meaning the number is divisible by 2), then the function returns 'True'. Otherwise, it returns 'False'. The 'if' statement allows the program to execute different code based on whether the number is even or odd.

Hint
is_even
1. The function should take in one argument.
2. The argument should be a number.
3. To check if a number is even, you need to divide it by 2 and check if the remainder is 0.
4. The function should return True if the number is even and False if the number is odd.
"""
# My Code
	def is_even(n: int) -> bool:
	    return n % 2 == 0
  
# Solution
	def is_even(n: int) -> bool:
		if n % 2 == 0:
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/102
"""
is_positive
Show Solution
Write a function that checks if a given number is positive.
is_positive(1) -> True
is_positive(-10) -> False
is_positive(19) -> True

Theory
is_positive
1. Function: A function is a block of code that performs a specific task when called. It takes input as parameters, performs an action, and returns an output. 
def add_numbers(x, y): 
    return x + y
2. Conditional Statement: A statement that performs a different action based on whether a condition is True or False. An if statement is an example of a conditional statement. 
x = 10 
if x > 5: 
    print("x is greater than 5")
3. Comparison Operator: An operator that compares two values and returns a Boolean value (True or False). Examples include ==, >, <, >=, <=. 
x = 5 
y = 10 
if x > y: 
    print("x is greater than y")
4. Boolean: A data type that can be either True or False. It is often used in conditional statements to determine if a statement should be executed. 
x = True
5. Parameter: A value that is passed into a function when it is called. It is used as input to the function. 
def square_number(x): 
    return x**2

Hint
is_positive
1. You only need one line of code to solve this problem.
2. Use a conditional (if/else) statement.
3. The condition should check if the number is greater than zero.
"""
# My Code
	def is_positive(n: int) -> bool:
	    return n > 0
  
# Solution
	def is_positive(n: int) -> bool:
	  if n > 0:
	    return True
		else:
		  return False





# https://www.codingdors.com/problem/103
"""
is_divisible
Show Solution
Write a function that checks if a given number is divisible by another number.
is_divisible(8, 2) -> True
is_divisible(5, 3) -> False
is_divisible(21, 7) -> True

Theory
is_divisible
1. Functions - A function is a block of code that performs a specific task. The function takes an input, performs some calculations on it, and returns the output. 
def square(n): 
    return n * n
2. Parameters - Parameters are special variables that are used to pass values to a function. They are defined in the function's definition, and are used to indicate what types of data the function expects to receive. 
def add(num1, num2): 
    return num1 + num2
3. Return - The return statement is used in a function to indicate what value should be returned when the function is called. Once the return statement is executed, the function is terminated. 
def add(num1, num2): 
    return num1 + num2
4. Boolean - A Boolean is a data type that can have only one of two possible values: true or false. It is often used to represent the results of comparisons or logical operations. '3 > 5' would return false.
5. Modulo operator - The modulo operator (%) returns the remainder of dividing one number by another. '5 % 2' would return 1, as 5 divided by 2 is 2 with a remainder of 1. Example function: 
def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False

Hint
is_divisible
- You can start off defining a function called "is_divisible" that takes in two parameters.
- To check if a number is divisible by another number, you can use the modulo operator (%).
- If the modulo of the first number and second number is 0, then the first number is divisible by the second number. Return True in this case.
- If the modulo is not 0, then the first number is not divisible by the second number. Return False in this case.
"""
# My Code
	def is_divisible(x: int, y: int) -> bool:
	    return x % y == 0

# Solution
	def is_divisible(x: int, y: int) -> bool:
		if x % y == 0:
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/104
"""
maximum
Show Solution
Write a function that returns the maximum of two numbers.
maximum(1, 3) -> 3
maximum(7, -3) -> 7
maximum(10, -10) -> 10

Theory
maximum
1. Parameters - These are the values passed into a function when it is called. 
maximum(1, 3)
 has two parameters: 1 and 3.
2. Return statement - This is what a function sends back as output when it is called. In the case of 
maximum(1, 3)
, the return statement would be 3.
3. Conditional statements - These are statements that execute code based on whether a certain condition is true or false. In the maximum function, we can use a conditional statement to compare the two parameters and return the larger one. For example:
if a > b:
    return a
else:
    return b
In this code, if a is greater than b, it will return a, otherwise it will return b.
4. Function definition - This is the code that defines a function. It includes the function name, parameters, and code to be executed when the function is called. An example function definition for maximum would be:
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
This defines the maximum function with two parameters (a and b) and includes the code to compare them and return the maximum value.

Hint
maximum
1. You only need one conditional statement to solve this.
2. Use "if" and "else" to compare the two numbers.
3. You can use the ">" operator to compare the two numbers.
4. The function should take two arguments, which are the two numbers being compared.
"""
# My Code
	def maximum(x: int, y: int) -> int:
	    return max(x,y)

# Solution
	def maximum(x: int, y: int) -> int:
		if x > y:
		  return x
		else:
		  return y





# https://www.codingdors.com/problem/105
"""
minimum
Show Solution
Write a function that returns the minimum of two numbers.
minimum(3, 7) -> 3
minimum(-3, -7) -> -7
minimum(10, 110) -> 10

Theory
minimum
1. Parameters: These are the inputs given to a function. They are defined within the parentheses of the function. Example: In the function 
def multiply(x, y)
, x and y are parameters.
2. Return statement: This statement returns the output of a function. It is used to exit a function and pass a value back to the caller. Example: In the function 
def add(x, y): 
    return x + y
, the 'return x + y' statement returns the sum of x and y.
3. if/else statements: These are conditional statements that execute code based on a condition being True or False. If the condition is True, the code within the if statement is executed. If it is False, the code within the else statement is executed. Example: 
if  x > 0: 
    return x
4. Comparison operators: These operators are used to compare values. Some of the common comparison operators are <, >, <=, >=, ==, and !=. == is used to check if two values are equal while != checks if they are not equal. Example: 
if x == y: 
    return True
5. Functions: Functions are blocks of code that perform a specific task. They are defined using the 'def' keyword followed by the function name, parentheses and a colon. Example: 
def add(x, y): 
    return x + y

Hint
minimum
1. This function should take in two parameters.
2. Use an if statement to compare the two numbers.
3. Return the smaller of the two numbers.
"""
# My Code
	def minimum(x: int, y: int) -> int:
	    return min(x,y)
  
# Solution
	def minimum(x: int, y: int) -> int:
		if x < y:
		  return x
		else:
		  return y





# https://www.codingdors.com/problem/106
"""
absolute_value
Show Solution
Write a function that returns the absolute value of a number.
absolute_value(8) -> 8
absolute_value(-19) -> 19
absolute_value(-37) -> 37

Theory
absolute_value
1. Function: A function is a block of code that performs a specific task. It can take input (by parameters) and return a result. It helps in modularizing a program, making it easier to read and maintain. Example: 
def add(a,b): 
    return a+b
2. Conditionals: Conditionals are statements that help control the flow of a program based on certain conditions. 'If', 'else', and 'elif' are some keywords used for conditionals in Python. They help us make decisions based on the current state of the program. Example: 
if a > b: 
    print("a is greater than b")
3. Math functions: Math functions are built-in functions in Python that help perform mathematical operations. 'abs()' is one such function that returns the absolute value of a number. Example: 
abs(-5.6)
4. Parameters: Parameters are the inputs to a function. They provide specific values that a function uses to perform a certain task. Example: 
def multiply(a,b): 
    return a*b
5. Return statement: A return statement is used to exit a function and return a value. It can be used to provide output from a function so that it can be used in other parts of the program. Example: 
def divide(a,b): 
    return a/b

Hint
absolute_value
1. Consider what the absolute value of a number means. 
2. The absolute value is always positive, regardless of the input. 
3. One possible solution involves using an if statement to check whether the input is negative.
"""
# My Code
	def absolute_value(n: int) -> int:
	    return abs(n)
  
# Solution
	def absolute_value(n: int) -> int:
		return abs(n)





# https://www.codingdors.com/problem/107
"""
greater_number
Show Solution
Write a function that returns the greater number of three given numbers.
greater_number(1, 2, 3) -> 3
greater_number(-1, -2, -3) -> -1
greater_number(10, 15, 7) -> 15

Theory
greater_number
1. Parameters - Values that are passed into a function. 'num1', 'num2', and 'num3' are the parameters in this problem.
2. Return Statement - A statement that specifies the value to be returned by a function. In this case, the function should return the greatest number amongst the three given numbers.
3. Conditional Statements - Statements used to perform different actions based on different conditions. The 'if-elif-else' conditional statement can be used to compare the given numbers and return the greatest number as output.

Hint
greater_number
1. You'll need to use conditionals to compare the numbers.
2. You can set a variable to one of the numbers initially and compare the other two numbers to it to find the greater one. 
3. Keep updating the variable with the greater number until you've compared all three. 
4. Remember to return the final value of the variable.
"""
# My Code
	def greater_number(x: int, y: int, z: int) -> int:
	    return max(x,y,z)
  
# Solution
	def greater_number(x: int, y: int, z: int) -> int:
		if x > y and x > z:
		  return x
		elif y > x and y > z:
		  return y
		else:
		  return z





# https://www.codingdors.com/problem/108
"""
is_negative
Show Solution
Write a function that checks if a given number is negative.
is_negative(5) -> False
is_negative(-5) -> True
is_negative(-21) -> True

Theory
is_negative
1. The if statement allows a program to execute certain code only if a certain condition is met. The code inside the if statement only runs if the condition inside the parentheses evaluates to True. Example:
num = 5
if num > 0:
    print("The number is positive!")  # this line will not execute because num is not greater than 0
2. A boolean is a data type in Python that can have one of two possible values: True or False. Boolean values are often used in conditional statements to determine whether or not a certain block of code should be executed. Example:
is_raining = False
if is_raining:
    print("Don't forget your umbrella!")
else:
    print("Enjoy the sunshine!")  # will print "Enjoy the sunshine!"
3. A comparison operator allows you to compare two values and returns a boolean value indicating whether the comparison is True or False. The most commonly used comparison operators in Python are: == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to). Example:
age = 25
if age >= 18:
    print("You are old enough to vote!")  # will print "You are old enough to vote!"
4. A function is a named block of code that performs a specific task. Functions help to break down complex problems into smaller, more manageable pieces. You can call a function multiple times throughout your code, which can help to eliminate redundant code. Example:
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
result = add_numbers(5, 7)
print(result)  # will print 12

Hint
is_negative
- Think about the comparison operator that checks if a number is less than 0.
- The function should take in a single parameter, which is the number to be checked.
- The return value of the function should be a boolean (True or False).
"""
# My Code
	def is_negative(n: int) -> bool:
	    return n < 0
  
# Solution
	def is_negative(n: int) -> bool:
		if n < 0:
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/109
"""
is_odd
Show Solution
Write a function that checks if a given number is odd.
is_odd(8) -> False
is_odd(9) -> True
is_odd(-21) -> True

Theory
is_odd
1. Function definition: A function is a block of organized, reusable code that is used to perform a single, related action. Example: 
def is_odd(num):
2. Modulo operator (%): The modulo operator returns the remainder of a division operation. Example: 
5 % 2
 returns 1 because 5 divided by 2 is 2 with a remainder of 1.
3. Conditional statements: Conditional statements are used to perform different actions based on different conditions. Example: 
if num % 2 == 0:
 (performs an action if the number is even)
4. Boolean values: Boolean values are either True or False. Example: True, False.
5. Return statement: The return statement is used to stop the execution of a function and return a value to the calling function. Example: 
return True

Hint
is_odd
1. Consider using the modulus operator (%) to check if the number is evenly divisible by 2.
2. Remember that negative numbers can be odd or even, so you'll need to consider those cases as well.
3. Your function should return a boolean value (True or False) based on whether the number is odd or not.
"""
# My Code
	def is_odd(n: int) -> bool:
	    return n % 2 != 0
  
# Solution
	def is_odd(n: int) -> bool:
		if n % 2 != 0:
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/110
"""
is_leap_year
Show Solution
Write a function that checks if a given year is a leap year.
Hint: A leap year is divisible by 4 but not divisible by 100
is_leap_year(2020) -> True
is_leap_year(2021) -> False
is_leap_year(1996) -> True

Theory
is_leap_year
1. Conditional Statements: These are used for decision-making and allow code to execute based on whether a certain condition is true or false. Example: 
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
2. Modulus Operator: It gives us the remainder of dividing one number by another number. In the case of leap years, a year is a leap year if it is divisible by 4, except for years that are divisible by 100, in which case it is only a leap year if it is also divisible by 400. Example:
print(10 % 3)  # prints 1, which is the remainder of 10 divided by 3
3. Logical Operators: They are used to combine conditional statements. "and" and "or" are the most commonly used logical operators. Example:
if x > 5 and y > 10:
    print("Both conditions are true")

Hint
is_leap_year
1. Leap years occur every four years.
2. If a year is divisible by 100, then it is not a leap year unless it is also divisible by 400.
3. Determine if the given year satisfies the above conditions to determine if it is a leap year or not.
"""
# My Code
	def is_leap_year(year: int) -> bool:
	    return year % 4 == 0 and year % 100 != 0 
  
# Solution
	def is_leap_year(year: int) -> bool:
		div_by_4 = year % 4
		div_by_100 = year % 100
		
		if div_by_4 == 0 and div_by_100 != 0:
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/111
"""
is_vowel
Show Solution
Write a function that checks if a given character is a vowel.
is_vowel('a') -> True
is_vowel('b') -> False
is_vowel('u') -> True

Theory
is_vowel
1. Functions allow you to group a set of statements that perform a specific task. Once a function is defined, it can be reused multiple times. Example: 
def add_numbers(x, y):
    return x + y
print(add_numbers(3, 5)) # Output: 8
2. Conditional statements are used to execute specific code when a certain condition is met. Example: 
x = 5 
if x > 0: 
    print("Positive")
elif x == 0: 
    print("Zero")
else: 
    print("Negative")
3. A Boolean data type is a data type that has only two possible values: True or False. Boolean values are often used in conditional statements. Example: 
x = 10
y = 5 
z = x > y
print(z) # Output: True
4. A string is a sequence of characters in Python. Strings are enclosed in quotes, either single or double quotes. Example: 
x = "Hello, world!"
print(x[0]) # Output: "H"
5. Loops allow you to iterate over a set of values and perform a specific task for each value in the set. Example: 
for i in range(5):
    print(i)

Hint
is_vowel
1. Consider using if-else statements. 
2. Remember that vowels are a, e, i, o, and u. 
3. You can use the in keyword to check if a character is in a string.
"""
# My Code
	def is_vowel(char: str) -> bool:
	    return char in ["a", "e", "i", "o", "u"]

# Solution
	def is_vowel(char: str) -> bool:
		char = char.lower()
		if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
	    return True
	  else:
	    return False





# https://www.codingdors.com/problem/112
"""
is_consonant
Show Solution
Write a function that checks if a given character is a consonant.
is_consonant('c') -> True
is_consonant('a') -> False
is_consonant('z') -> True

Theory
is_consonant
1. A statement that executes a specific piece of code if a particular condition is true. 
if x < 0:
2. An expression that evaluates to either True or False. 
x > y
3. An operator that compares two values and returns a boolean value based on the comparison. 
==, >, <, >=, <=
4. An operator that combines two conditions and returns True if both conditions are true. 
and
5. An operator that reverses the boolean value of a condition. 
not
 Example:
def is_consonant(char):
    if char.isalpha() and char.lower() not in 'aeiou':
        return True
    else:
        return False
In this example, we use a conditional statement (if), a boolean expression (char.lower() not in 'aeiou'), a comparison operator (==), a conditional operator (and), and a not operator (not). The function checks if the given character is a letter (using the isalpha() method) and a consonant (by checking if the lowercase version of the character is not in the string 'aeiou'). If both conditions are true, the function returns True. Otherwise, it returns False.

Hint
is_consonant
1. Think about what makes a character a consonant. 
2. Remember that vowels are a, e, i, o, and u. 
3. Consider using conditional statements to check if a character is a vowel or consonant. 
4. Keep in mind that the function should return a Boolean value.
"""
# My Code
	def is_consonant(char: str) -> bool:
	    vowels = ["a", "e", "i", "o", "u"]
	    return char.lower() not in vowels
  
# Solution
	def is_consonant(char: str) -> bool:
		char = char.lower()
		
		if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/113
"""
is_uppercase
Show Solution
Write a function that checks if a given character is uppercase.
is_uppercase('a') -> False
is_uppercase('A') -> True
is_uppercase('Z') -> True

Theory
is_uppercase
1. Strings: A string is a sequence of characters, enclosed in single or double quotes. 
'Hello World'
 is a string.
2. Conditional Statements: Conditional statements are used to make decisions and execute different code blocks based on certain conditions. An if statement is one such conditional statement. Example: 
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
3. Comparison Operators: Comparison Operators are used to compare two values and evaluate to either True or False. Examples include == (equal to), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), != (not equal to). Example: 
x = 5
y = 10
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")
4. ASCII Codes: The ASCII code represents each character as a unique number between 0 and 127. Uppercase letters are represented by numbers between 65-90, while lowercase letters are represented by numbers between 97-122. Example:
print(ord('A'))  # output: 65
print(chr(65))  # output: 'A'

Hint
is_uppercase
1. You only need to check a single character at a time.
2. The function should return a boolean value.
3. You can use the function isupper()
"""
# My Code
	def is_uppercase(char: str) -> bool:
	    return char.isupper()
  
# Solution
	def is_uppercase(char: str) -> bool:
		if char.isupper():
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/114
"""
is_lowercase
Show Solution
Write a function that checks if a given character is lowercase.
is_lowercase('a') -> True
is_lowercase('A') -> False
is_lowercase('z') -> True

Theory
is_lowercase
1. A conditional statement that allows for different actions to be taken based on whether a condition is true or false. Example: 
if x < 0:
    print("Negative number")
else:
    print("Non-negative number")
2. ord() function: Returns the Unicode code point of a given character. Example: 
ord('a')
# Output: 97
3. chr() function: Returns the character that corresponds to the given Unicode code point. Example: 
chr(97)
# Output: 'a'
4. Boolean: A data type with only two possible values, True or False. Example: 
x = True
y = False
5. String: A sequence of characters. Example: 
x = 'hello world'

Hint
is_lowercase
- Think about the islower() function.
- Your function should return True or False
"""
# My Code
def is_lowercase(char: str) -> bool:
    return char.islower()
  
# Solution
def is_lowercase(char: str) -> bool:
	if char.islower():
	  return True
	else:
	  return False





# https://www.codingdors.com/problem/115
"""
is_same_letter
Show Solution
Write a function that checks if two given characters are the same letter, regardless of their case.
is_same_letter('a', 'A') -> True
is_same_letter('a', 'b') -> False
is_same_letter('C', 'C') -> True

Theory
is_same_letter
1. Function: A function is a block of organized, reusable code that is used to perform a single, related action. It takes input, processes it, and produces output. 
def is_same_letter(char1, char2):
2. Conditional Statements: Conditional statements are used to perform different actions based on different conditions. The if statement is used to check a condition, and if it is True, then a block of code is executed. 
if char1.lower() == char2.lower():
3. Comparison Operators: Comparison operators are used to compare two values. The result of a comparison is either True or False. == is the equality operator, which checks if two values are equal. 
if char1.lower() == char2.lower():
4. String Methods: String methods are built-in functions that can be used to manipulate strings. lower() is a string method that returns a copy of the string in which all case-based characters have been lowercased. 
if char1.lower() == char2.lower():
Example: 
# Function to check if two given characters are the same letter, regardless of their case
def is_same_letter(char1, char2):
    if char1.lower() == char2.lower():
        return True
    else:
        return False
In this example, we define a function 
is_same_letter
that takes two arguments char1 and char2. We use a conditional statement to check if the lowercased versions of char1 and char2 are equal using the equality operator. If they are equal, we return True. If they are not equal, we return False. 
is_same_letter('a', 'A') # True
is_same_letter('a', 'b') # False
is_same_letter('C', 'C') # True
When we pass in the arguments 'a' and 'A', the function returns True because the lowercase versions of both characters are equal. When we pass in the arguments 'a' and 'b', the function returns False because the lowercase versions of the two characters are not equal. Finally, when we pass in the arguments 'C' and 'C', the function returns True because both characters are equal and we are ignoring case.

Hint
is_same_letter
1. You can use the built-in string method 
lower()
 or 
upper()
 to convert both characters to the same case before comparing them
2. You should compare if both characters are the same letter
"""
# My Code
	def is_same_letter(char1: str, char2: str) -> bool:
	    return char1.lower() == char2.lower()
  
# Solution
	def is_same_letter(char1: str, char2: str) -> bool:
		char1 = char1.lower()
		char2 = char2.lower()
		#or you could use upper() for both variables	
		if char1 == char2:
		  return True
		else:
		  return False
	




# https://www.codingdors.com/problem/116
"""
is_digit
Show Solution
Write a function that checks if a given character is a digit.
is_digit(1) -> True
is_digit('a') -> False
is_digit('!') -> False

Theory
is_digit
1. Type conversion: The process of converting one data type to another data type. Example: 
str(5)
 converts the integer 5 into the string '5'.
2. Conditionals: Statements that check whether a condition is true or not. Example: 
if x > 5:
 checks if x is greater than 5.
3. Comparison operators: Operators that compare two values and return a Boolean value (True or False) depending on the result of the comparison. Example: >= checks if the left operand is greater than or equal to the right operand.
4. Character encoding: A system that assigns a unique number to each character. Example: ASCII assigns the number 48 to the character '0'.
5. Logical operators: Operators that combine two or more Boolean expressions and return a Boolean value based on the result of the combination. Example: 'and' returns True if both operands are True.
6. Type checking: The process of verifying the data type of a value. Example: 
isinstance(5, int)
 checks if the value 5 is an integer.

 Hint
is_digit
1. You can use the built-in function 
isdigit()
.
2. The function should take in one parameter.
3. The parameter can be any data type.
4. The function should return a boolean value.
"""
# My Code
	def is_digit(char: str) -> bool:
	    return char.isdigit()
  
# Solution
	def is_digit(char: str) -> bool:
		if char.isdigit():
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/117
"""
is_alphabetic
Show Solution
Write a function that checks if a given character is alphabetic.
is_alphabetic('g') -> True
is_alphabetic('1') -> False
is_alphabetic('?') -> False

Theory
is_alphabetic
1. Strings: Strings are immutable sequences of Unicode code points. They can be created by enclosing characters in quotes. 
'hello'
 is a string.
2. Conditional Statements: A conditional statement is used to execute a certain code only if a particular condition is true. if is a conditional statement. Example: 
if x > 5:
    print('x is greater than 5')
3. Boolean: A boolean is a data type that can have only one of two possible values: 
True or False
4. Characters: A character is a letter, number, or symbol. 
5. isalpha(): A string method that returns True if all the characters in the string are alphabetic and there is at least one character, otherwise it returns False. Example:
s = 'alpha'
print(s.isalpha()) # True
s = 'alpha123'
print(s.isalpha()) # False

Hint
is_alphabetic
- Consider using the 
isalpha()
 method built into Python strings
- The function should return a boolean value (True or False) based on whether the given character is alphabetic or not
"""
# My Code
	def is_alphabetic(char: str) -> bool:
	    return char.isalpha()
  
# Solution
	def is_alphabetic(char: str) -> bool:
		if char.isalpha():
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/118
"""
is_alphanumeric
Show Solution
Write a function that checks if a given character is alphanumeric.
is_alphanumeric('a') -> True
is_alphanumeric('1') -> True
is_alphanumeric('.') -> False

Theory
is_alphanumeric
1. Character: Characters are symbols used in writing, output to display or for any other purpose of communication. In computing, a character is represented by a numerical code that corresponds to a character in the character set. Example: 
'a'
 is a character in the English alphabet.
2. Alphanumeric: An alphanumeric is any character of the English alphabet (a to z, A to Z) and any digit (0 to 9). Example: 'a' or '1'.
3. Boolean: In programming, Boolean is a data type used to represent logic or truth values. It has only two possible values, True or False. Example: 
is_alphanumeric('a')
 returns True.
4. Function: Function is a block of code that can perform a task, and returns a result. It helps to eliminate repetitive code. Example:
def is_alphanumeric(char):
    if char.isalnum():
        return True
    else:
        return False

Hint
is_alphanumeric
- Use the built-in functions isalpha() and isdigit() to check if a character is an alphabet or a digit. 
- You can use the built-in function isalnum() as well
- Return True if either is True, otherwise return False.
"""
# My Code
	def is_alphanumeric(char: str) -> bool:
	    return char.isalnum()
  
# Solution
	def is_alphanumeric(char: str) -> bool:
		if char.isalnum():
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/119
"""
is_greater_or_equal
Show Solution
Write a function that checks if the first given number is greater than or equal to the second given number.
is_greater_or_equal(3, 3) -> True
is_greater_or_equal(-10, -21) -> True
is_greater_or_equal(1, 10) -> False

Theory
is_greater_or_equal
1. Function definition: A function is a block of code that performs some specific task and can be reused whenever required. 
def my_function()
2. Parameters: Parameters are the values that are passed to a function when it is called. 
def my_function(param1, param2)
3. Comparison operators: Comparison operators are used to compare two values and return True or False based on the comparison result. Examples: ==, !=, >, <, >=, <=.
4. Conditional statements: Conditional statements are used to execute specific code based on certain conditions. Examples: if, else, elif.

Hint
is_greater_or_equal
1. You only need one line of code using a comparison operator. 
2. Use the greater than or equal to operator.
"""
# My Code
	def is_greater_or_equal(x: int, y: int) -> bool:
	    return x >= y
  
# Solution
	def is_greater_or_equal(x: int, y: int) -> bool:
		if x >= y:
		  return True
		else:
		  return False





# https://www.codingdors.com/problem/120
"""
is_smaller_or_equal
Show Solution
Write a function that checks if the first given number is smaller than or equal to the second given number.
is_smaller_or_equal(1, 3) -> True
is_smaller_or_equal(-10, -10) -> True
is_smaller_or_equal(7, 1) -> False

Theory
is_smaller_or_equal
1. Comparison operators: These operators are used to compare two values. ==(equal), !=(not equal), <(less than), >(greater than), <=(less than or equal to), >=(greater than or equal to) are comparison operators. For example, 
10 < 20
 will return True because 10 is less than 20.
2. if/else statement: This statement is used to perform different actions based on different conditions. If the condition specified is True, then the code within the IF block will be executed, else the code within the ELSE block will be executed. For example,
if x < y:
    # do something
else:
    # do something else
3. Function: Functions are used to perform specific actions without repeating the same code. It takes some input, performs the specified task, and returns the output. For example,
def add_numbers(x, y):
    return x + y
4. Boolean: A Boolean is a data type with only two possible values, True or False. Booleans are mostly used to perform logical operations. For example, 
(10 < 20) and (30 > 40)
 will return False because the second condition is False.
5. Conditional expression (ternary operator): It is a shorthand syntax for an if-else statement. It is used to evaluate an expression based on a condition. For example, 
x if condition else y
 will return x if the condition evaluates to True, else it will return y.

Hint
is_smaller_or_equal
1. You have a function that takes two arguments.
2. The function should return a boolean value.
3. You need to compare the two arguments using a comparison operator.
4. You need to use either the less than or equal to operator or the greater than or equal to operator.
5. You need to decide what to return in case the two given numbers are equal.
"""
# My Code
	def is_smaller_or_equal(x: int, y: int) -> bool:
	    return x <= y
  
# Solution
	def is_smaller_or_equal(x: int, y: int) -> bool:
		if x <= y:
		  return True
		else:
		  return False
