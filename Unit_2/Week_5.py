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
        total = 0
        for i in range(n):
            total += i
        return total
# Your solution is incorrect because the range function in Python generates a sequence that starts from 0 and ends at n-1. This means that your current implementation will sum integers from 0 to n-1 instead of 1 to n. To fix this, you should update the range function to start at 1 instead of the default 0. Here is the corrected version of your function:
    def sum_one_to_n(n: int):
        total = 0
        for i in range(1, n+1):
            total += i
        return total

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
        soma = 0
        contador = 0
        while contador <= n:
            soma += contador
            contador += 1
        return soma

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





# https://www.codingdors.com/problem/294
"""
sum_to_n_even
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all even integers from 0 to n inclusive, using a for loop.
sum_to_n_even(5) -> 6
sum_to_n_even(10) -> 30
sum_to_n_even(1) -> 0

Theory
sum_to_n_even
1. For loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). A 'for' loop can be used to execute a set of statements, once for each item in a list, tuple, set etc. Example: 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
2. Even number: An even number is any integer that can be exactly divided by 2. In other words, it has no remainder when divided by 2. Example: 
2, 4, 6, 8, 10
3. Range(): 'range()' function is used to generate a sequence of numbers. It generates a sequence of numbers from the start argument to the stop argument, in increments of step argument. Example:
for i in range(0, 6, 2):
    print(i)

Hint
sum_to_n_even
1. Define an integer before the for loop to store the sum of even integers.
2. Use the range() function to loop through integers from 0 to n.
3. Use an if statement to check if the integer is even.
4. If the integer is even, sum.
5. Return the sum.
"""
# My Code
    def sum_to_n_even(n: int) -> int:
        soma = 0
        i = 0
        for i in range(0, n+1):
            if (i % 2) == 0:
                soma += i
            i += 1
        return soma

# Solution
    def sum_to_n_even(n: int) -> int:
    	sum = 0
    	for i in range(n+1):
    	  if i % 2 == 0:
    	    sum += i
    	return sum

# IA's Solutios
# 1. Using range() with a step of 2:
def sum_to_n_even(n: int) -> int:
    return sum(range(0, n+1, 2))
# Explanation: This solution utilizes the `range()` function with a step of 2 to generate a sequence of even numbers from 0 to n (inclusive), then calculates the sum of the numbers using `sum()`.
# 2. Using a list comprehension:
def sum_to_n_even(n: int) -> int:
    return sum([i for i in range(0, n+1) if i % 2 == 0])
# Explanation: This solution uses a list comprehension to filter out even numbers from the range 0 to n and then calculates the sum of these even numbers using `sum()`.
# 3. Using a while loop:
def sum_to_n_even(n: int) -> int:
    soma = 0
    i = 0
    while i <= n:
        if i % 2 == 0:
            soma += i
        i += 1
    return soma
# Explanation: This solution achieves the same result as the given function, but instead of a for loop, it uses a while loop to iterate through numbers from 0 to n and add even numbers to the sum.





# https://www.codingdors.com/problem/296
"""
sum_even_number_while
Show Solution
Write a Python function that takes an integer n as input and returns the sum all even integers from 0 to n inclusive, using a while loop. 
sum_even_number_while(5) -> 6
sum_even_number_while(10) -> 30
sum_even_number_while(1) -> 0

Theory
sum_even_number_while
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

Hint
sum_even_number_while
1. Use a while loop to iterate over the integers from 0 to n inclusive
2. Use an if statement to test if the integer is even
3. Sum the even integer
4. Return the sum at the end of the loop.
"""
# My Code
def sum_even_number_while(n: int) -> int:
    soma = 0
    i = 0
    while i <= n:
        if i % 2 == 0: 
            soma += i
        i += 1
    return soma

# Solution
    def sum_even_number_while(n: int) -> int:
    	sum = 0
    	i = 0
    	while i <= n:
    	  if i % 2 == 0:
    	    sum += i
    	  i += 1
    	return sum

# IA's Solutios
# Alternative Solution 1:
def sum_even_number_while(n: int) -> int:
    soma = 0
    i = 0
    while i <= n:
        soma += i
        i += 2
    return soma
