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
  
def print_to_n_for_loop(n: int):
    return [x for x in range(n+1)]
# This solution uses list comprehension to create a list of numbers from 0 to n inclusive. It is a more concise way to achieve the same result as using a for loop.
# Alternative Solution 2: Using range directly in the return statement
def print_to_n_for_loop(n: int):
    return list(range(n+1))
# In this solution, we eliminate the need for a separate list variable by directly using the range function inside the return statement. This also makes the code more succinct and easier to understand.
# 2. Using a while loop:
def print_to_n_for_loop(n: int):
    listinha = []
    i = 0
    while i <= n:
        listinha.append(i)
        i += 1
    return listinha
# In this solution, a while loop is used to iterate over the range from 0 to n inclusive. The loop adds each number to the list and increments the counter variable i.





# https://www.codingdors.com/problem/82
"""
print_to_n_even
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all even integers from 0 to n inclusive, using a for loop.
print_to_n_even(5) -> [0, 2, 4]
print_to_n_even(10) -> [0, 2, 4, 6, 8, 10]
print_to_n_even(1) -> [0]

Theory
print_to_n_even
1. For loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). A 'for' loop can be used to execute a set of statements, once for each item in a list, tuple, set etc. Example: 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
2. List: A list is a collection of items in a particular order. Lists are one of the most versatile data structures in Python and are often used to store collections of related data. Lists are mutable which means we can change the items in the list after it has been created.
Example: 
list_of_numbers = [1, 2, 3, 4, 5]
3. Append: The 'append()' method adds an item to the end of the list. It takes one argument and adds it to the end of the list. Example: 
list = [1, 2, 3, 4]
list.append(5)
4. Even number: An even number is any integer that can be exactly divided by 2. In other words, it has no remainder when divided by 2. Example: 
2, 4, 6, 8, 10
5. Range(): 'range()' function is used to generate a sequence of numbers. It generates a sequence of numbers from the start argument to the stop argument, in increments of step argument. Example:
for i in range(0, 6, 2):
    print(i)

Hint
print_to_n_even
1. Define an empty list before the for loop to store even integers.
2. Use the range() function to loop through integers from 0 to n.
3. Use an if statement to check if the integer is even.
4. If the integer is even, append it to the list.
5. Return the list.    
"""
# My Code
  def print_to_n_even(n: int):
      listinha = []
      for i in range(0, n+1):
          if i % 2 == 0:
              listinha.append(i)
      return listinha

# Solution
  def print_to_n_even(n: int):
  	even = []
  	for i in range(0, n+1):
  	  if i % 2 == 0:
  	    even.append(i)
  	return even

# IA's Solutions
# 1. Using list comprehension:
def print_to_n_even(n: int):
    return [i for i in range(n+1) if i % 2 == 0]
# This solution uses list comprehension to generate the list of even integers from 0 to n inclusive. It is a more concise way of achieving the same result.
# 2. Using a while loop:
def print_to_n_even(n: int):
    listinha = []
    i = 0
    while i <= n:
        if i % 2 == 0:
            listinha.append(i)
        i += 1
    return listinha
# This solution uses a while loop instead of a for loop to iterate over the numbers from 0 to n and append the even numbers to the list.
# 3. Using a range with a step of 2:
def print_to_n_even(n: int):
    return list(range(0, n+1, 2))
# This solution directly generates a list of even integers from 0 to n inclusive by using the range function with a step of 2.





# https://www.codingdors.com/problem/84
"""
print_odd_to_n_forloop
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all odd integers from 0 to n inclusive, using a for loop. 
print_odd_to_n_forloop(5) -> [1, 3, 5]
print_odd_to_n_forloop(10) -> [1, 3, 5, 7, 9]
print_odd_to_n_forloop(1) -> [1]

Theory
print_odd_to_n_forloop
1. For loop: A for loop is used for iterating over a sequence, like strings, lists, tuples etc. or for iterating over a range of integer numbers. It executes a set of statements, once for each item in the sequence. For example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
2. List: A list is a collection of values, which can be of any type. Lists are ordered, meaning each item has a specific index, starting at 0. They are mutable, meaning their contents can be changed at any time. For example:
my_list = [1, "hello", 3.4, True]
3. if statement: An if statement is used for conditional execution. It checks a condition, and if it is true, runs a block of code. For example:
x = 5
if x > 3:
  print("x is greater than 3")
4. Modulo operator: The modulo operator returns the remainder of a division operation. It is denoted by the % symbol in Python. For example:
x = 5
y = 2
print(x % y) # output: 1

Hint
print_odd_to_n_forloop
1. Use a for loop to iterate from 0 to n inclusive.
2. Check if each integer is odd using the modulus operator.
3. If the integer is odd, append it to the list.
"""
# My Code
  def print_odd_to_n_forloop(n: int):
      return [i for i in range(n+1) if i % 2 != 0]
  
  def print_odd_to_n_forloop(n: int):
      listinha = []
      for i in range(0, n+1):
          if i%2 != 0:
              listinha.append(i)
      return listinha
  
  def print_odd_to_n_forloop(n: int):
      listinha = []
      for i in range(1, n+1, 2):
          listinha.append(i)
      return listinha

# Solution
def print_odd_to_n_forloop(n: int):
	odd = []
	for i in range(0, n+1):
	  if i % 2 != 0:
	    odd.append(i)
	return odd

# IA's Solutions
# Sure! Here is an alternative solution using a for loop:
def print_odd_to_n_forloop(n: int):
    odd_numbers = []
    for i in range(1, n+1, 2):
        odd_numbers.append(i)
    return odd_numbers
