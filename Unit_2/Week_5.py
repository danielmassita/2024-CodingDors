"""
CODING DORS
UNIT 2 - LOOPS - https://cs50.harvard.edu/python/2022/notes/2/
WEEK 5 - Loops - https://www.codingdors.com/week/5
"""





# https://www.codingdors.com/problem/83
"""
sum_one_to_n
Show Solution
Write a Python function that takes an integer n as input and calculates the sum of all integers from 1 to n, inclusive using a for loop. The function should the return the result.
sum_one_to_n(5) -> 15
sum_one_to_n(10) -> 55
sum_one_to_n(20) -> 210

Theory
sum_one_to_n
1. Looping with for loop in Python:
for i in range(n):
    # code block
2. Initializing a variable: 
total = 0
3. Updating a variable: 
total += i
4. Returning a value from a function: 'return total'. Example:
# This function calculates the sum of all integers from 1 to n
def sum_one_to_n(n):
    # Initializing the total sum
    total = 0
    # Looping through all numbers from 1 to n
    for i in range(n):
        # Adding the number i to the total sum
        total += i
    # Returning the total sum
    return total

Hint
sum_one_to_n
1. Use a for loop to iterate from 1 to n inclusive.
2. Initialize a variable to keep track of the sum.
3. Add each number in the loop to the sum variable.
4. Return the sum variable as the result.
"""
# My Code
  def sum_one_to_n(n: int):
      somatorio = 0
      for i in range(0, n+1):
          somatorio += i
      return somatorio

# Solution
  def sum_one_to_n(n: int):
  	sum = 0
  	for i in range(0, n+1):
  	  sum = sum + i
  	return sum

# IA's Solutios
# 1. Using the sum() function with a range() generator:
def sum_one_to_n(n: int):
    return sum(range(1, n+1))
# This solution uses the `sum()` function combined with a `range()` generator to calculate the sum of integers from 1 to n directly without the need for an explicit loop. The `range(1, n+1)` generates a sequence of numbers from 1 to n (inclusive) which is then passed to the `sum()` function to compute the sum.
# 2. Using a list comprehension:
def sum_one_to_n(n: int):
    return sum([i for i in range(1, n+1)])
# This solution also avoids an explicit loop by using a list comprehension to generate the numbers from 1 to n and then passing the resulting list to the `sum()` function to calculate the sum.
# 3. Using the formula for the sum of an arithmetic series:
def sum_one_to_n(n: int):
    return n * (n + 1) // 2
# This solution bypasses the need for any explicit iteration by directly applying the formula for the sum of an arithmetic series. The formula states that the sum of the first n natural numbers is n * (n + 1) / 2. By using this formula, we can calculate the sum of integers from 1 to n more efficiently without the need for a loop.




 
# https://www.codingdors.com/problem/87
"""
sum_one_to_n_while
Show Solution
Write a Python function that takes an integer n as input and calculates the sum of all integers from 1 to n, inclusive, using a while loop.
sum_one_to_n_while(5) -> 15 
sum_one_to_n_while(10) -> 55 
sum_one_to_n_while(20) -> 210

Theory
sum_one_to_n_while
1. While loop: A while loop is a control flow statement that allows code to be executed repeatedly based on a condition. It is used to repeatedly execute a block of code as long as the condition remains True. Example: 
while True: 
    print("Hello World")
2. Summation: Summation is the process of adding up a sequence of numbers. The summation of n integers can be calculated using the formula n(n+1)/2. Example:
1 + 2 + 3 + 4 + 5 = 15
3. Function: Function is a group of related statements that perform a specific task. It helps in the organization and modularity of the code. Example:
def sum_one_to_n_while(n):
    sum = 0
    i = 1
    while i<=n:
        sum += i
        i += 1
    return sum

Hint
sum_one_to_n_while
1. Define a variable to hold the sum, initialized to 0. 
2. Use a while loop to iterate starting from 1 until n, inclusive. 
3. Add the current value of the iterator to the sum variable in each iteration. 
4. Return the sum value after the loop is completed.
"""
# My Code
    def sum_one_to_n_while(n: int):
    	somatorio = 0
    	contador = 0
    	while contador <= n:
    	  somatorio += i
    	  contador += 1
    	return somatorio

# Solution
    def sum_one_to_n_while(n: int):
    	sum = 0
    	i = 0
    	while i <= n:
    	  sum = sum + i
    	  i = i + 1
    	return sum


# IA's Solutios
# 1. Using a for loop:
def sum_one_to_n_while(n: int):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
# In this solution, we use a for loop to iterate over the range from 1 to n (inclusive) and add each number to the sum.
# 2. Using the arithmetic progression formula:
def sum_one_to_n_while(n: int):
    return (n * (n + 1)) // 2
# This solution uses the formula for the sum of an arithmetic progression to directly calculate the sum of all integers from 1 to n. The formula is `n * (n + 1) / 2`.





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutios





