"""
CODING DORS
UNIT 1 - CONDITIONALS - https://cs50.harvard.edu/python/2022/notes/1/
WEEK 4 - Lists 1 - https://www.codingdors.com/week/4
"""





# https://www.codingdors.com/problem/257
"""
first_element
Show Solution
Write a function that returns the first element of a given list.
first_element([1,2,3,4,5]) -> 1
first_element([5,4,3,2,1]) -> 5
first_element([10,20,30,40,50]) -> 10

Theory
first_element
1. A list is a collection of elements, which can be of different data types, that are ordered and changeable. Lists are created by placing elements inside square brackets. Example: 
my_list = [1, 2, 3, "hello", True]
2. Indexing is the process of accessing an element in a list by its position, which is called its index. The first element in a list has an index of 0, the second has an index of 1, and so on. Example: 
my_list[3]
would return "hello" because it is the fourth element in the list.

Hint
first_element
1. Use list indexing (0) to access and return the first element of the list.
"""
# My Code
  def first_element(n: list) -> int:
      return n[0]
    
# Solution
  def first_element(n: list) -> int:
  	return n[0]

# IA's Solutions
# 1. Using indexing directly:
def first_element(n: list) -> int:
    return n[0]
# 2. Using the built-in `next()` function with an iterator:
def first_element(n: list) -> int:
    return next(iter(n))
# Explanation: This solution creates an iterator from the list `n` using the `iter()` function and then uses the `next()` function to return the first element of the iterator, which is the same as the first element of the list.
# 3. Using unpacking with a for loop:
def first_element(n: list) -> int:
    for first in n:
        return first
# Explanation: This solution iterates over the list `n` using a for loop and returns the first element encountered.





# https://www.codingdors.com/problem/258
"""
second_element
Show Solution
Write a function that returns the second element of a given list.
second_element([1,2,3,4,5]) -> 2
second_element([5,4,3,2,1]) -> 4
second_element([10,20,30,40,50]) -> 20

Theory
second_element
1. In Python, a list is a mutable sequence of items. The items can be of any type (integers, strings, other lists, etc.). Lists are created by enclosing values in square brackets [], separated by commas. Example:
fruits = ['apple', 'banana', 'cherry']
2. Python allows you to access any item in the list by its index, which refers to its position within the list. Python list indices start at 0 for the first element. Example:
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # Outputs: apple
3. In Python, you can access the nth item in a list by its index (n-1). For instance, to get the second item in a list, you would use the index 1. Example:
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])  # Outputs: banana

Hint
second_element
1. Use list indexing (1) to access and return the second element of the list.
"""
# My Code
  def second_element(n: list) -> int:
      return n[1]
    
# Solution
  def second_element(n: list) -> int:
      return n[1]

# IA's Solutions
# 1. Using list unpacking:
def second_element(n: list) -> int:
    _, second = n
    return second
# Explanation: In this solution, we use list unpacking to assign the first element to a placeholder variable and the second element to the variable 'second'. Then, we return the second element.
# 2. Using slicing:
def second_element(n: list) -> int:
    return n[1:2][0]
# Explanation: Here, we use list slicing to extract a sublist containing only the second element. By accessing the first element of this sublist, we get the second element of the original list.
# 3. Using indexing with try-except:
def second_element(n: list) -> int:
    try:
        return n[1]
    except IndexError:
        return None
# Explanation: This solution uses a try-except block to handle the case where the list may not have a second element. If an IndexError is raised, indicating that the second element doesn't exist, we return None.





# https://www.codingdors.com/problem/259
"""
last_element
Show Solution
Write a function that returns the last element of a given list.
last_element([1,2,3,4,5]) -> 5
last_element([5,4,3,2,1]) -> 1
last_element([10,20,30,40,50]) -> 50

Theory
last_element
1. A list is a collection of items in a particular order. Lists are created by separating the items with commas and enclosing them in square brackets. 
[1, 2, 3, 'hello']
2. Indexing is used to extract specific elements from a sequence like list or tuple. The index starts from 0 and goes up to n-1 where n is the length of the list. To retrieve the first element of a list, we can use index 0. 
mylist[0]
3. Slicing is used to extract a specific range of elements from a sequence like list or tuple. It is denoted by the colon (:) symbol. 
mylist[1:3]
4. Negative indexing is used to access the elements of a sequence from its end. The last element can be accessed by index -1. 
mylist[-1]

Hint
last_element
1. Use negative indexing (-1) to access and return the last element of the list.
"""
# My Code
  def last_element(n: list) -> int:
      return n[-1]
    