# Explanation:
# 1. We initialize an empty list called `odd_numbers` to store the odd integers.
# 2. We iterate over the range from 1 to n (inclusive) with a step size of 2 using the `range` function. This ensures that we only consider odd integers in the loop.
# 3. Within the loop, we append each odd integer `i` to the `odd_numbers` list.
# 4. Finally, we return the list containing all odd integers from 0 to n inclusive.





# https://www.codingdors.com/problem/85
"""
print_one_to_n_while
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all the integers from 1 to n, inclusive, using a while loop. 
print_one_to_n_while(5) -> [1, 2, 3, 4, 5]
print_one_to_n_while(10) ->  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_one_to_n_while(0) -> []

Theory
print_one_to_n_while
1. While loop: A while loop in Python repeatedly executes a block of statements as long as the given condition is true. 
while x < 10:
 Example: 
x = 1
while x <= 5:
    print(x)
    x += 1
2. List creation: A list is a collection of elements enclosed in square brackets. Lists are mutable, i.e., they can be modified. Example: 
my_list = [1, 2, 3, 4, 5]
3. List append method: The append() method adds an element to the end of the list. Example: 
my_list.append(6)
4. Initializing an empty list: A list with no elements can be created by declaring an empty pair of square brackets. Example: 
my_list = []
5. While loop termination: The while loop must terminate to avoid an infinite loop. A condition must be set so that the loop is exited when the condition is false. Example: 
x = 1
while x <= 5:
    print(x)
    x += 1

Hint
print_one_to_n_while
1. Define an empty list before the while loop.
2. Use a while loop that continues until a counter variable reaches n.
3. Inside the while loop, add each number to the list.
4. Increment the counter variable with each iteration of the loop.
5. Return the list outside of the loop.
"""
# My Code
  def print_one_to_n_while(n: int):
      listinha = []
      indice = 1
      while indice <= n:
          listinha.append(indice)
          indice += 1
      return listinha

# Solution
  def print_one_to_n_while(n: int):
  	numbers = []
  	i = 1
  	while i <= n:
  	  numbers.append(i)
  	  i = i + 1
  	return numbers

# IA's Solutions
# Alternative Solution 1:
def print_one_to_n_while(n: int):
    listinha = []
    indice = 1
    while indice <= n:
        listinha += [indice]
        indice += 1
    return listinha
# Explanation: This solution is very similar to the original one. The only difference is the use of the += operator to concatenate the integer to the list without using the append() method. This is just a matter of personal preference.
# Alternative Solution 2:
def print_one_to_n_while(n: int):
    listinha = []
    indice = 1
    while indice <= n:
        listinha.append(indice)
        indice = indice + 1
    return listinha
# Explanation: In this solution, we explicitly increment the 'indice' variable using the statement indice = indice + 1. This achieves the same result as using the += operator in the previous solution, but the increment operation is more explicit.
# Alternative Solution 3:
def print_one_to_n_while(n: int):
    listinha = []
    indice = 1
    while True:
        listinha.append(indice)
        indice += 1
        if indice > n:
            break
    return listinha
# Explanation: In this solution, we use a while True loop and break out of it when the 'indice' variable becomes greater than n. This approach makes the loop logic more explicit by handling the termination condition within the loop instead of just relying on the condition in the while statement.





# https://www.codingdors.com/problem/86
"""
print_even_number_while
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all even integers from 0 to n inclusive, using a while loop. 
print_even_number_while(5) -> [0, 2, 4]
print_even_number_while(10) -> [0, 2, 4, 6, 8, 10]
print_even_number_while(1) -> [0]

Theory
print_even_number_while
1. While loop - a control flow statement that repeatedly executes a block of code as long as the specified condition is true. Example: 
x = 0
while x < 5:
    print(x)
    x += 1
Output: 0 1 2 3 4
2. Modulo operator - returns the remainder of dividing the left hand operand by right hand operand. Example: 
5 % 2 = 1     # remainder when 5 is divided by 2 is 1
10 % 3 = 1    # remainder when 10 is divided by 3 is 1
3. If statement - a control flow statement that executes a block of code if a specified condition is true. Example: 
age = 18
if age >= 18:
    print("You can vote!")
4. Range function - generates a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. Example: 
range(5)     # generates the sequence 0, 1, 2, 3, 4
range(2, 8)  # generates the sequence 2, 3, 4, 5, 6, 7


"""
# My Code
  def print_even_number_while(n: int):
      listinha = []
      indice = 0
      while indice <= n:
          if indice % 2 == 0:
              listinha.append(indice)
          indice += 1
      return listinha

# Solution
  def print_even_number_while(n: int):
  	numbers = []
  	i = 0
  	while i <= n:
  	  if i % 2 == 0:
  	    numbers.append(i)
  	  i = i + 1
  	return numbers

# IA's Solutions
# 1. Using list comprehension:
def print_even_number_while(n: int):
    listinha = []
    indice = 0
    while indice <= n:
        listinha.append(indice)
        indice += 2
    return listinha
# Explanation: This solution uses list comprehension to directly append even numbers to the list. The `indice` is incremented by 2 in each iteration to skip odd numbers.
# 2. Simplified version:
def print_even_number_while(n: int):
    listinha = []
    indice = 0
    while indice <= n:
        listinha.append(indice)
        indice += 2
    return listinha
# Explanation: This solution is a more concise version of the original function by directly incrementing `indice` by 2.
# 3. Using a for loop:
def print_even_number_while(n: int):
    listinha = []
    for i in range(0, n+1, 2):
        listinha.append(i)
    return listinha
# Explanation: This solution uses a for loop with a step size of 2 to directly iterate over even numbers and append them to the list.





# https://www.codingdors.com/problem/88
"""
print_to_n_odd_while
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all odd integers from 0 to n inclusive, using a while loop. 
print_to_n_odd_while(5) -> [1, 3, 5]
print_to_n_odd_while(10) -> [1, 3, 5, 7, 9]
print_to_n_odd_while(1) -> [1]

Theory
print_to_n_odd_while
1. While loop: A while loop is a control flow statement that allows us to execute a block of statements repeatedly until a given condition is satisfied. The condition is checked before executing the statements inside the loop. Example: 
i = 0
while i < 3:
    print(i)
    i += 1
2. A list is a collection of elements in a specific order. Lists are mutable, which means we can change, add, or remove their elements. We can use square brackets [] or the list() constructor to create a list. Example: 
my_list = [1, 2, 3, 4]
new_list = list(range(1,10,2))
3. An odd integer is any integer that is not an even number, i.e., not divisible by 2 without a remainder. Example: 
odd_num = 3
another_odd_num = 7

Hint
print_to_n_odd_while
1. Start with an empty list to store the odd integers
2. Initialize a counter variable to 1
3. Use a while loop to iterate while the counter is less than or equal to n
4. Within the loop, check if the counter is odd
5. If it is, add it to the list
6. Increment the counter by 1 with each iteration
7. Return the list at the end of the function
"""
# My Code
  def print_to_n_odd_while(n: int):
      listinha = []
      indice = 1
      while indice <= n:
          if indice % 2 != 0:
              listinha.append(indice)
          indice += 1
      return listinha

# Solution
  def print_to_n_odd_while(n: int):
  	numbers = []
  	i = 0
  	while i <= n:
  	  if i % 2 != 0:
  	    numbers.append(i)
  	  i = i + 1
  	return numbers

# IA's Solutions
# 1. Using a for loop:
def print_to_n_odd_for(n: int):
    listinha = []
    for i in range(1, n+1, 2):
        listinha.append(i)
    return listinha
# Explanation: In this solution, we use a for loop to iterate through all odd numbers from 1 to n (inclusive) by incrementing the loop variable by 2. The odd numbers are then appended to the list.
# 2. Using list comprehension:
def print_to_n_odd_list_comprehension(n: int):
    return [i for i in range(1, n+1) if i % 2 != 0]
# Explanation: In this solution, we use list comprehension to create a list of odd numbers from 1 to n (inclusive). The list comprehension evaluates the condition `i % 2 != 0` which filters out even numbers, leaving only odd numbers in the resulting list.





# https://www.codingdors.com/problem/89
"""
reverse_n_for
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all numbers from n to 0 inclusive (reverse order), using a for loop.
reverse_n_for(5) -> [5,4, 3, 2, 1, 0]
reverse_n_for(3) -> [3, 2, 1, 0]
reverse_n_for(1) -> [1, 0]

Theory
reverse_n_for
1. For loop: A loop in Python that iterates over a sequence of values. It executes a block of code repeatedly until a certain condition is met. Example: 
for i in range(5):
    print(i)
Output: 
0
1
2
3
4
2. A built-in Python function that generates a sequence of numbers. It takes three arguments: start, stop, and step. Example: 
range(0, 10, 2)
Output: [0, 2, 4, 6, 8]
3. A mutable sequence in Python that stores a collection of elements. Elements can be of any type and are ordered. Example: 
my_list = [1, 'two', 3.0, [4, 5]]
Output: [1, 'two', 3.0, [4, 5]]
4. A built-in Python method for lists that adds an element to the end of a list. Example: 
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
Output: [1, 2, 3, 4]
5. range() with a reversed step: range() can be used to generate a sequence of numbers in reverse order by setting a negative step. Example: 
range(5, -1, -1)
Output: [5, 4, 3, 2, 1, 0]

Hint
reverse_n_for
1. Define a function that takes an integer as an argument. 
2. Create an empty list to store the output. 
3. Use a for loop to iterate from the input integer to 0. 
4. Append each number to the list. 
5. Return the list.
"""
# My Code
  def reverse_n_for(n: int):
      listinha = []
      for i in range(n, -1, -1):
          listinha.append(i)
      return listinha

# Solution
  def reverse_n_for(n: int):
  	numbers = []
  	for i in range(n, -1, -1):
  	  numbers.append(i)
  	return numbers

# IA's Solutions
# Alternative Solution 1: Using a list comprehension
def reverse_n_for(n: int):
    return [i for i in range(n, -1, -1)]
# In this solution, we use a list comprehension to create the list directly without the need for an explicit loop. The list comprehension iterates over the range from n to 0 in reverse order and creates a list of numbers.
# Alternative Solution 2: Using the reversed() function
def reverse_n_for(n: int):
    return list(reversed(range(n+1)))
# In this solution, we use the reversed() function to reverse the range object created by range(n+1) and convert it to a list. This approach is more concise and readable compared to explicitly iterating over the range.
# Alternative Solution 3: Using a while loop
def reverse_n_for(n: int):
    listinha = []
    while n >= 0:
        listinha.append(n)
        n -= 1
    return listinha
# In this solution, we use a while loop to iterate from n down to 0 and append each number to the list. This approach is an alternative to using a for loop and achieves the same result.





