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

Theory
sum_or_half_sum
1. Conditional Statements - Conditional statements in Python are used to execute certain blocks of code when certain conditions are true. They are created using if, elif, and else statements. 
Example: 
x = 10
if x > 5:
  print("x is greater than 5")
elif x == 5:
  print("x is equal to 5")
else:
  print("x is less than 5")
2. Arithmetic Operators - Arithmetic operators are used to perform mathematical operations in Python. They include +, -, *, /, %, and //. 
Example: 
a = 10
b = 5
print(a + b) # Output: 15
print(a - b) # Output: 5
print(a * b) # Output: 50
print(a / b) # Output: 2.0
print(a % b) # Output: 0
print(a // b) # Output: 2
3. Functions - Functions in Python are blocks of code that can be called to perform a specific task. They can take input parameters and return values. 
Example: 
def multiply(x, y):
  return x * y
print(multiply(2, 3)) # Output: 6
4. Boolean Operators - Boolean operators are used to compare values and return a boolean value of either True or False. They include and, or, and not. 
Example: 
x = 5
y = 10
print(x > 3 and y > 7) # Output: True
print(x < 3 or y < 7) # Output: False
print(not x == 5) # Output: False
5. Comparison Operators - Comparison operators are used to compare values in Python and return a boolean value of either True or False. They include ==, !=, >, <, >=, and <=. 
Example: 
x = 5
y = 10
print(x == 5) # Output: True
print(x != 5) # Output: False
print(x > y) # Output: False
print(x < y) # Output: True
print(x >= 5) # Output: True
print(y <= 10) # Output: True

Hint
sum_or_half_sum
1. You will need an if statement to check if the two input integers are the same.
2. Within the if statement, you should return half of the sum of the two integers.
3. If the two integers are not the same, you should return the sum of the two integers.
"""
# My Code
	def sum_or_half_sum(a: int, b: int)-> int:
	    if a == b:
	        return (a+b)/2
	    else:
	        return a+b

# Solution
	def sum_or_half_sum(a: int, b: int)-> int:
	    if a != b:
	        return a + b
	    else:
	        return a

# IA's Solutions
# 1. Using a conditional expression:
	def sum_or_half_sum(a: int, b: int) -> int:
	    return (a + b) / 2 if a == b else a + b
# In this solution, we use a conditional expression which is shorter and more concise than an if-else statement. It directly returns the sum of 'a' and 'b' if they are not equal, and returns half of their sum if they are equal.
# 2. Using a ternary operator:
	def sum_or_half_sum(a: int, b: int) -> int:
	    return (a + b) / 2 if a == b else a + b
# This solution is similar to the first one but uses a ternary operator instead of a conditional expression. Ternary operators are a more compact way to write conditional statements in Python.
# 3. Using the min() and max() functions:
	def sum_or_half_sum(a: int, b: int) -> int:
	    if a == b:
	        return a
	    return a + b
# In this solution, we use the min() and max() functions to handle the case where 'a' and 'b' are equal. If 'a' is equal to 'b', we return 'a'. Otherwise, we return the sum of 'a' and 'b'.





# https://www.codingdors.com/problem/14
"""
absolute_difference
Show Solution
Write a Python function that takes two input numbers 'a' and 'b', and returns the absolute difference between them. However, if the absolute difference is greater than 10, the function should return double the absolute difference instead. For instance, if 'a' is 4 and 'b' is 8, the function should return 4. If 'a' is 10 and 'b' is 25, the function should return 30.
absolute_difference(4, 8) -> 4
absolute_difference(10, 25) -> 30

Theory
absolute_difference
1. Absolute value: Returns the absolute value of a number. It returns the number without its sign. 
abs(-5) #5
2. Conditional Statements: If the condition evaluates to true, then execute the code in the if block. Otherwise, execute the code in the else block (if it exists).
num = 5
if num > 0:
    print("Positive")
else:
    print("Negative or Zero")
3. Comparison Operators: Used to compare two values. Returns a boolean True or False based on the comparison.
a = 5
b = 10
a < b  # True
a > b  # False
a == b  # False
a != b  # True
4. Double operator: Multiplies a number by 2.
a = 7
a_double = a*2
print(a_double) # 14

Hint
absolute_difference
1. Use the abs() function to calculate the absolute difference between a and b.
2. Check if the absolute difference is greater than 10 using an if statement.
3. If the absolute difference is greater than 10, return double the absolute difference using the multiplication operator.
4. If the absolute difference is not greater than 10, simply return the absolute difference.
"""
# My Code
	def absolute_difference(a: int, b: int)-> int:
	    result = abs(a-b)
	    if result > 10:
	        return 2*result
	    else:
	        return result

# Solution
	def absolute_difference(a: int, b: int)-> int:
	    if abs(a - b) > 10:
	        return abs(a - b) * 2
	    else:
	        return abs(a - b)

# IA's Solution
# Sure! Here is an alternative solution using a single line of code with the ternary operator:
	def absolute_difference(a: int, b: int) -> int:
	    return 2 * abs(a - b) if abs(a - b) > 10 else abs(a - b)
# In this solution, the absolute difference is calculated using `abs(a - b)` and then checked if it is greater than 10. If it is greater than 10, the function returns double the absolute difference. Otherwise, it returns the absolute difference itself. The ternary operator `x if condition else y` is used to achieve this in a single line.





# https://www.codingdors.com/problem/15
"""
dog_trouble
Show Solution
We have a playful dog that barks loudly at night. The 'hour' parameter is the current hour time in the range 0...23. We are in trouble if the dog is barking and the hour is before 6 or after 22. Return True if we are in trouble.
dog_trouble(True, 5) → True
dog_trouble(True, 7) → False
dog_trouble(False, 6) → False

Theory
dog_trouble
1. Boolean - a data type that has only two possible values, true or false. Example:  'True'
2. If/else statement - a programming structure that allows the program to make a decision based on a condition. Example: 
if hour < 6 or hour > 22:
    return True
else:
    return False
3. Comparison operators - operators that compare two values and return a boolean value of true or false. Example: 'hour < 6'
4. Parameters - values that are passed into a function to be used in the function's calculations. Example: 'hour' in 'dog_trouble(True, 6)'
5. Return statement - a statement in a function that returns a value back to the caller of the function. Example:  
return True

Hint
dog_trouble
1. Identify the conditions that result in being in trouble. 
2. Determine the range of hours that result in being in trouble. 
3. Look for the given values of the 'hour' parameter to check if they fall within the trouble range. 
4. Use the 'dog' parameter to determine if the dog is actually barking. 
5. Return True if both the conditions are met, else return False.
"""
# My Code
	def dog_trouble(barking: bool, hour: int)-> bool:
	    if hour > 22 or hour < 6:
	        is_late = True
	    if is_late == True and barking == True:
	        return True
	    else:
	        return False
	        

# Solution
	def dog_trouble(barking: bool, hour: int)-> bool:
	    if barking == True and (hour <= 6 or hour >= 22):
	        return True
	    else:
	        return False

# IA's Solution
	def dog_trouble(barking: bool, hour: int) -> bool:
	    return barking and (hour < 6 or hour > 22)
		
# Explanation:
	def dog_trouble(barking: bool, hour: int)-> bool:
		# trouble (true) IF barking(true) AND 6 > hour > 22
		return True if barking and (hour < 6 or hour > 22) else False
# 1. This solution directly returns the result of the logical expression `barking and (hour < 6 or hour > 22)`.
# 2. If `barking` is True and the current `hour` is less than 6 or greater than 22, the expression evaluates to True, indicating that we are in trouble.
# 3. Otherwise, the expression evaluates to False, indicating that we are not in trouble.
	def dog_trouble(barking: bool, hour: int)-> bool:
	  if barking == True and (6 > hour or hour > 22):
	    return True
	  else:
	    return False





# https://www.codingdors.com/problem/16
"""
near_ten
Show Solution
Given an int 'n', return True if it is within 10 of 50. 
Note: abs(num) computes the absolute value of a number.
near_ten(48) → True
near_ten(55) → True
near_ten(5) → False

Theory
near_ten
1. abs() function: Returns the absolute value of a number. 
abs(-5) = 5
2. Comparison operators: Used to compare values and return a boolean value (True or False). 
5 < 10
returns True.
3. Logical operators: Used to combine conditional statements and return a boolean value. 
5 < 10 and 10 < 20
returns True.
4. Ternary operators: A shorter way of writing an if-else statement in one line. 
x = 5 if y == 10 else 0
sets x to 5 if y is equal to 10, otherwise sets it to 0.
"""
# My Code
	def near_ten(n: int)->bool:
	    if 40 <= abs(n) <= 60:
	        return True
	    else:
	        return False
		    
# Solution
	def near_ten(n: int)->bool:
	    c = abs(n - 50)
	    if c <= 10:
	        return True
	    else:
	        return False
		    
# IA's Solutions
# 1. Using the abs() function directly in the comparison:
	def near_ten(n: int) -> bool:
	    return abs(50 - n) <= 10
# Explanation: This solution calculates the absolute difference between 'n' and 50 using abs(50 - n), and then checks if this absolute difference is less than or equal to 10. If it is, the function returns True, indicating that 'n' is within 10 of 50.
# 2. Using a ternary conditional expression:
	def near_ten(n: int) -> bool:
	    return True if abs(50 - n) <= 10 else False
# Explanation: This solution uses a ternary conditional expression to achieve the same result as the first solution. It checks if the absolute difference between 'n' and 50 is less than or equal to 10 and returns True if it is, otherwise it returns False.
# 3. Checking two separate conditions:
	def near_ten(n: int) -> bool:
	    return (n >= 40 and n <= 50) or (n >= 50 and n <= 60)
# Explanation: This solution checks two separate conditions to determine if 'n' is within 10 of 50. It first checks if 'n' is between 40 and 50 (inclusive), and then checks if 'n' is between 50 and 60 (inclusive). If either of these conditions is true, the function returns True.





# https://www.codingdors.com/problem/17
"""
hi_string
Show Solution
Given a string 's', return a new string where "hi " has been added to the front. However, if the string already begins with "hi", return the string unchanged.
hi_string('Alice') → 'hi Alice'
hi_string('hi Bob') → 'hi Bob'
hi_string('') → 'hi'

Theory
hi_string
1. String Concatenation: Joining two or more strings together to produce a new string. Example: 
'hello ' + 'world'
will return 'hello world'.
2. String Slicing: Extracting a part of a string based on its index. Example: 
'computer'[0:4]
will return 'comp'.
3. Conditional Statements: Statement that executes different actions depending on whether a condition is true or false. Example: 
if x > 5: 
    print('x is greater than 5')
4. String Comparison: Comparing two or more strings to check if they are equal or not. Example: 
'hello' == 'world'
 will return False.

Hint
hi_string
1. Check if the first two characters of the string are "hi" using slicing. 
2. If step 1 is True, return the string unchanged. 
3. If step 1 is False, concatenate "hi " at the beginning of the string. 
4. If the string is empty, simply return "hi".
"""
# My Code
	def hi_string(s: str)-> str:
	    if s[0:2]=="hi":
	        return s
	    else:
	        return f"hi {s}"

# Solution
	def hi_string(s: str)-> str:
		if s[0:2] == 'hi':
		  return s
		else:
		  return 'hi ' + s
			
# IA's Solutions
# 1. Using string concatenation:
	def hi_string(s: str) -> str:
	    if s.startswith("hi"):
	        return s
	    else:
	        return "hi " + s
# In this solution, the `startswith()` method is used to check if the string `s` already begins with "hi". If it does, the original string is returned unchanged. Otherwise, "hi " is concatenated with the original string using the `+` operator.
# 2. Using f-strings directly:
	def hi_string(s: str) -> str:
	    if s.startswith("hi"):
	        return s
	    else:
	        return f"hi {s}"
# This solution is similar to the original one provided, but it directly uses an f-string to return the modified string with "hi " added at the front.





# https://www.codingdors.com/problem/20
"""
front5
Show Solution
Given a string 's', we'll say that the front is the first 5 chars of the string. If the string length is less than 5, the front is whatever is there. Return a new string which is 5 copies of the front.
front5('Python') → 'PythoPythoPythoPythoPytho'
front5('Chocolate') → 'ChocoChocoChocoChocoChoco'
front5('abc') → 'abcabcabcabcabc'

Theory
front5
1. Substring: A substring is a smaller part of a string. A string can be sliced to get a smaller part of it. 
"Hello"[1:3]
 returns "el". 
2. Conditional statements: We can use conditional statements like if-else to check if a condition is true, and execute different programs based on it. 
if x > 0:
    print("Positive")
else:
    print("Negative")
3. Concatenation: Concatenation is joining two or more strings into one. We can use the + operator or the join method. 
"Hello" + "World"
 returns "HelloWorld".
4. Repetition: We can repeat a string n number of times using the * operator. 
"Hello" * 3
 returns "HelloHelloHello". 
In this problem, we need to get the front of the string and repeat it 5 times. We can use substring and repetition to solve this.

Hint
front5
1. Identify the first 5 characters of the string.
2. Check if the length of the string is less than 5, if yes, use the whole string as front.
3. Return a new string which is the front repeated 5 times.
"""
# My Code
	def front5(s: str)-> str:
	    tamanho = len(s)
	    if tamanho < 5:
	        front = s[0:tamanho]
	    else:
	        front = s[0:5]
	    return front*5
    
# Solution
	def front5(s: str)-> str:
		first = s[:5]
		return first * 5
		
# IA's Solutions
# 1. Using string slicing and repetition in a single line:
	def front5(s: str) -> str:
	    return (s[:5] if len(s) >= 5 else s) * 5
# This solution uses a conditional expression to check if the length of the string is greater than or equal to 5. If it is, it takes the first 5 characters of the string; otherwise, it takes the entire string. Then, it multiplies this front portion by 5 to get the desired output.
# 2. Using string concatenation in a loop:
	def front5(s: str) -> str:
	    front = s[:5] if len(s) >= 5 else s
	    result = ''
	    for _ in range(5):
	        result += front
	    return result
# This solution follows a more traditional approach by using a loop to concatenate the front portion of the string to the result string five times. It first calculates the front portion of the string based on its length and then iterates five times, appending the front portion each time to build the final result.





# https://www.codingdors.com/problem/181
"""
caught_speeding
Show Solution
You are driving a little too fast, and a police officer stops you. Write a function to return the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(100, True) → 2

Theory
caught_speeding
1. Conditionals are used to make decisions based on certain conditions. The most common conditional statements in programming are if statements and switch statements. Example: 
if x > 10:
    # do something
2. Functions are blocks of reusable code that perform a specific task. They are used to modularize code and make it more efficient. Example: 
def add(a, b) :
    return a + b
3. Variables are used to store and manipulate data in a program. They are declared with a name. Example: 
name = "Alice"
4. Operators are used to perform operations on values and variables in a program. There are many different kinds of operators, including arithmetic, comparison, and logical operators.  Example: 
result = 10 + 5

Hint
caught_speeding
1. You need to write a function that takes in one parameter, which is the speed you were driving at. 
2. The function should return an integer value based on the given conditions. 
3. Remember to account for the exception if it is your birthday.
"""
# My Code
	def caught_speeding(speed: int, is_birthday: bool) -> int:        
	    if is_birthday == True:
	        speed = speed - 5
	
	    if speed <= 60:
	        return int(0)        
	    if 61 <= speed <= 80:
	        return int(1)
	    if speed > 81:
	        return int(2)

# Solution
	def caught_speeding(speed: int, is_birthday: bool) -> int:
	  if is_birthday:
	    speed -= 5
	  if speed <= 60:
	    return 0
	  elif 61 <= speed <= 80:
	    return 1
	  else:
	    return 2
	  
# IA's Solutions
# Here is an alternative solution using a simpler approach without the need for multiple if statements:
	def caught_speeding(speed: int, is_birthday: bool) -> int:
	    if is_birthday:
	        speed -= 5
	    
	    if speed <= 60:
	        return 0
	    elif speed <= 80:
	        return 1
	    else:
	        return 2
# In this solution, we first adjust the speed if it is the driver's birthday. Then, we directly check the speed ranges in a single if-elif-else block. This approach simplifies the code by reducing the number of if statements and improves readability.





# https://www.codingdors.com/problem/183
"""
alarm_clock
Show Solution
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
alarm_clock(1, False) → '7:00'
alarm_clock(0, False) → '10:00'
alarm_clock(6, True) → 'off'

Theory
alarm_clock
1. Conditionals are used to make decisions based on certain conditions. The most common conditional statements in programming are if statements and switch statements. Example: 
if x > 10:
    # do something
2. Functions are blocks of reusable code that perform a specific task. They are used to modularize code and make it more efficient. Example: 
def add(a, b) :
    return a + b
3. Variables are used to store and manipulate data in a program. They are declared with a name. Example: 
name = "Alice"
4. Operators are used to perform operations on values and variables in a program. There are many different kinds of operators, including arithmetic, comparison, and logical operators.  Example: 
result = 10 + 5

Hint
alarm_clock
1. Consider using an if/else statement.
2. Use the boolean variable to determine whether it's a weekday or weekend.
3. If it's a weekday, the alarm time is always "7:00".
4. If it's a weekend and we are not on vacation, the alarm time is "10:00".
5. If we are on vacation, the alarm time on weekdays is "10:00" and on weekends it is "off".
"""
# My Code
	def alarm_clock(day: int, vacation: bool) -> str:
	    if vacation==True:
	        if day==0 or day==6:
	            return f"off"
	        else:
	            return "10:00"
	            
	    else:
	        if day==0 or day==6:
	            return f"10:00"
	        else:
	            return f"7:00"

# Solution
	def alarm_clock(day: int, vacation: bool) -> str:
		if vacation:
		  if day == 0 or day == 6:
		    return "off"
		  else:
		    return "10:00"
		else:
		  if day == 0 or day == 6:
		    return "10:00"
		  else:
		    return "7:00"

# IA's Solutions
# Sure! Here is an alternative solution using a dictionary to store the alarm times:
def alarm_clock(day: int, vacation: bool) -> str:
    alarm_times = {0: "10:00", 1: "7:00", 2: "7:00", 3: "7:00", 4: "7:00", 5: "7:00", 6: "10:00"}
	
    if vacation:
        return "off" if alarm_times[day] == "10:00" else "10:00"
    else:
        return alarm_times[day]
# In this solution, we use a dictionary `alarm_times` to store the alarm times for each day of the week. We then check the value for the given day in the dictionary and return the corresponding alarm time based on whether it is a vacation or not.





# https://www.codingdors.com/problem/184
"""
love_six
Show Solution
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6.
love_six(6, 4) → True
love_six(4, 5) → False
love_six(1, 5) → True

Theory
love_six
1. Conditional statements are used to take decisions based on certain conditions. In python, if, elif, and else are used for conditional statements. Example: 
if x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is a negative number")
2. Boolean Operators are used to combine conditional statements. Python has three Boolean operators: and, or, and not. Example:
if x > 0 and y > 0:
    print("Both x and y are positive numbers")
elif x > 0 or y > 0:
    print("At least one of x and y is a positive number")
3. Comparison Operators are used to compare values. Python has six comparison operators: ==, !=, >, <, >=, <=. Example:
if x == y:
    print("x and y are equal")
elif x != y:
    print("x and y are not equal")
else: 
    print("this will never run")
4. Arithmetic Operators are used to perform mathematical operations in Python. Python has seven arithmetic operators: +, -, *, /, %, //, and **. Example:
x = 10
y = 3
print(x + y)      # 13
print(x - y)      # 7
print(x * y)      # 30
print(x / y)      # 3.33333333333
print(x % y)      # 1
print(x // y)     # 3
print(x ** y)     # 1000
5. Logical Operators are used to combine multiple conditions and return a Boolean value. Python has two logical operators: and and or. Example:
if x > 0 and y > 0:
    print("Both x and y are positive")
elif x > 0 or y > 0:
    print("At least one of x and y is positive")
6. Functions are a group of related statements that perform a specific task when called. In python, a function is defined using the def keyword followed by function name and parameters enclosed in a parentheses. Example: 
def add_numbers(a, b):
    return a + b
sum = add_numbers(2, 5)
print(sum)   # 7

Hint
love_six
Think about the different ways that the numbers can add up or subtract to 6.
"""
# My Code
	def love_six(a: int, b: int) -> bool:
	    if (a or b) == 6:
	        return True
	    elif abs(a-b)==6 or abs(b-a)==6 or abs(a+b)==6:
	        return True
	    else:
	        return False
		    
# Solution
	def love_six(a: int, b: int) -> bool:
		if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
		  return True
		else:
		  return False
			
# IA's Solutions
# Sure! Here is an alternative solution in Python with explanations:
def love_six(a: int, b: int) -> bool:
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6
# Explanation:
# 1. The expression `a == 6` checks if the value of `a` is equal to 6.
# 2. The expression `b == 6` checks if the value of `b` is equal to 6.
# 3. The expression `a + b == 6` checks if the sum of `a` and `b` is equal to 6.
# 4. The expression `abs(a - b) == 6` checks if the absolute difference between `a` and `b` is equal to 6.
# This solution simplifies the conditions by directly checking each condition in a single line, which results in a more concise and readable code.





# https://www.codingdors.com/problem/185
"""
in_one_to_ten
Show Solution
Given a number n, return True if n is in the range 1..10, inclusive. Unless "outside_mode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
in_one_to_ten(5, True) → True
in_one_to_ten(11, False) → False
in_one_to_ten(1, True) → True

Theory
in1to10
1. Conditional Statement: A decision-making statement that specifies which block of code to execute based on a boolean condition. Example: 
if n < 0: 
    print("Number is negative")
2. Comparison Operator: An operator that compares two values and returns a boolean value based on the comparison. Example: 
n < 10
3. Boolean Operator: An operator that combines two or more boolean values and returns a single boolean value. Example: 
n < 10 and n > 0
4. Inclusive Range: A set of integers that includes both the first and last value of the range. Example: 
range(1, 11)
5. Logical NOT Operator: An operator that reverses the boolean value of its operand. Example: 
not n < 10
6. Function Return Statement: A statement that stops the execution of a function and returns a value. Example: 
return True
7. Default Parameter Value: A default value set for a function parameter that is used when the value is not provided by the caller. Example: 
def my_function(x=5):

Hint
in1to10
1. Consider using a conditional statement to handle the two cases (inside and outside mode).
2. Think about the range of values you need to check for each case.
3. Pay attention to the inclusive/exclusive nature of the range.
4. You can use comparison operators (e.g. '<', '>', '<=', '>=') to check if a number is within a certain range.
"""
# My Code
	def in_one_to_ten(n: int, outside_mode: bool) -> bool:
	    if outside_mode==False and (1 <= n <= 10):
	        return True
	    elif outside_mode==True and (10 >= n or n <= 1):
	        return True
	    
	    else:
	        return False

# Solution
	def in_one_to_ten(n: int, outside_mode: bool) -> bool:
		if outside_mode and (n <= 1 or n >= 10):
		  return True
		else:
		  if 1 < n < 10:
		    return True
		  else:
		    return False
			  
# IA's Solutions
# 1. Using conditional expressions:
def in_one_to_ten(n: int, outside_mode: bool) -> bool:
    return (outside_mode and (n <= 1 or n >= 10)) or (not outside_mode and 1 <= n <= 10)
# Explanation: This solution uses conditional expressions to directly return the desired boolean value based on the conditions specified in the question. It checks if `outside_mode` is True and if `n` is less than or equal to 1 or greater than or equal to 10, or if `outside_mode` is False and `n` is in the range 1 to 10.
# 2. Using nested if statements:
def in_one_to_ten(n: int, outside_mode: bool) -> bool:
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10
# Explanation: This solution uses nested if statements to check if `outside_mode` is True and then return True if `n` is less than or equal to 1 or greater than or equal to 10. Otherwise, if `outside_mode` is False, it checks if `n` is in the range 1 to 10 and returns True or False accordingly.





# https://www.codingdors.com/problem/186
"""
near_ten_bool
Show Solution
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
near_ten_bool(12) → True
near_ten_bool(19) → True
near_ten_bool(23) → False

Theory
near_ten
1. The modulo operator (%) returns the remainder of the division of two numbers. For example, 
7 % 3
 is equal to 1, because 7 divided by 3 leaves a remainder of 1.
2. Logical operators are used to combine two or more conditions and evaluate them as a single Boolean expression. 'and' returns True if both conditions are True. 'or' returns True if either of the conditions is True. 'not' negates the result of a Boolean expression.
3. Comparison operators are used to compare two values or expressions. > and < evaluate if one value is greater or less than the other. >= and <= evaluate if one value is greater than or equal to, or less than or equal to, the other. == and != evaluate if two values are equal or not equal. Example:
def is_within_two_of_ten(num):
    return (num % 10 <= 2) or (num % 10 >= 8)
In this example, we use the modulo operator to check if the remainder of dividing num by 10 is within 2 of either end (0, 1, 8, or 9). We combine the conditions using the logical operator or and return the result as a Boolean value.


"""
# My Code
	def near_ten_bool(num: int) -> bool:
	    if (num % 10) in [0, 1, 2, 8, 9]:
	        return True
	    else:
	        return False
		    
# Solution
	def near_ten_bool(num: int) -> bool:
		if num % 10 >= 8 or num % 10 <= 2:
		  return True
		else:
		  return False
			
# IA's Solutions
# 1. Using the abs() function:
def near_ten_bool(num: int) -> bool:
    return (num % 10 <= 2) or (abs(num % 10 - 10) <= 2)
# This solution first checks if the remainder of num divided by 10 is less than or equal to 2. If not, it calculates the absolute difference between the remainder and 10, and checks if that is less than or equal to 2.
# 2. Using the min() function:
def near_ten_bool(num: int) -> bool:
    return min(num % 10, abs(num % 10 - 10)) <= 2
# In this solution, we use the min() function to find the minimum value between the remainder of num divided by 10 and the absolute difference between the remainder and 10. If the minimum value is less than or equal to 2, the function returns True.





# https://www.codingdors.com/problem/188
"""
answer_cell
Show Solution
Your cell phone rings. Return True if you should answer it. Normally you answer, except in the morning you only answer if it is your mom calling. In all cases, if you are asleep, you do not answer.
answer_cell(False, True, True) → False
answer_cell(True, True, True) → False
answer_cell(False, False, False) → True

Theory
answer_cell
1. If statements is used to execute a block of code only if a certain condition is true. It can be accompanied by else and elif statements to provide multiple conditions. Example: 
age = 18
if age >= 18:
    print("You are eligible to vote.")
2. Logical operators are used to combine and manipulate boolean values. and operator returns True if both conditions are true, or operator returns True if at least one condition is true, and not operator returns the opposite boolean value of the condition. Example: 
is_raining = True
has_umbrella = True
if is_raining and has_umbrella:
    print("You can go out without getting wet.")
3. Variables are used to store and manipulate data values in a program. The value of a variable can be changed in the program. Example: 
x = 5
y = 3
z = x + y
print(z) # Output: 8

Hint
answer_cell
1. Consider the time of day and the identity of the caller. 
2. Also, take into account whether you are asleep or not.
"""
# My Code
	def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
	    if is_asleep == True:
	        return False
	            
	    else:
	        if (is_morning == True) and (is_mom == True):
	            return True
	        elif (is_morning == True) and (is_mom == False):
	            return False
	        else:
	            return True
			
# Solution
	def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
		if is_asleep:
		  return False
		elif is_morning and not is_mom:
		  return False
		return True
		
# IA's Solutions
# Solution 1:
def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
    if is_asleep:
        return False
    if is_morning and not is_mom:
        return False
    return True
# Explanation:
# This solution uses the same logic as the original code but simplifies the conditions by directly checking if `is_asleep` is True and returning False. Then, it checks if it is morning and not mom calling, returning False in that case. Otherwise, it returns True.
# Solution 2:
def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
    return not is_asleep and (not is_morning or is_mom)
# Explanation:
# In this solution, we use a single line of code with boolean logic. It first checks if the person is not asleep and then checks whether it is not morning or if it is morning, then it should be the mom calling. This approach simplifies the conditions into a single expression.





# https://www.codingdors.com/problem/189
"""
tea_party
Show Solution
We are having a party with amounts of tea and candy. Return the int outcome of the party encoded as 0=bad, 1=good, or 2=great. A party is good (1) if both tea and candy are at least 5. However, if either tea or candy is at least double the amount of the other one, the party is great (2). However, in all cases, if either tea or candy is less than 5, the party is always bad (0).
tea_party(5, 5) → 1
tea_party(10, 5) → 2
tea_party(4, 5) → 0

Hint
tea_party
1. Identify the three possible outcomes: bad (0), good (1), or great (2).
2. Check if either tea or candy is less than 5. If so, return 0 (bad).
3. Check if both tea and candy are at least 5. If so, you have at least a good party (1).
4. Check if either tea or candy is at least double the amount of the other one. If so, return 2 (great).
5. If none of the above conditions have been met, return 1 (good).
"""
# My Code
	def tea_party(tea: int, candy: int) -> int:
	    if tea < 5 or candy < 5:
	        return 0
	    elif (tea >= 2*candy) or (candy >= 2*tea):
	        return 2
	    else:
	        return 1
		    
# Solution
	def tea_party(tea: int, candy: int) -> int:
		if tea < 5 or candy < 5:
		  return 0
		elif tea >= 2 * candy or candy >= 2 * tea:
		  return 2
		else:
		  return 1
			
# IA's Solutions
# Certainly! Your solution is already quite clear and efficient. Here is an alternative solution using a nested if-else structure:
def tea_party(tea: int, candy: int) -> int:
    if tea < 5 or candy < 5:
        return 0
    else:
        if tea >= 2*candy or candy >= 2*tea:
            return 2
        else:
            return 1
# This alternative solution achieves the same outcome by checking the conditions in a nested manner.
# Another way to approach this problem is by using a single return statement with all the conditions checked in a compact way:
def tea_party(tea: int, candy: int) -> int:
    return 0 if tea < 5 or candy < 5 else 2 if tea >= 2*candy or candy >= 2*tea else 1
# This solution utilizes conditional expressions within a single return statement to directly return the appropriate outcome based on the conditions. It is more concise but may be slightly less readable for some individuals.





# https://www.codingdors.com/problem/190
"""
fizz_string
Show Solution
Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz". If both the "f" and "b" conditions are true, return "FizzBuzz". In all other cases, return the string unchanged.
fizz_string('fizz') → 'Fizz'
fizz_string('buzzb') → 'Buzz'
fizz_string('fizzb') → 'FizzBuzz'
fizz_string('abcdefg') → 'abcdefg'

Theory
fizz_string
1. The if statement is used to check a condition and perform certain operations based on whether the condition is true or false. Example: 
if x > 0:
    print("Positive")
else:
    print("Negative or Zero")
2. The startswith() method is used to check whether a given string starts with a specified prefix. Example: 
str1 = "Hello World"
if str1.startswith("Hello"):
    print("Starts with Hello")
else:
    print("Does not start with Hello")
3. The endswith() method is used to check whether a given string ends with a specified suffix. Example: 
str1 = "Hello World"
if str1.endswith("World"):
    print("Ends with World")
else:
    print("Does not end with World")
4. The and operator is used to check if both conditions in a logical statement are true. Example: 
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive")
else:
    print("At least one number is not positive")
5. The return statement is used to exit a function and return a value or an object. Example: 
def square(x):
    return x*x
6. The if-elif-else statement is used to execute different blocks of code based on multiple conditions. Example: 
x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

Hint
fizz_string
1. Check if the string starts with "f".
2. Check if the string ends with "b".
3. Combine the two conditions using "and" operator.
4. Use conditional statements to return FizzBuzz, Fizz, Buzz or the original string.
"""
# My Code
	def fizz_string(s: str) -> str:
	    if s[0]=="f" and s[-1]=="b":
	        return "FizzBuzz"
	    elif s[0] == "f":
	        return "Fizz"
	    elif s[-1] == "b":
	        return "Buzz"
	    else:
	        return s
	    

# Solution
	def fizz_string(s: str) -> str:
		if s[0] == "f" and s[-1] == "b":
		  return "FizzBuzz"
		elif s[0] == "f":
		  return "Fizz"
		elif s[-1] == "b":
		  return "Buzz"
		else:
		  return s
			
# IA's Solutions
# Sure! Here is an alternative solution using Python that achieves the same result as the one you provided:
def fizz_string(s: str) -> str:
    fizz = "Fizz" if s.startswith("f") else ""
    buzz = "Buzz" if s.endswith("b") else ""
    if fizz and buzz:
        return fizz + buzz
    elif fizz:
        return fizz
    elif buzz:
        return buzz
    else:
        return s
# In this solution, we use the `startswith()` method to check if the string starts with "f" and the `endswith()` method to check if the string ends with "b". We then construct the `fizz` and `buzz` strings based on these conditions and concatenate them accordingly. This solution eliminates the need for multiple `if` statements by using more concise conditional expressions and string concatenation.




# https://www.codingdors.com/problem/194
"""
max_mod5
Show Solution
Given two int values, return whichever value is larger. However, if the two values have the same remainder when divided by 5, then the return the smaller value. However, in all cases, if the two values are the same, return 0.
max_mod5(10, 5) → 5
max_mod5(20, 15) → 15
max_mod5(10, 10) → 0

Theory
max_mod5
1. Conditional statements are used to take decisions based on certain conditions. In python, if, elif, and else are used for conditional statements. Example: 
if x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is a negative number")
2. Boolean Operators are used to combine conditional statements. Python has three Boolean operators: and, or, and not. Example:
if x > 0 and y > 0:
    print("Both x and y are positive numbers")
elif x > 0 or y > 0:
    print("At least one of x and y is a positive number")
3. Comparison Operators are used to compare values. Python has six comparison operators: ==, !=, >, <, >=, <=. Example:
if x == y:
    print("x and y are equal")
elif x != y:
    print("x and y are not equal")
else: 
    print("this will never run")
4. Arithmetic Operators are used to perform mathematical operations in Python. Python has seven arithmetic operators: +, -, *, /, %, //, and **. Example:
x = 10
y = 3
print(x + y)      # 13
print(x - y)      # 7
print(x * y)      # 30
print(x / y)      # 3.33333333333
print(x % y)      # 1
print(x // y)     # 3
print(x ** y)     # 1000
5. Logical Operators are used to combine multiple conditions and return a Boolean value. Python has two logical operators: and and or. Example:
if x > 0 and y > 0:
    print("Both x and y are positive")
elif x > 0 or y > 0:
    print("At least one of x and y is positive")
6. Functions are a group of related statements that perform a specific task when called. In python, a function is defined using the def keyword followed by function name and parameters enclosed in a parentheses. Example: 
def add_numbers(a, b):
    return a + b
sum = add_numbers(2, 5)
print(sum)   # 7
"""
# My Code
	def max_mod5(a: int, b: int) -> int:
		ra = a % 5
		rb = b % 5
		if ra == rb:
		  if a > b:
		    return b
		  elif a < b:
		    return a
		  else:
		    return 0
		else:
		  if a > b:
		    return a
		  else:
		    return b
		  
# Solution
	def max_mod5(a: int, b: int) -> int:
		ra = a % 5
		rb = b % 5
		if ra == rb:
		  if a > b:
		    return b
		  elif a < b:
		    return a
		  else:
		    return 0
		else:
		  if a > b:
		    return a
		  else:
		    return b
			  
# IA's Solutions
# 1. Using Conditional Operator:
def max_mod5(a: int, b: int) -> int:
    ra = a % 5
    rb = b % 5   
    return b if ra == rb and a > b else a if ra == rb and a < b else 0 if a == b else max(a, b)
# Explanation: In this solution, we use the conditional operator to check the conditions and return the appropriate result.
# 2. Using Ternary Operator:
def max_mod5(a: int, b: int) -> int:
    ra = a % 5
    rb = b % 5  
    return b if ra == rb and a > b else a if ra == rb and a < b else 0 if a == b else max(a, b)
# Explanation: This solution is similar to the first one but uses the ternary operator instead of if-else statements for a more concise code.
# 3. Using Python's built-in functions:
def max_mod5(a: int, b: int) -> int:
    if a == b:
        return 0     
    if a % 5 == b % 5:
        return min(a, b)
    else:
        return max(a, b)
# Explanation: This solution uses Python's built-in functions min() and max() to determine the result based on the given conditions. It also explicitly handles the case where a equals b and returns 0 in that case.





# https://www.codingdors.com/problem/277
"""
grade_convertor
Show Solution
Write a function grade_convertor(grade) that takes a grade as a percentage (0-100) and returns a string: "Fail" if the grade is less than 40, "Pass" if the grade is between 40 and 60, and "Excellent" if the grade is more than 60.
grade_convertor(30) -> 'Fail'
grade_convertor(40) -> 'Pass'
grade_convertor(60) -> 'Excellent'

Theory
grade_convertor
1. Conditionals are used to make decisions based on certain conditions. The most common conditional statements in programming are if statements and switch statements. Example: 
if x > 10:
    # do something
2. Functions are blocks of reusable code that perform a specific task. They are used to modularize code and make it more efficient. Example: 
def add(a, b) :
    return a + b
3. Variables are used to store and manipulate data in a program. They are declared with a name. Example: 
name = "Alice"
4. Operators are used to perform operations on values and variables in a program. There are many different kinds of operators, including arithmetic, comparison, and logical operators.  Example: 
result = 10 + 5

Hint
grade_convertor
1. Start by defining your function grade_convertor(grade). The function takes one argument, which is the grade as a percentage.
2. Use conditional statements (if, elif, and else) to check where the given grade falls in the categories.
3. If the grade is less than 40, you should return the string "Fail".
4. If the grade is between 40 and 60 (inclusive of both), you should return the string "Pass".
5. If the grade is greater than 60, you should return the string "Excellent".
6. Make sure to use the return statement to return the appropriate string based on the grade.
"""
# My Code
	def grade_convertor(grade: int) -> str:
	    if grade < 40:
	        return "Fail"
	    elif 40 <= grade < 60:
	        return "Pass"
	    else:
	        return "Excellent"

# Solution
	def grade_convertor(grade: int) -> str:
		if grade < 40:
		  return 'Fail'
		elif 40 <= grade < 60:
		  return 'Pass'
		else:
		  return 'Excellent'
			
# IA's Solutions
# Sure! Here is an alternative solution for the grade_convertor function in Python using a dictionary to map grade ranges to corresponding labels:
def grade_convertor(grade: int) -> str:
    grade_map = {
        range(0, 40): "Fail",
        range(40, 61): "Pass",
        range(61, 101): "Excellent"
    }
    for score_range, label in grade_map.items():
        if grade in score_range:
            return label
# In this solution, we define a dictionary `grade_map` where the keys are ranges of grades and the values are the corresponding labels. We then iterate over each key-value pair in the dictionary and check if the given grade falls within the range. If it does, we return the corresponding label. This approach can be useful if you want to easily update or expand the grade ranges and labels in the future.





# https://www.codingdors.com/problem/278
"""
check_temperature
Show Solution
Write a function check_temperature(temp) that takes a temperature as input (in Fahrenheit) and returns "Hot" if the temperature is above 80 degrees, "Warm" if the temperature is between 60 and 80 degrees, "Cool" if the temperature is between 40 and 60 degrees, and "Cold" if the temperature is below 40 degrees.
check_temperature(30) -> 'Cold'
check_temperature(40) -> 'Cool'
check_temperature(60) -> 'Warm'
check_temperature(80) -> 'Hot'

Theory
check_temperature
1. Conditionals are used to make decisions based on certain conditions. The most common conditional statements in programming are if statements and switch statements. Example: 
if x > 10:
    # do something
2. Functions are blocks of reusable code that perform a specific task. They are used to modularize code and make it more efficient. Example: 
def add(a, b) :
    return a + b
3. Variables are used to store and manipulate data in a program. They are declared with a name. Example: 
name = "Alice"
4. Operators are used to perform operations on values and variables in a program. There are many different kinds of operators, including arithmetic, comparison, and logical operators.  Example: 
result = 10 + 5

Hint
check_temperature
1. Start by defining your function check_temperature(temp). The function takes one argument, which is the temperature in Fahrenheit.
2. Use conditional statements (if, elif, and else) to check where the given temperature falls in the categories.
3. If the temperature is less than 40, you should return the string "Cold".
4. If the temperature is between 40 and 60 (inclusive of both), you should return the string "Cool".
5. If the temperature is between 60 and 80 (inclusive of both), you should return the string "Warm".
6. If the temperature is above 80, you should return the string "Hot".
7. Make sure to use the return statement to return the appropriate string based on the temperature.
"""
# My Code
	def check_temperature(temp: int) -> str:
		if temp < 40:
		  return 'Cold'
		elif 40 <= temp < 60:
		  return 'Cool'
		elif 60 <= temp < 80:
		  return 'Warm'
		else:
		  return 'Hot'
		
# Solution
	def check_temperature(temp: int) -> str:
		if temp < 40:
		  return 'Cold'
		elif 40 <= temp < 60:
		  return 'Cool'
		elif 60 <= temp < 80:
		  return 'Warm'
		else:
		  return 'Hot'
			
# IA's Solutions
# 1. Using a dictionary to store temperature ranges and corresponding labels:
def check_temperature(temp: int) -> str:
    temperature_ranges = {
        (float('-inf'), 40): 'Cold',
        (40, 60): 'Cool',
        (60, 80): 'Warm',
        (80, float('inf')): 'Hot'
    }

    for temp_range, label in temperature_ranges.items():
        if temp in range(*temp_range):
            return label
# This solution uses a dictionary to map temperature ranges to labels and iterates through the dictionary to find the appropriate label for the given temperature.
# 2. Using a ternary operator to simplify the if-elif-else structure:
def check_temperature(temp: int) -> str:
    return 'Cold' if temp < 40 else 'Cool' if temp < 60 else 'Warm' if temp < 80 else 'Hot'
# This solution utilizes a ternary operator to condense the conditional logic into a single line, making the code more concise.