# Solution
  def last_element(n: list) -> int:
      return n[-1]

# IA's Solutions
# 1. Using list slicing:
def last_element(n: list) -> int:
    return n[len(n)-1]
# Explanation: This solution uses list slicing to access the last element of the list. By using `n[len(n)-1]`, we can directly access the last element of the list `n`.
# 2. Using pop() method:
def last_element(n: list) -> int:
    return n.pop()
# Explanation: The `pop()` method removes and returns the last element from the list. In this solution, we can simply call `n.pop()` to get the last element of the list `n`.





# https://www.codingdors.com/problem/260
"""
list_length
Show Solution
Write a function that returns the length of a given list.
list_length([2,5,8]) -> 3
list_length([11,3,2,9]) -> 4
list_length([0,2,4,6,8,9]) -> 6

Theory
list_length
1. Lists are a type of data structure in Python that can hold any arbitrary number of ordered elements. They are defined using brackets 
[]
 and the elements are separated by commas. Example: 
my_list = [1, 2, 3, 'four', 5.6]
2. The len() function is a built-in function in Python that returns the number of elements in a given object. It can be applied to lists, tuples, strings, and other sequence types. Example:
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length) # Output: 5

Hint
list_length
1. Use Python's built-in function len() to find and return the length of the list.
"""
# My Code
  def list_length(n: list) -> int:
      return len(n)
    
# Solution
  def list_length(n: list) -> int:
      return len(n)

# IA's Solutions
# 1. Using a loop:
def list_length(n: list) -> int:
    count = 0
    for _ in n:
        count += 1
    return count
# Explanation: This solution iterates through each element in the list and increments a counter variable by 1 for each element, effectively counting the number of elements in the list.
# 2. Using list comprehension:
def list_length(n: list) -> int:
    return sum(1 for _ in n)
# Explanation: This solution uses list comprehension to create a list of 1s for each element in the original list and then sums up these 1s to get the total count, which is the length of the list.
# 3. Recursive approach:
def list_length(n: list) -> int:
    if not n:
        return 0
    return 1 + list_length(n[1:])
# Explanation: This solution uses recursion to calculate the length of the list. It checks if the list is empty, in which case it returns 0. Otherwise, it returns 1 (to account for the current element) plus the length of the remaining list (obtained by recursively calling the function with the list sliced from the second element onwards).





# https://www.codingdors.com/problem/261
"""
concatenate_lists
Show Solution
Write a function that concatenates two given lists.
concatenate_lists([1], [2]) -> [1,2]
concatenate_lists([3,4], [5]) -> [3,4,5]
concatenate_lists([2], [4,6,8]) -> [2,4,6,8]

Theory
concatenate_lists
1. Lists are ordered collections of items in Python. They are defined by enclosing a comma-separated sequence of items in square brackets []. Items in a list can be of any type, and a single list can contain items of different types. Example:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
2. You can combine two or more lists into a single list using the + operator, which is known as list concatenation. Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # combined_list is now [1, 2, 3, 4, 5, 6]

Hint
concatenate_lists
1. Use the concatenation operator (+) to concatenate the two lists.
"""
# My Code
  def concatenate_lists(n1: list, n2: list) -> list:
      return list(n1 + n2)
    
# Solution
  def concatenate_lists(n1: list, n2: list) -> list:
  	return n1 + n2

# IA's Solutions
# Alternative Solution:
def concatenate_lists(n1: list, n2: list) -> list:
    return n1 + n2
# Explanation:
# 1. In this alternative solution, we don't need to use the `list()` function while concatenating the two lists `n1` and `n2`.
# 2. The `+` operator can be directly used with lists in Python to concatenate them.
# 3. The result of `n1 + n2` is a new list that contains all the elements from `n1` followed by all the elements from `n2`.
# 4. Finally, the concatenated list is returned as the output of the function.