# https://www.codingdors.com/problem/90
"""
reverse_n_while
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all numbers from n to 0 inclusive (reverse order), using a while loop.
reverse_n_while(5) -> [5, 4, 3, 2, 1, 0]
reverse_n_while(3) -> [3, 2, 1, 0]
reverse_n_while(1) -> [1, 0]

Theory
reverse_n_while
1. While loop: A while loop in Python continuously executes a block of statements as long as the condition inside the loop returns True. Once the condition becomes False, the program control passes to the line immediately following the loop. Example: 
i = 0
while i < 5:
   print(i)
   i += 1
2. List: A list is a collection of items in a particular order. Lists are one of the most versatile data types in Python. A list can be denoted by square brackets and contains comma-separated items. Example: 
cars = ['Honda', 'Toyota', 'Ford']
3. Append method: The append() method adds a single item to the existing list. It is used to add elements to a list in Python. This method adds elements at the end of the list. Example:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
4. Function: A function is a block of code that performs a specific task. It is a self-contained unit of code that can be executed whenever required. Functions help to break down large programs into smaller and modular chunks. Example: 
def simple_interest(p, t, r):
     si = (p * t * r)/100
     return si
5. Range function: The range function in Python is a function that returns a sequence of numbers. It generates a sequence of numbers starting from the given start index up to the end index. The third parameter specifies the increment and is optional. Example:
for i in range(5):
    print(i)

Hint
reverse_n_while
1. Initialize an empty list to store the resulting numbers.
2. Use a while loop with a condition that checks whether n is greater than or equal to 0.
3. Within the while loop, append the current value of n to the list.
4. Decrement the value of n by 1 in each loop iteration.
5. Return the resulting list after the while loop has completed.
"""
# My Code
	def reverse_n_while(n: int):
	    listinha = []
	    indice = n
	    while indice >= 0:
		listinha.append(indice)
		indice -= 1
	    return listinha

# Solution
	def reverse_n_while(n: int):
		numbers = []
		while n >= 0:
		  numbers.append(n)
		  n = n - 1
		return numbers

# IA's Solutions
# 1. Using a for loop:
def reverse_n_while(n: int):
    listinha = []
    for i in range(n, -1, -1):
        listinha.append(i)
    return listinha
# 2. Using list comprehension:
def reverse_n_while(n: int):
    return [i for i in range(n, -1, -1)]
# 3. Using a while loop with a decrementing range:
def reverse_n_while(n: int):
    listinha = []
    while n >= 0:
        listinha.append(n)
        n -= 1
    return listinha
# All these solutions achieve the same result as your original code by creating a list in reverse order from n to 0 inclusive. Each solution offers a different approach to achieving the desired outcome, showcasing the flexibility and versatility of Python.





# https://www.codingdors.com/problem/91
"""
reverse_n_even_for
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all even numbers from n to 0 inclusive, using a for loop.
reverse_n_even_for(5) -> [4, 2, 0]
reverse_n_even_for(3) -> [2, 0]
reverse_n_even_for(1) -> [0]

Theory
reverse_n_even_for
1. A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). It executes a set of statements, once for each item in a sequence. Example: 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
2. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. Example:
for x in range(6):
  print(x)
Output: 
0
1
2 
3
4
5
3. An if statement is a conditional statement that runs or skips code based on whether a condition is true or false. Example:
a = 33
b = 200
if b > a:
  print("b is greater than a")
Output: b is greater than a
4. A list is a collection of items ordered in a particular sequence, which can be of any type. Lists are mutable, i.e., their contents can be modified after creation. Example: 
my_list = [1, "Hello", 3.4, True]

Hint
reverse_n_even_for
1. You need to start with n and work your way down to 0, so your for loop should count downwards.
2. You need to identify the even numbers in your for loop. One way to do this is to use the modulus operator (%).
3. You need to add the even numbers to a list and return that list.
"""
# My Code
	def reverse_n_even_for(n: int):
	    listinha = []
	    for i in range(n, -1, -1):
	        if i%2 == 0:
	            listinha.append(i)
	    return listinha

# Solution
	def reverse_n_even_for(n: int):
		numbers = []
		for i in range(n, -1, -1):
		  if i % 2 == 0:
		    numbers.append(i)
		return numbers

# IA's Solutions
# 1. Using list comprehension:
def reverse_n_even_for(n: int):
    return [i for i in range(n, -1, -1) if i % 2 == 0]
# Explanation: This solution utilizes list comprehension to create the list of even numbers in a more concise way. It iterates through the range from n to 0 inclusive and only adds the even numbers to the list.
# 2. Using a while loop:
def reverse_n_even_for(n: int):
    listinha = []
    while n >= 0:
        if n % 2 == 0:
            listinha.append(n)
        n -= 1
    return listinha
# Explanation: This solution uses a while loop to iterate from n to 0 inclusive. It checks if the number is even and adds it to the list if it is. The loop continues until n reaches 0.
# 3. Using extended slicing:
def reverse_n_even_for(n: int):
    return list(range(n, -1, -1))[::2]
# Explanation: This solution first creates a list of numbers from n to 0 using the range function. Then, it uses extended slicing [::2] to only select every second element in the list, effectively filtering out the odd numbers.