# Explanation: In this alternative solution, instead of checking for even numbers using the condition `if i % 2 == 0`, we directly increment the loop variable `i` by 2 in each iteration, ensuring that we only consider even numbers. This approach reduces the number of iterations required.
# Alternative Solution 2:
def sum_even_number_while(n: int) -> int:
    soma = 0
    i = 0
    while i <= n:
        if i % 2 == 0:
            soma += i
        i += 1
    return soma
# Explanation: This solution is similar to the original function, but the condition `if i % 2 == 0` is placed inside the while loop. It still achieves the desired result by correctly summing all even numbers within the range.
# Alternative Solution 3:
def sum_even_number_while(n: int) -> int:
    soma = sum(i for i in range(n + 1) if i % 2 == 0)
    return soma
# Explanation: This solution takes a different approach by using a list comprehension to generate all even numbers in the range from 0 to n, and then summing them up using the built-in `sum` function. While this solution is concise, it may not be as efficient as the previous ones for large values of n.





# https://www.codingdors.com/problem/295
"""
sum_odd_to_n_forloop
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all odd integers from 0 to n inclusive, using a for loop. 
sum_odd_to_n_forloop(5) -> 9
sum_odd_to_n_forloop(10) -> 25
sum_odd_to_n_forloop(1) -> 1

Theory
sum_odd_to_n_forloop
1. For loop: A for loop is used for iterating over a sequence, like strings, lists, tuples etc. or for iterating over a range of integer numbers. It executes a set of statements, once for each item in the sequence. For example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
3. if statement: An if statement is used for conditional execution. It checks a condition, and if it is true, runs a block of code. For example:
x = 5
if x > 3:
  print("x is greater than 3")
4. Modulo operator: The modulo operator returns the remainder of a division operation. It is denoted by the % symbol in Python. For example:
x = 5
y = 2
print(x % y) # output: 1

Hint
sum_odd_to_n_forloop
1. Use a for loop to iterate from 0 to n inclusive.
2. Check if each integer is odd using the modulus operator.
3. If the integer is odd, sum.
"""
# My Code
    def sum_odd_to_n_forloop(n: int) -> int:
        soma = 0
        i = 0
        for i in range(0, n+1):
            if i % 2 != 0:
                soma += i
            i += 1
        return soma

# Solution
    def sum_odd_to_n_forloop(n: int) -> int:
    	sum = 0
    	for i in range(n+1):
    	  if i % 2 != 0:
    	    sum += i
    	return sum

# IA's Solutios
# **Alternative Solution 1: Using range with step 2**
def sum_odd_to_n_forloop(n: int) -> int:
    soma = 0
    for i in range(1, n+1, 2):  # start from 1 with step 2 to only consider odd numbers
        soma += i
    return soma
# In this solution, we start the loop from 1 and increment the loop variable `i` by 2 in each iteration. This ensures that we only consider odd numbers in the summation process.
# **Alternative Solution 2: Using List Comprehension**
def sum_odd_to_n_forloop(n: int) -> int:
    return sum([i for i in range(1, n+1) if i % 2 != 0])
# In this solution, we use list comprehension to generate a list of odd numbers from 1 to `n` using a conditional statement (`if i % 2 != 0`). Then, we calculate the sum of all elements in the generated list using the `sum` function.





# https://www.codingdors.com/problem/297
"""
sum_to_n_odd_while
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all odd integers from 0 to n inclusive, using a while loop. 
sum_to_n_odd_while(5) -> 9
sum_to_n_odd_while(10) -> 25
sum_to_n_odd_while(1) -> 1

Theory
sum_n_to_odd_while
1. While loop: A while loop is a control flow statement that allows us to execute a block of statements repeatedly until a given condition is satisfied. The condition is checked before executing the statements inside the loop. Example: 
i = 0
while i < 3:
    print(i)
    i += 1
2. An odd integer is any integer that is not an even number, i.e., not divisible by 2 without a remainder. Example: 
odd_num = 3
another_odd_num = 7

Hint
sum_n_to_odd_while
1. Start with an empty list to store the odd integers
2. Initialize a counter variable to 1
3. Use a while loop to iterate while the counter is less than or equal to n
4. Within the loop, check if the counter is odd
5. If it is, add it to the sum
6. Increment the counter by 1 with each iteration
7. Return the sum at the end of the function
"""
# My Code
    def sum_to_n_odd_while(n: int) -> int:
        soma = 0
        i = 1
        while i <= n:
            if i % 2 != 0:
                soma += i
            i += 1
        return soma