# https://www.codingdors.com/problem/262
"""
repeat_list
Show Solution
Write a function that repeats a given list n times.
repeat_list([1,2], 3) -> [1,2,1,2,1,2]
repeat_list([5,6,7]], 2) -> [5,6,7,5,6,7]
repeat_list([1], 5) -> [1,1,1,1,1]

Theory
repeat_list
1. As we've discussed in the previous example, lists are ordered collections of items in Python. They are versatile and can contain any type of items. Example:
list1 = [1, 2, 3]
2. You can repeat the elements in a list a given number of times using the * operator. This is known as list repetition. The operation returns a new list with the original elements repeated the specified number of times. Example:
list1 = [1, 2, 3]
repeated_list = list1 * 3  # repeated_list is now [1, 2, 3, 1, 2, 3, 1, 2, 3]

Hint
repeat_list
1. Use the repetition operator (*) to repeat the list 'n' times.
"""
# My Code
  def repeat_list(l: list, n: int) -> list:
      return list(l * n)
    
# Solution
  def repeat_list(l: list, n: int) -> list:
  	return l * n

# IA's Solutions
# 1. Using list comprehension:
def repeat_list(l: list, n: int) -> list:
    return [item for item in l for _ in range(n)]
# Explanation: This solution uses list comprehension to create a new list by repeating each element of the original list n times using a nested loop.
# 2. Using itertools.chain.from_iterable():
from itertools import chain
def repeat_list(l: list, n: int) -> list:
    return list(chain.from_iterable([l]*n))
# Explanation: This solution uses the itertools.chain.from_iterable() function to concatenate n copies of the original list into a single iterable and then converts it back to a list.
# 3. Using the * operator and sum():
def repeat_list(l: list, n: int) -> list:
    return list(sum([l]*n, []))
# Explanation: This solution uses the * operator to repeat the original list n times and then uses the sum() function with an empty list as the initial value to flatten the nested lists into a single list.





# https://www.codingdors.com/problem/263
"""
front_back_list
Show Solution
Given a list 'n', return a new list where the first and last elements have been exchanged.
front_back_list([10,20,30]) → [30,20,10]
front_back_list([5,6,7]) → [7,6,5]
front_back_list([4,6,8]) → [8,6,4]

Theory
front_back_list
1. Lists are ordered collections of items in Python. They are mutable, which means you can change their content without changing their identity. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [10, 20, 30]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. You can also use negative indexing in Python, with -1 referring to the last element, -2 the second to last, and so on. Example:
list1 = [10, 20, 30]
first_element = list1[0]  # 10
last_element = list1[-1]  # 30

Hint
front_back_list
1. Create a new list where the first element is the last element of the original list and the last element is the first element of the original list.
2. The rest of the elements remain the same as the original list.
"""
# My Code
  # def front_back_list(n: list) -> list:
  #     primeiro = n[0]
  #     ultimo = n[-1]
  #     return [ultimo, n[1:-1], primeiro]
# Your solution is close, but there is a mistake in how you are constructing the new list. 
# In your return statement, you are trying to return a list that includes the last element first, followed by a sublist of elements from index 1 to the second to last element, and then finally the first element. This causes an issue because the middle part of the list is itself a sublist, and this creates a nested list structure instead of a flat list.
# To fix this issue, you should concatenate the elements correctly in a single list without nested sublists. Here is the corrected version of your function:
  def front_back_list(n: list) -> list:
      primeiro = n[0]
      ultimo = n[-1]
      return [ultimo] + n[1:-1] + [primeiro]

# Solution
  def front_back_list(n: list) -> list:
  	return [n[-1], n[1], n[0]] 

# IA's Solutions
# Sure! Here is an alternative solution for the front_back_list function in Python:
def front_back_list(n: list) -> list:
    n[0], n[-1] = n[-1], n[0]
    return n
# Explanation:
# 1. The function takes a list 'n' as input.
# 2. Using tuple unpacking, it exchanges the first and last elements of the list by assigning n[-1] to n[0] and n[0] to n[-1].
# 3. Finally, it returns the modified list 'n' with the first and last elements exchanged.





# https://www.codingdors.com/problem/264
"""
first_element_is_greater
Show Solution
Write a function that checks if the first given element in the list is greater than or equal to the second given element.
first_element_is_greater([4,5]) -> True
first_element_is_greater([10, -10]) -> True
first_element_is_greater([1, 10]) -> False

Theory
first_element_is_greater
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5
3. In Python, you can compare two values using comparison operators. The greater than or equal to operator >= returns True if the left operand is greater than or equal to the right operand. Example:
result = 4 >= 5  # False

Hint
first_element_is_greater
1. Use list indexing to access the first and second elements.
2. Check if the first element is greater than or equal to the second element and return the result of this comparison.
"""
# My Code
  def first_element_is_greater(n: list) -> bool:
      return True if n[0] >= n[1] else False
    