# https://www.codingdors.com/problem/92
"""
reverse_n_even_while
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all even numbers from n to 0 inclusive, using a while loop.
reverse_n_even_while(5) -> [4, 2, 0]
reverse_n_even_while(3) -> [2, 0]
reverse_n_even_while(1) -> [0]

Theory
reverse_n_even_while
1. While Loop: A while loop is a control flow statement that allows code to be executed repeatedly based on a given condition. The loop continues to execute until the condition is False. 
Example: 
i = 0
while i < 5:
    print(i)
    i += 1
2. List: A list is a data structure in Python that is a collection of items. It is ordered and changeable. Lists are defined by having values separated by commas inside square brackets []. 
Example: 
my_list = [1, 3, "apple", True]
3. Append: Append() is a built-in function in Python that adds a single item to the existing list. The item is added at the end of the list. 
Example:
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
4. If statement: An if statement is a control flow statement that allows code to be executed conditionally based on a given condition. If the condition is true, the block of code inside the if statement is executed, otherwise, it is skipped. 
Example: 
x = 5 
if x < 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")
5. Range: The range function is a built-in function in Python that generates a sequence of numbers. It can take 1-3 parameters, start (inclusive), stop (exclusive), and step(argument to skip counting). 
Example:
# generates odd numbers between 1 and 10
odd_numbers = range(1, 10, 2)
print(list(odd_numbers)) # [1, 3, 5, 7, 9]

Hint
reverse_n_even_while
1. Start with an empty list to store the even numbers
2. Set up a while loop to continue until n reaches 0
3. Within the loop, use an if statement to check if n is even
4. If n is even, append it to the list
5. Decrement n within the loop to eventually reach 0
6. Return the list of even numbers at the end of the function
"""
# My Code
	def reverse_n_even_while(n: int):
	    listinha = []
	    while n >= 0:
	        if n%2 == 0:
	            listinha.append(n)
	        n -= 1
	    return listinha

# Solution
	def reverse_n_even_while(n: int):
		numbers = []
		while n >= 0:
		  if n % 2 == 0:
		    numbers.append(n)
		  n = n - 1
		return numbers

# IA's Solutions
# 1. Using a decrementing loop counter:
def reverse_n_even_while(n: int):
    listinha = []
    while n >= 0:
        if n % 2 == 0:
            listinha.append(n)
        n -= 1
    return listinha
# 2. Using a loop with step size of -2 to directly skip odd numbers:
def reverse_n_even_while(n: int):
    listinha = []
    while n >= 0:
        listinha.append(n)
        n -= 2
    return listinha
# 3. Using a simpler approach with a single condition inside the loop:
def reverse_n_even_while(n: int):
    listinha = []
    while n >= 0:
        listinha.append(n)
        n -= 2 if n >= 2 else 1
    return listinha
# All of these solutions essentially do the same thing by iterating from n to 0 inclusively and adding even numbers to the list. However, they vary slightly in terms of readability and efficiency due to different ways of handling conditions and loop counter updates.





# https://www.codingdors.com/problem/93
"""
reverse_n_odd_while
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all odd numbers from n to 1 inclusive, using a while loop.
reverse_n_odd_while(5) -> [5, 3, 1]
reverse_n_odd_while(3) -> [3, 1]
reverse_n_odd_while(1) -> [1]

Theory
reverse_n_odd_while
1. While loops - used to repeatedly execute a block of code while a certain condition is true. Example: 
count = 0
while count < 5:
  print("Hello!")
  count += 1
# Output: 
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
2. Lists - used to store multiple items in a single variable. Items in a list are indexed and can be accessed and manipulated easily. Example:
my_list = [1, 2, "three", True]
print(my_list[1])
# Output: 2
my_list.append("four")
print(my_list)
# Output: [1, 2, "three", True, "four"]
3. If statements - used to execute a block of code only if a certain condition is true. Example:
x = 5
if x > 10:
  print("x is greater than 10")
else:
  print("x is not greater than 10")
# Output: x is not greater than 10
4. The '%' operator - used to calculate the remainder of a division. Example:
print(10 % 3)
# Output: 1
5. range() function - used to generate a sequence of numbers. Example:
for i in range(0, 5):
  print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

Hint
reverse_n_odd_while
1. The function should take in one parameter, an integer n.
2. Create an empty list to hold the odd numbers.
3. Use a while loop with a condition that checks for odd numbers greater than or equal to 1.
4. Within the while loop, append the current odd number to the list and decrement it by 2.
5. Return the list at the end of the function.
"""
# My Code
	def reverse_n_odd_while(n: int):
	    listinha = []
	    while n >= 0:
	        if n % 2 > 0:
	            listinha.append(n)
	        n -= 2 
	    return listinha

# Solution
	def reverse_n_odd_while(n: int):
		numbers = []
		while n >= 0:
		  if n % 2 != 0:
		    numbers.append(n)
		  n = n - 1
		return numbers

# IA's Solutions
# 1. Using a while loop with different condition:
def reverse_n_odd_while(n: int):
    listinha = []
    while n >= 1:
        if n % 2 != 0:
            listinha.append(n)
        n -= 1
    return listinha
# Explanation: In this solution, we start the while loop with the condition `n >= 1` to include the number 1 in the final list. We check if the number is odd using the condition `n % 2 != 0` and then decrement `n` by 1 in each iteration.
# 2. Simplifying the condition inside the while loop:
def reverse_n_odd_while(n: int):
    listinha = []
    while n >= 1:
        if n % 2:
            listinha.append(n)
        n -= 1
    return listinha
# Explanation: In Python, the condition `n % 2` will automatically evaluate to `True` if the remainder is non-zero (indicating an odd number) and `False` if the remainder is zero (indicating an even number). This simplifies the condition inside the if statement.