# Solution
    def sum_to_n_odd_while(n: int) -> int:
    	sum = 0
    	i = 0
    	while i <= n:
    	  if i % 2 != 0:
    	    sum += i
    	  i += 1
    	return sum

# IA's Solutios
# 1. Using range function with step size 2:
def sum_to_n_odd_while(n: int) -> int:
    soma = 0
    i = 1
    while i <= n:
        soma += i
        i += 2
    return soma
# Explanation: In this solution, we start from i = 1 and add i to the sum in each iteration of the while loop. We increment i by 2 in each iteration to ensure that we only consider odd numbers. This solution eliminates the need for the conditional check `if i % 2 != 0` in each iteration.
# 2. Using an if statement to exclude even numbers without a modulo operation:
def sum_to_n_odd_while(n: int) -> int:
    soma = 0
    i = 1
    while i <= n:
        if i & 1:  # Check if i is odd using bitwise AND
            soma += i
        i += 1
    return soma
# Explanation: In this solution, we use a bitwise AND operation (`i & 1`) to check if the least significant bit of i is set, which is equivalent to checking if i is odd. This allows us to exclude even numbers without using the modulo operator `%`. The rest of the code is similar to the original solution.





# https://www.codingdors.com/problem/298
"""
sum_reverse_n_for
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all numbers from n to 0 inclusive (reverse order), using a for loop.
sum_reverse_n_for(5) -> 15
sum_reverse_n_for(3) -> 6
sum_reverse_n_for(1) -> 1

Theory
sum_reverse_n_for
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
3. range() with a reversed step: range() can be used to generate a sequence of numbers in reverse order by setting a negative step. Example: 
range(5, -1, -1)
Output: [5, 4, 3, 2, 1, 0]

Hint
sum_reverse_n_for
1. Define a function that takes an integer as an argument. 
2. Create an integer to store the output. 
3. Use a for loop to iterate from the input integer to 0. 
4. Sum each number. 
5. Return the sum.
"""
# My Code
    def sum_reverse_n_for(n: int) -> int:
        soma = 0
        i = n
        for i in range(i, 0, -1):
            soma += i
            i -= 1
        return soma

# Solution
    def sum_reverse_n_for(n: int) -> int:
    	sum = 0
    	for i in range(n, -1, -1):
    	  sum += i
    	return sum

# IA's Solutios
# Alternative Solution 1:
def sum_reverse_n_for(n: int) -> int:
    total = 0
    for i in range(n, -1, -1):
        total += i
    return total
# Explanation for Alternative Solution 1:
# - In this solution, we use a variable named `total` to keep track of the cumulative sum of numbers from `n` down to 0.
# - We iterate over a range starting from `n` down to -1 (inclusive) with a step of -1 using the `range()` function.
# - During each iteration, we add the current value of `i` to the `total` sum.
# - Finally, we return the total sum.
# Alternative Solution 2:
def sum_reverse_n_for(n: int) -> int:
    return sum(range(n, -1, -1))
# Explanation for Alternative Solution 2:
# - In this solution, we use the `sum()` function along with the `range()` function to calculate the sum directly in a single line of code.
# - The `range(n, -1, -1)` generates a sequence of numbers from `n` down to -1 with a step of -1.
# - The `sum()` function calculates the sum of all the numbers generated by `range()` and returns the result.





# https://www.codingdors.com/problem/299
"""
sum_reverse_n_while
Show Solution
Write a Python function that takes an integer n as input and returns the sum all numbers from n to 0 inclusive (reverse order), using a while loop.
sum_reverse_n_while(5) -> 15
sum_reverse_n_while(3) -> 6
sum_reverse_n_while(1) -> 1

Theory
sum_reverse_n_while
A while loop in Python continuously executes a block of statements as long as the condition inside the loop returns True. Once the condition becomes False, the program control passes to the line immediately following the loop. Example: 
i = 0
while i < 5:
   print(i)
   i += 1

Hint
sum_reverse_n_while
1. Initialize an integer to store the resulting numbers.
2. Use a while loop with a condition that checks whether n is greater than or equal to 0.
3. Within the while loop, sum the current value of n.
4. Decrement the value of n by 1 in each loop iteration.
5. Return the resulting sum after the while loop has completed.
"""
# My Code
    def sum_reverse_n_while(n: int) -> int:
        soma = 0
        i = n
        while i != 0:
            soma += i
            i -= 1
        return soma