# Solution
  def first_element_is_greater(n: list) -> bool:
  	if n[0] >= n[-1]:
  	  return True
  	else:
  	  return False

# IA's Solutions
# **Solution 1:**
def first_element_is_greater(n):
    if n[0] >= n[1]:
        return True
    else:
        return False
# In this solution, we directly check if the first element is greater than or equal to the second element. If the condition is met, the function returns True, otherwise it returns False.
# **Solution 2:**
def first_element_is_greater(n):
    return n[0] >= n[1]
# This solution simplifies the previous one by directly returning the result of the comparison operation `n[0] >= n[1]`. If the condition is True, the function returns True, otherwise it returns False.
# **Solution 3:**
def first_element_is_greater(n):
    if n[0] >= n[1]:
        return "True"
    else:
        return "False"
# In this solution, we return the result of the comparison operation as a string. If the condition is met, the function returns the string "True", otherwise it returns the string "False".





# https://www.codingdors.com/problem/265
"""
first_element_is_smaller
Show Solution
Write a function that checks if the first given element of the list is smaller than or equal to the second given element.
first_element_is_smaller([1, 3]) -> True
first_element_is_smaller([-10, -10]) -> True
first_element_is_smaller([7, 1]) -> False

Theory
first_element_is_smaller
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5
3. In Python, you can compare two values using comparison operators. The greater than or equal to operator >= returns True if the left operand is greater than or equal to the right operand. Example:
result = 4 >= 5  # False

Hint
first_element_is_smaller
1. Use list indexing to access the first and second elements.
2. Check if the first element is less than or equal to the second element and return the result of this comparison.
"""
# My Code
  def first_element_is_smaller(n: list) -> bool:
      return True if n[0] <= n[1] else False
    
# Solution
  def first_element_is_smaller(n: list) -> bool:
  	if n[0] <= n[-1]:
  	  return True
  	else:
  	  return False

# IA's Solutions
# 1. Using direct comparison:
def first_element_is_smaller(n: list) -> bool:
    return n[0] <= n[1]
# Explanation: This solution directly compares the first element of the list to the second element using the less than or equal to operator and returns True if the condition is satisfied, otherwise returns False.
# 2. Using min function:
def first_element_is_smaller(n: list) -> bool:
    return min(n) == n[0]
# Explanation: This solution uses the `min` function to find the minimum value in the list and compares it to the first element of the list. If the first element is the minimum, then it returns True, otherwise it returns False.
# 3. Using if-else one-liner:
def first_element_is_smaller(n: list) -> bool:
    return True if n[0] <= n[1] else False
# Explanation: This solution uses a conditional expression (also known as a ternary operator) to check if the first element is smaller than or equal to the second element and return True if it is, otherwise return False.





# https://www.codingdors.com/problem/266
"""
first_last9
Show Solution
Given a list of integers, return True if the number 9 appears as either the first or last element in the list. The list will be of length 1 or more.
first_last9([1, 2, 9]) → True
first_last9([9, 1, 2, 3]) → True
first_last9([13, 9, 1, 2, 3]) → False

Theory
first_last9
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5
3. In Python, you can compare two values using comparison operators. The greater than or equal to operator >= returns True if the left operand is greater than or equal to the right operand. Example:
result = 4 >= 5  # False
4. The logical OR operator or in Python returns True if at least one of the operands is true. Otherwise, it returns False. Example:
result = (1 == 2) or (2 == 2)  # True, because the second comparison is true

Hint
first_last9
1. Use list indexing to check the first and last elements of the list.
2. If any of them is 9, return True. Else, return False.
"""
# My Code
  def first_last9(n: list) -> bool:
      return True if n[0]==9 or n[-1]==9 else False
    
# Solution
  def first_last9(n: list) -> bool:
  	if n[0] == 9 or n[-1] == 9:
  	  return True
  	else:
  	  return False

# IA's Solutions
# Sure! Your solution is already concise and correct. Here is an alternative solution using a simpler approach:
def first_last9(nums: list) -> bool:
    return nums[0] == 9 or nums[-1] == 9
# This solution does not use the `if` and `else` statements explicitly. Instead, it directly returns the result of the comparison `nums[0] == 9` or `nums[-1] == 9`, which will result in either `True` or `False`.





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





# https://www.codingdors.com/problem/
"""

"""
# My Code

    
# Solution


# IA's Solutions