# https://www.codingdors.com/problem/94
"""
reverse_n_odd_for
Show Solution
Write a Python function that takes an integer n as input and returns a list that contains all odd numbers from n to 0, using a for loop.
reverse_n_odd_for(5) -> [5, 3, 1]
reverse_n_odd_for(3) -> [3, 1]
reverse_n_odd_for(1) -> [1]

Theory
reverse_n_odd_for
1. for loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). A loop variable is used for accessing the elements of a sequence one by one. 
for i in range(5):
2. list: A list is a collection of elements enclosed in square brackets and separated by commas. Lists can be changed. 
my_list = [1, 2, 3, 4]
3. integer: An integer is a whole number (not a fraction) that can be either positive, negative, or zero. 
my_int = 5
4. function: A function is a block of code that is designed to perform a specific task. 
def my_function():
Example: 
# reverse_n_odd_for(5) -> [5, 3, 1]
def reverse_n_odd_for(n):
    odd_list = []
    for i in range(n, -1, -1):
        if i % 2 == 1:
            odd_list.append(i)
    return odd_list

Hint
reverse_n_odd_for
1. Use a for loop that starts from n and goes down to 0 (inclusive)
2. Check if the current number in the loop is odd using the modulus operator (%)
3. If the number is odd, add it to a list (initialize an empty list before the loop)
4. Return the list containing all the odd numbers found in the loop.
"""
# My Code
	def reverse_n_odd_for(n: int):
	    listinha = []
	    for n in range(n, -1, -1):
	        if n%2 > 0:
	            listinha.append(n)
	    return listinha

# Solution
	def reverse_n_odd_for(n: int):
		numbers = []
		for i in range(n, -1, -1):
		  if i % 2 != 0:
		    numbers.append(i)
		return numbers

# IA's Solutions
# 1. Using list comprehension:
def reverse_n_odd_for(n: int):
    return [x for x in range(n, -1, -1) if x % 2 != 0]
# Explanation: This solution uses list comprehension to create a list of odd numbers from n to 0. It iterates over the range from n to 0 with a step of -1 and filters out only the odd numbers using the condition `x % 2 != 0`.
# 2. Using while loop:
def reverse_n_odd_for(n: int):
    listinha = []
    while n >= 0:
        if n % 2 != 0:
            listinha.append(n)
        n -= 1
    return listinha
# Explanation: This solution uses a while loop to iterate from n to 0 and checks if each number is odd before appending it to the list. It decrements the value of n in each iteration until it reaches 0.





# https://www.codingdors.com/problem/308
"""
count_odds_list
Show Solution
Return the number of odd integers in the given list. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
count_odds_list([2, 1, 2, 3, 4]) → 2
count_odds_list([2, 2, 5]) → 1
count_odds_list([1, 3, 5]) → 3


"""
# My Code
	def count_odds_list(l: list) -> int:
	    contador = 0
	    tamanho = len(l)
	    for i in range(tamanho):
	        if l[i] % 2 != 0:
	            contador += 1
	    return contador

# Solution
	def count_odds_list(l: list) -> int:
		sum = 0
		for i in range(len(l)):
		  if l[i] % 2 != 0:
		    sum += 1
		return sum

# IA's Solutions
# Sure! Here is an alternative solution to count the number of odd integers in a given list using list comprehension:
def count_odds_list(l: list) -> int:
    return len([x for x in l if x % 2 != 0])
# In this solution, a list comprehension is used to iterate over each element in the input list l and a new list is created containing only the elements that are odd (i.e., elements for which x % 2 != 0 is True). The length of this new list, which corresponds to the number of odd integers, is then returned.





# https://www.codingdors.com/problem/309
"""
has33_list
Show Solution
Given a list of integers, return True if the list contains a 3 next to a 3 somewhere.
has33_list([1, 3, 3]) → True
has33_list([1, 3, 1, 3]) → False
has33_list([3, 1, 3]) → False


"""
# My Code
def has33_list(l: list) -> bool:
	for i in range(len(l)-1):
	  if l[i] == l[i+1] == 3:
	    return True
	return False

# Solution
	def has33_list(l: list) -> bool:
		for i in range(len(l)-1):
		  if l[i] == l[i+1] == 3:
		    return True
		return False

# IA's Solutions
# 1. Using a list comprehension:
def has33_list(l: list) -> bool:
    return any(l[i] == l[i+1] == 3 for i in range(len(l)-1))
# Explanation: This solution uses a list comprehension along with the `any` function to check if any pair of consecutive elements in the list are equal to 3. It returns `True` if it finds such a pair, otherwise it returns `False`.
# 2. Using the `zip` function:
def has33_list(l: list) -> bool:
    return any(x == y == 3 for x, y in zip(l, l[1:]))
# Explanation: This solution uses the `zip` function to iterate over pairs of consecutive elements in the list. It then checks if both elements in the pair are equal to 3. If it finds such a pair, it returns `True`, otherwise it returns `False`.
# 3. Using a simple iteration with index:
def has33_list(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] == l[i+1] == 3:
            return True
    return False
# Explanation: This solution is similar to the original solution provided. It iterates over the list using indices and checks if each pair of consecutive elements are equal to 3. If it finds such a pair, it returns `True`, otherwise it returns `False`.