# Solution
    def sum_reverse_n_while(n: int) -> int:
    	sum = 0
    	while n > 0:
    	  sum += n
    	  n -= 1
    	return sum

# IA's Solutios
# Solution 1: Using a while loop with range function
def sum_reverse_n_while(n: int) -> int:
    soma = 0
    for i in range(n, -1, -1):
        soma += i
    return soma
# In this solution, we use the range function to iterate over the numbers from n to 0 in reverse order. This simplifies the while loop by directly iterating over the range of numbers.
# Solution 2: Using a while loop with a decrementing counter
def sum_reverse_n_while(n: int) -> int:
    soma = 0
    i = n
    while i >= 0:
        soma += i
        i -= 1
    return soma
# In this solution, we use a decrementing counter i to iterate over the numbers from n to 0. The loop continues while i is greater than or equal to 0, and the counter i is decremented by 1 in each iteration.





# https://www.codingdors.com/problem/300
"""
sum_reverse_n_even_for
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all even numbers from n to 0 inclusive, using a for loop.
sum_reverse_n_even_for(5) -> 6
sum_reverse_n_even_for(3) -> 2
sum_reverse_n_even_for(1) -> 0

Theory
sum_reverse_n_even_for
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

Hint
sum_reverse_n_even_for
1. You need to start with n and work your way down to 0, so your for loop should count downwards.
2. You need to identify the even numbers in your for loop. One way to do this is to use the modulus operator (%).
3. You need to add the even numbers
"""
# My Code
    def sum_reverse_n_even_for(n: int) -> int:
        soma = 0
        i = n
        for i in range(n, -1, -1):
            if i % 2 == 0:
                soma += i
            i -= 1
        return soma

# Solution
    def sum_reverse_n_even_for(n: int) -> int:
    	sum = 0
    	for i in range(n, -1, -1):
    	  if i % 2 == 0:
    	    sum += i
    	return sum

# IA's Solutios
# Sure! Here is an alternative solution using a for loop:
def sum_reverse_n_even_for(n: int) -> int:
    total_sum = 0
    for i in range(n, -1, -1):
        if i % 2 == 0:
            total_sum += i
    return total_sum
# In this solution, we use a for loop with `range(n, -1, -1)` to iterate from n to 0 in reverse order. We then check if the current number is even using the condition `i % 2 == 0`, and if it is, we add it to the total_sum. Finally, we return the total_sum after the loop is complete.





# https://www.codingdors.com/problem/301
"""
sum_reverse_n_even_while
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all even numbers from n to 0 inclusive, using a while loop.
sum_reverse_n_even_while(5) -> 6
sum_reverse_n_even_while(3) -> 2
sum_reverse_n_even_while(1) -> 0

Theory
sum_reverse_n_even_while
1. While Loop: A while loop is a control flow statement that allows code to be executed repeatedly based on a given condition. The loop continues to execute until the condition is False. 
Example: 
i = 0
while i < 5:
    print(i)
    i += 1
2. If statement: An if statement is a control flow statement that allows code to be executed conditionally based on a given condition. If the condition is true, the block of code inside the if statement is executed, otherwise, it is skipped. 
Example: 
x = 5 
if x < 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")

Hint
sum_reverse_n_even_while
1. Start with an integer to store the even numbers
2. Set up a while loop to continue until n reaches 0
3. Within the loop, use an if statement to check if n is even
4. If n is even, sum
5. Decrement n within the loop to eventually reach 0
6. Return the sum
"""
# My Code
    def sum_reverse_n_even_while(n: int) -> int:
        soma = 0
        i = n
        while i >= 0:
            if i % 2 == 0:
                soma += i
            i -= 1
        return soma

# Solution
    def sum_reverse_n_even_while(n: int) -> int:
    	sum = 0
    	while n > 0:
    	  if n % 2 == 0:
    	    sum += n
    	  n -= 1
    	return sum

# IA's Solutios
# Alternative Solution 1:
def sum_reverse_n_even_while(n: int) -> int:
    total_sum = 0
    while n >= 0:
        if n % 2 == 0:
            total_sum += n
        n -= 1
    return total_sum
# In this solution, the function uses a while loop to iterate from n to 0 inclusive. It checks if the current number is even and adds it to the total_sum if it is. Finally, it decreases n by 1 in each iteration.
# Alternative Solution 2:
def sum_reverse_n_even_while(n: int) -> int:
    total_sum = 0
    while n >= 0:
        total_sum += n if n % 2 == 0 else 0
        n -= 1
    return total_sum
# This alternative solution is similar to the first one but uses a conditional expression to add either the current number or 0 to the total sum based on whether the number is even or odd. This approach can be considered more concise and elegant by some programmers.





# https://www.codingdors.com/problem/303
"""
sum_reverse_n_odd_for
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all odd numbers from n to 0, using a for loop.
sum_reverse_n_odd_for(5) -> 9
sum_reverse_n_odd_for(3) -> 4
sum_reverse_n_odd_for(1) -> 1

Theory
sum_reverse_n_odd_for
1. for loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). A loop variable is used for accessing the elements of a sequence one by one. 
for i in range(5):
2. function: A function is a block of code that is designed to perform a specific task. 
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
sum_reverse_n_odd_for
1. Use a for loop that starts from n and goes down to 0 (inclusive)
2. Check if the current number in the loop is odd using the modulus operator (%)
3. If the number is odd, add it 
4. Return the sum of all the odd numbers found in the loop.
"""
# My Code
def sum_reverse_n_odd_for(n: int) -> int:
    soma = 0
    i = n
    for i in range(n, 0, -1):
        if i % 2 != 0:
            soma += i
        # i = i - 1 # OPCIONAL
    return soma

# Solution
    def sum_reverse_n_odd_for(n: int) -> int:
    	sum = 0
    	for i in range(n, -1, -1):
    	  if i % 2 != 0:
    	    sum += i
    	return sum

# IA's Solutios
# 1. Using a range in reverse order with a step of -1 and checking for odd numbers within the loop:
def sum_reverse_n_odd_for(n: int) -> int:
    total = 0
    for i in range(n, 0, -1):
        if i % 2 != 0:
            total += i
    return total
# 2. Using a while loop instead of a for loop to iterate through the range in reverse order:
def sum_reverse_n_odd_for(n: int) -> int:
    total = 0
    i = n
    while i > 0:
        if i % 2 != 0:
            total += i
        i -= 1
    return total
# Both of these alternative solutions achieve the same result by iterating through the range from n to 0 in reverse order and adding up only the odd numbers to the total sum.





# https://www.codingdors.com/problem/302
"""
sum_reverse_n_odd_while
Show Solution
Write a Python function that takes an integer n as input and returns the sum of all odd numbers from n to 1 inclusive, using a while loop.
sum_reverse_n_odd_while(5) -> 9
sum_reverse_n_odd_while(3) -> 4
sum_reverse_n_odd_while(1) -> 1

Theory
sum_reverse_n_odd_while
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
2. If statements - used to execute a block of code only if a certain condition is true. Example:
x = 5
if x > 10:
  print("x is greater than 10")
else:
  print("x is not greater than 10")
# Output: x is not greater than 10
3. The '%' operator - used to calculate the remainder of a division. Example:
print(10 % 3)
# Output: 1

Hint
sum_reverse_n_odd_while
1. The function should take in one parameter, an integer n.
2. Create an integer to hold the odd numbers.
3. Use a while loop with a condition that checks for odd numbers greater than or equal to 1.
4. Within the while loop, sum the current odd number
5. Return the sum at the end of the function.
"""
# My Code
    def sum_reverse_n_odd_while(n: int) -> int:
        soma = 0
        while n >= 1:
            if n % 2 != 0:
                soma += n
            n -= 1
        return soma

# Solution
    def sum_reverse_n_odd_while(n: int) -> int:
    	sum = 0
    	while n > 0:
    	  if n % 2 != 0:
    	    sum += n
    	  n -= 1
    	return sum

# IA's Solutios
# 1. Using a for loop:
def sum_reverse_n_odd_for(n: int) -> int:
    soma = 0
    for i in range(n, 0, -1):
        if i % 2 != 0:
            soma += i
    return soma
# This solution achieves the same result using a for loop instead of a while loop. It iterates over the range from n to 1 in steps of -1, checking for odd numbers and adding them to the sum.
# 2. Using a list comprehension:
def sum_reverse_n_odd_list_comprehension(n: int) -> int:
    return sum(i for i in range(n, 0, -1) if i % 2 != 0)
# This solution utilizes a list comprehension to generate a list of odd numbers from n to 1 and then uses the sum() function to calculate the sum of those numbers.
# 3. Using a recursive function:
def sum_reverse_n_odd_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n % 2 != 0:
        return n + sum_reverse_n_odd_recursive(n-1)
    else:
        return sum_reverse_n_odd_recursive(n-1)
# This solution uses a recursive function to calculate the sum of odd numbers from n to 1. It adds the current number to the sum if it is odd and then calls the function recursively with n-1.





# https://www.codingdors.com/problem/304
"""
sum_one_to_n_step
Show Solution
Write a Python function that takes an integer n as input and calculates the sum of all integers from 3 to n, inclusive using a for loop. The function should the return the result.
sum_one_to_n_step(15) -> 45
sum_one_to_n_step(10) -> 18
sum_one_to_n_step(20) -> 63

Theory
sum_one_to_n_step
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
sum_one_to_n_step
1. Use a for loop to iterate from 3 to n inclusive.
2. Sum the number
"""
# My Code
    def sum_one_to_n_step(n: int) -> int:
        soma = 0
        for i in range(3, n+1, 3):
            soma += i
        return soma

# Solution
    def sum_one_to_n_step(n: int) -> int:
        soma = 0
        for i in range(3, n+1, 3):
            soma += i
        return soma

# IA's Solutios
# 1. Using a While loop:
def sum_one_to_n_step(n: int) -> int:
    soma = 0
    i = 3
    while i <= n:
        soma += i
        i += 3
    return soma
# In this solution, we initialize a variable `i` to 3 and use a while loop to iterate until `i` is less than or equal to `n`. Inside the loop, we add `i` to the running sum `soma` and increment `i` by 3 in each iteration.
# 2. Using a list comprehension:
def sum_one_to_n_step(n: int) -> int:
    return sum([i for i in range(3, n+1, 3)])
# In this solution, we use a list comprehension to generate a list of numbers from 3 to `n` with a step of 3. We then use the `sum` function to calculate the sum of all the numbers in the list and return the result.





# https://www.codingdors.com/problem/305
"""
sum_one_to_n_step_while
Show Solution
Write a Python function that takes an integer n as input and calculates the sum of all integers from 3 to n, inclusive using a while loop. The function should the return the result.
sum_one_to_n_step_while(15) -> 45
sum_one_to_n_step_while(10) -> 18
sum_one_to_n_step_while(20) -> 63

Theory
sum_one_to_n_step_while
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
sum_one_to_n_step_while
1. Define a variable to hold the sum, initialized to 0. 
2. Use a while loop to iterate starting from 3 until n, inclusive. 
3. Add the current value of the iterator to the sum variable in each iteration. 
4. Return the sum value after the loop is completed.
"""
# My Code
    def sum_one_to_n_step_while(n: int) -> int:
        soma = 0
        indice = 3
        while indice <= n:
            soma += indice
            indice += 3
        return soma

# Solution
    def sum_one_to_n_step_while(n: int) -> int:
    	sum = 0
    	i = 3
    	while i <= n:
    	  sum += i
    	  i += 3
    	return sum

# IA's Solutios
# 1. Using a for loop:
def sum_one_to_n_step_while(n: int) -> int:
    soma = 0
    for i in range(3, n+1, 3):
        soma += i
    return soma
# In this solution, we use a for loop with a range starting from 3, ending at n+1, and incrementing by 3 in each iteration. We sum up all the numbers generated by the range and return the result.
# 2. Using a while loop with a range check:
def sum_one_to_n_step_while(n: int) -> int:
    soma = 0
    indice = 3
    while indice <= n:
        soma += indice
        indice += 3
    return soma
# This solution is similar to the original one but with a small modification. Instead of checking if the index is less than or equal to n in each iteration, we could also check if index + 3 is less than or equal to n. This way, we avoid unnecessary iterations when the final sum would exceed n.

    