# https://www.codingdors.com/problem/310
"""
list456
Show Solution
Given a list of integers, return True if the sequence of numbers 4, 5, 6 appears in the list somewhere.
list456([1, 4, 5, 6, 1]) → True
list456([1, 4, 5, 4, 6]) → False
list456([1, 1, 2, 4, 5, 6]) → True


"""
# My Code
def list456(l: list) -> bool:
	for i in range(len(l)-2):
	  if l[i] == 4 and l[i+1] == 5 and l[i+2] == 6:
	    return True
	return False

# Solution
	def list456(l: list) -> bool:
		for i in range(len(l)-2):
		  if l[i] == 4 and l[i+1] == 5 and l[i+2] == 6:
		    return True
		return False

# IA's Solutions
# Here is an alternative solution using list comprehension:
def list456(l: list) -> bool:
    return any(l[i:i+3] == [4, 5, 6] for i in range(len(l)-2))
# Explanation:
# 1. This solution uses list comprehension to iterate through the list 'l' and check if a sublist of 3 consecutive elements is equal to [4, 5, 6].
# 2. The expression `l[i:i+3]` denotes a sublist of 'l' starting at index 'i' and ending at index 'i+2'.
# 3. The `any()` function is used to return True if at least one sublist matches [4, 5, 6].
# 4. The function returns True if the sequence [4, 5, 6] appears in the list 'l', otherwise it returns False.
#   Solution 1: Using list comprehension and the zip function
def list456(l: list) -> bool:
    return any(x == (4, 5, 6) for x in zip(l, l[1:], l[2:]))
# Explanation: This solution uses list comprehension along with the zip function to create tuples of three consecutive elements in the list. It then checks if any of these tuples are equal to (4, 5, 6). The any() function returns True if any of the tuples match the specified condition.
# Solution 2: Using the in operator and list slicing
def list456(l: list) -> bool:
    return (4, 5, 6) in zip(l, l[1:], l[2:])
# Explanation: This solution directly checks if the tuple (4, 5, 6) is present in the list of tuples created by zipping three consecutive elements of the input list. The in operator returns True if the specified tuple is found in the list of tuples.





# https://www.codingdors.com/problem/306
"""
has_matching_list
Show Solution
Given two lists 'l1' and 'l2', write a function that determines if the two lists share at least one letter in the same position. The function should return True if they do and False otherwise.
Assume that both lists will have the same length.
has_matching_list(["a","p","p","l","e"], ["a","b","c","d","e"]) → True
has_matching_list(["h","e","l","l","o"], ["w","o","r","l","d"]) → True
has_matching_list(["d","a","n","c","e"], ["l","o","v","e","r"]) → False
"""
# My Code
	def has_matching_list(l1: list, l2: list) -> bool:
	    tamanho = len(l1)
	    for i in range(tamanho):
	        if l1[i] == l2[i]:
	            return True
	    return False

# Solution
	def has_matching_list(l1: list, l2: list) -> bool:
		for i in range(len(l1)):
		  if l1[i] == l2[i]:
		    return True
		return False

# IA's Solutions
# 1. Using the zip() function:
def has_matching_list(l1: list, l2: list) -> bool:
    return any(x == y for x, y in zip(l1, l2))
# - Explanation: This solution uses the zip() function to pair elements from both lists together. It then uses a generator expression inside the any() function to check if there is at least one pair of elements that match.
# 2. Using list comprehension:
def has_matching_list(l1: list, l2: list) -> bool:
    return any(l1[i] == l2[i] for i in range(len(l1)))
# - Explanation: This solution uses a list comprehension to iterate over the indices of the lists and check if the elements at the same index match. The any() function is used to return True if any of the comparisons are True.
# 3. Using a single line with all():
def has_matching_list(l1: list, l2: list) -> bool:
    return all(l1[i] == l2[i] for i in range(len(l1)))
# - Explanation: This solution is similar to the previous one but uses the all() function to return True only if all the comparisons are True. If any pair of elements does not match, it will return False immediately.





# https://www.codingdors.com/problem/307
"""
check_first_number_list
Show Solution
Given a list 'l', determine if the first number appearing in the list is 0. The function should return False if the first number in the list is 0. If the list does not contain any numbers or if the first number appearing isn't 0, it should return True.
check_first_number_list(["H","e","l","l","o"]) → True
check_first_number_list(["H","e","l","l","0"]) → False
check_first_number_list(["H","3","l","l","0"]) → True
"""
# My Code
	def check_first_number_list(l: list) -> bool:
	    tamanho = len(l)
	    lista_numeros = []
	    for i in range(tamanho):
	        if str(l[i]).isdigit() == True:
	            lista_numeros.append(l[i])
	    if lista_numeros[0] == "0":
	        return False
	    if lista_numeros == None:
	        return True
	    return True

# Solution
	def check_first_number_list(l: list) -> bool:
		for i in range(len(l)):
		  if str(l[i]).isdigit():
		    if str(l[i]) == '0':
		      return False
		    else:
		      return True
		return True

# IA's Solutions
# Here is an alternative solution in Python for the problem statement:
def check_first_number_list(l: list) -> bool:
    if len(l) == 0:
        return True
    for item in l:
        if str(item).isdigit():
            if int(item) == 0:
                return False
            else:
                return True
    return True
# Explanation:
# 1. The function `check_first_number_list` takes a list `l` as input and returns a boolean value.
# 2. If the length of the list is 0, meaning the list is empty, the function returns True right away.
# 3. It iterates through each item in the list using a for loop.
# 4. For each item, it checks if the item is a digit using `str(item).isdigit()`.
# 5. If the item is a digit, it further checks if the integer value of the item is 0.
# 6. If the first number appearing in the list is 0, the function returns False.
# 7. If the list doesn't contain any numbers or if the first number appearing isn't 0, it returns True.