# https://www.codingdors.com/problem/22
"""
sum_sequence
Show Solution
Given 2 integers 'x' and 'y', return the sum of all integers in the range of x and y. 
sum_sequence(1, 100) -> 5050 
sum_sequence(5, 36) -> 501

Theory
sum_sequence
1. Range - 'range(start, stop, step)' creates a sequence of numbers from start to stop (exclusive), incrementing by step. If step is not specified, it defaults to 1. Example: 
range(1, 10, 2)
 creates the sequence [1, 3, 5, 7, 9]. 
2. Summation - 'sum(iterable)' returns the sum of all elements in the iterable, which can be a list, tuple, or set. Example: 
sum([1, 2, 3, 4, 5])
 returns 15.
3. Conditional statements - 'if' statements allow you to execute code only when certain conditions are met. 'if' is followed by a condition that evaluates to True or False, and the code that is indented after it will only be executed if the result is True. Example: 
if x > 10:
    print("x is greater than 10")
4. Variables - Variables allow you to store values that you can use later in your code. Example: 
a = 5
 assigns the value 5 to the variable a.
5. Functions - Functions allow you to encapsulate a piece of code that can be called multiple times with different inputs. They can take in arguments and return values. Example: 
def multiply(x, y):
    return x * y

Hint
sum_sequence
- Start a variable at 0 to keep track of the running total.
- Use a loop to iterate through all integers from x to y, inclusive.
- Add each integer to the running total in each iteration of the loop.
- Return the running total as the final answer.
"""
# My Code
    def sum_sequence(x: int, y: int) -> int:
        soma = 0
        for i in range(x, y+1, 1):
            soma += i
        return soma

# Solution
    def sum_sequence(x: int, y: int) -> int:
      sum = 0
      for i in range(x, y+1):
        sum = sum + i
      return sum

# IA's Solutios
# Certainly! Here is an alternative solution using the formula for the sum of an arithmetic sequence:
def sum_sequence(x: int, y: int) -> int:
    n = y - x + 1
    return n * (x + y) // 2
# Explanation:
# - Calculate the number of integers in the range by subtracting the starting integer x from the ending integer y and adding 1 (`n = y - x + 1`).
# - Use the formula for the sum of an arithmetic sequence: `sum = n * (first term + last term) / 2`, where `n` is the number of terms and `first term` is x while `last term` is y.
# - Return the sum calculated from the formula.
# This solution is more efficient than iterating through all integers in the range, especially for larger ranges, as it calculates the sum directly using the formula.





# https://www.codingdors.com/problem/21
"""
return_quarters
Show Solution
Given an integer called 'change', use a while loop to determine how many quarters will be given as 'change'. 
return_quarters(76) -> 3 
return_quarters(29) -> 1

Theory
return_quarters
1. A while loop is a type of loop that will repeatedly execute a block of code until the given condition becomes false. It keeps iterating until the condition becomes false. Example: 
x = 0
while x < 10:
  print(x)
  x += 1
2. An integer is a whole number (no fractions), meaning it can be either positive, negative or zero. Example: 
x = 7 
3. A variable is a named location that stores a value or an object in memory so that we can easily access and manipulate its contents. Example:
change = 50 
4. Conditional statements are used to perform different actions based on different conditions. if, if-else, and if-elif-else are conditional statements. Example:
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
5. The return statement is used to exit a function and return a value to the caller. Example:
def add(x, y):
    z = x + y
    return z 
6. Increment means to increase or a change in the value of a variable. Example: 
x = 5
x += 1  # increment by 1
7. Division is a mathematical operation that is used to find the number of times one number goes into another. Example: 
15 / 3  # returns 5.0 

Hint
return_quarters
- Think about the value of a quarter (or 25 cents).
- What kind of loop would be effective for this problem?
- Consider using integer division and modulus to find the number of quarters.
"""
# My Code
    def return_quarters(change: int) -> int:
        quarters = 0
        while (change % 25) > 0:
            quarters += 1
            change -= 25
        return quarters
    
# Solution
    def return_quarters(change: int) -> int:
    	quarter = 0
    	while change >= 25:
    	  quarter = quarter + 1
    	  change = change - 25
    	return quarter

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