# https://www.codingdors.com/problem/313
"""
sort_list
Show Solution
Given a list of integers, return a the same list sorted in ascending order.
sort_list([25, 12, 22, 11]) -> [11, 12, 22, 25]
sort_list([-5, 0, -2, 3, 2, 1]) -> [-5, -2, 0, 1, 2, 3]
"""
# My Code
def sort_list(l: list) -> list:
    lista_ordenada = []
    lista_ordenada = l.sort()
    return lista_ordenada
# Your solution is almost correct, but there is a small mistake in the way you are using the `sort()` method. The `sort()` method in Python does not return a new sorted list, instead, it sorts the list in place and returns `None`. Therefore, when you assign `lista_ordenada = l.sort()`, you are actually assigning `None` to `lista_ordenada`.
# To fix this issue, you should use the `sort()` method on the list directly and then return the list itself (not the result of `sort()`). Here is the corrected version of your function:
def sort_list(l: list) -> list:
    l.sort()
    return l
# By sorting the list directly and returning it after sorting, you will get the sorted list as the output.

# Solution
	def sort_list(l: list) -> list:
		return sorted(l)

# IA's Solutions
# 1. Using the sorted() function:
def sort_list(l: list) -> list:
    return sorted(l)
# Explanation: This solution uses the built-in sorted() function in Python, which returns a new sorted list without modifying the original list. It takes the input list 'l' and returns a new sorted list in ascending order.
# 2. Using the sorted() function with a lambda function:
def sort_list(l: list) -> list:
    return sorted(l, key=lambda x: x)
# Explanation: This solution also uses the sorted() function, but with a lambda function as the 'key' parameter. The lambda function specifies the sorting criteria, which in this case is just the elements themselves (x). This solution will also return a new sorted list in ascending order without modifying the original list.





# https://www.codingdors.com/problem/311
"""
sum_matrix_elements
Show Solution
Given a 2-dimensional list (matrix) of integers, write a Python function that calculates and returns the sum of all its elements using loops.
sum_matrix_elements([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 45
sum_matrix_elements([[10]]) -> 10
"""
# My Code
	def sum_matrix_elements(matrix):
	    # [1,2,3]
	    # [4,5,6]
	    # [7,8,9]
	    # sum = 45
	    somatorio = 0
	    for i in range(matrix):
	        somatorio += i
	    return somatorio
# Your solution is incorrect because you are trying to iterate over the matrix using the range function, which expects an integer as an argument, not a list. To iterate over each row in the matrix, you should use "for row in matrix" instead of "for i in range(matrix)".
# Here is the corrected version of your function:
	def sum_matrix_elements(matrix):
	    somatorio = 0
	    for row in matrix:
	        for cada in row:
	            somatorio += cada
	    return somatorio

# Solution
	def sum_matrix_elements(matrix):
		total = 0
		for row in matrix:
		  for num in row:
		    total += num
		return total

# IA's Solutions
# Alternative Solution 1: Using Nested List Comprehension
def sum_matrix_elements(matrix):
    return sum([sum(row) for row in matrix])
# Explanation:
# - This solution uses a nested list comprehension to iterate over each row in the matrix and calculate the sum of elements in each row.
# - The outer list comprehension iterates over each row in the matrix.
# - The inner list comprehension calculates the sum of elements in each row.
# - The `sum()` function is used to calculate the total sum of all elements in the matrix.
# - The final sum is returned as the result.
# Alternative Solution 2: Using Numpy Library
import numpy as np
def sum_matrix_elements(matrix):
    return np.sum(matrix)
# Explanation:
# - This solution utilizes the `numpy` library, which provides efficient numerical operations on multi-dimensional arrays.
# - We first import the `numpy` library as `np`.
# - The `np.sum()` function is used to calculate the sum of all elements in the matrix.
# - The function directly takes the matrix as input and returns the total sum of all elements in the matrix.





# https://www.codingdors.com/problem/312
"""
has_letter_a_matrix
Show Solution
Given a 2-dimensional list (matrix) where each element is a single letter, write a Python function that determines if the letter 'a' exists in the matrix. If the letter 'a' is found, the function should return True, otherwise, it should return False.
has_letter_a_matrix([['b', 'c', 'd'], ['e', 'f', 'g'], ['h', 'i', 'a']]) -> True
has_letter_a_matrix([['b', 'c', 'd'], ['e', 'f', 'g'], ['h', 'i', 'j']]) -> False
"""
# My Code
	def has_letter_a_matrix(matrix):
	    for row in matrix:
	        for elemento in row:
	            if elemento == "a":
	                return True
	    return False

# Solution
	def has_letter_a_matrix(matrix):
		for row in matrix:
		  for num in row:
		    if num == 'a':
		      return True
		return False

# IA's Solutions
# 1. Using any():
def has_letter_a_matrix(matrix):
    return any('a' in row for row in matrix)
# Explanation: This solution uses the `any()` function to check if 'a' exists in any of the rows in the matrix. It iterates through each row and checks if 'a' is in that row. If 'a' is found in any row, it returns True, otherwise it returns False.
# 2. Using nested list comprehensions:
def has_letter_a_matrix(matrix):
    return any('a' in row for row in matrix)
# Explanation: This solution uses a nested list comprehension to iterate through both the rows and elements in the matrix. It checks if 'a' is in each element of the matrix. If 'a' is found in any element, it returns True, otherwise it returns False.






