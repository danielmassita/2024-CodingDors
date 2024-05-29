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





# https://www.codingdors.com/problem/267
"""
same_value
Show Solution
Given a list of integers with 3 elements, return True if all the 3 elements are equal.
same_value([1, 2, 3]) → False
same_value([2, 2, 2]) → True
same_value([1, 2, 1]) → False

Theory
same_value
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
same_value
1. Compare the elements at the first, second, and third index of the list with each other.
2. If all the elements are equal, return True. Else, return False.
"""
# My Code
  def same_value(n: list) -> bool:
      if n[0] == n[1] and n[1] == n[2]:
          return True
      else:
          return False
  
  def same_value(n: list) -> bool:
      return True if n[0]==n[1]==n[2] else False
    
# Solution
  def same_value(n: list) -> bool:
  	if n[0] == n[1] == n[2]:
  	  return True
  	else:
  	  return False

# IA's Solutions
# 1. Using the `count` method:
def same_value(n: list) -> bool:
    return n.count(n[0]) == len(n)
# Explanation: This solution uses the `count` method to count the occurrences of the first element `n[0]` in the list `n`. If the count is equal to the length of the list, then all elements are the same, and it returns True.
# 2. Using set:
def same_value(n: list) -> bool:
    return len(set(n)) == 1
# Explanation: This solution converts the list `n` into a set, which removes any duplicate elements. If the length of the set is 1, it means all elements in the list are the same, and it returns True.
# 3. Using all:
def same_value(n: list) -> bool:
    return all(element == n[0] for element in n)
# Explanation: This solution uses the `all` function along with a generator expression to check if all elements in the list `n` are equal to the first element `n[0]`. It returns True if all elements are the same.





# https://www.codingdors.com/problem/268
"""
common_element
Show Solution
Given 2 lists of integers, a and b, return True if they have the same first element or they have the same second element or they have the same last element. Both arrays will be length 3.
common_element([1,2,3], [4,5,3]) -> True
common_element([1,2,3], [4,5,6]) -> False
common_element([3,2,1], [0,2,4]) -> True

Theory
common_element
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
common_element
1. Compare the elements at the corresponding indices from both the lists using an "or" condition (== operator).
2. If any of the conditions is True, return True. Otherwise, return False.
"""
# My Code
  def common_element(a: list, b: list) -> bool:
      if a[0]==b[0] or a[1]==b[1] or a[2]==b[2]:
          return True
      else:
          return False
    
# Solution
  def common_element(a: list, b: list) -> bool:
  	if a[0] == b[0]:
  	  return True
  	elif a[1] == b[1]:
  	  return True
  	elif a[2] == b[2]:
  	  return True
  	else:
  	  return False

# IA's Solutions
# Certainly! Here is an alternative solution using the `any()` function along with list comprehension:
def common_element(a: list, b: list) -> bool:
    return any(x in a for x in b)
# Explanation:
# - This solution uses the `any()` function, which returns `True` if any element in the iterable passed as an argument is `True`.
# - The list comprehension `[x in a for x in b]` generates a list of Boolean values based on whether each element in list `b` is present in list `a`.
# - The `any()` function then checks if any element in the generated list is `True`, indicating that there is a common element between the two lists.
# - If there is a common element, the function returns `True`; otherwise, it returns `False`.





# https://www.codingdors.com/problem/269
"""
sum_all
Show Solution
Given a list of integers length 3, return the sum of all the elements.
sum_all([1, 2, 3]) → 6
sum_all([5, 11, 2]) → 18
sum_all([7, 0, 0]) → 7

Theory
sum_all
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5

Hint
sum_all
1. Use Python's built-in function sum() to sum all the elements in the list.
"""
# My Code
  def sum_all(n: list) -> int:
      return sum(n)
    
# Solution
  def sum_all(n: list) -> int:
  	sum = n[0] + n[1] + n[2]
  	return sum

# IA's Solutions
# 1. Using a loop:
def sum_all(n: list) -> int:
    sum = 0
    for num in n:
        sum += num
    return sum
# Explanation: This solution iterates over each element in the list `n` and adds it to the `sum` variable.
# 2. Using the reduce function from the functools module:
from functools import reduce
def sum_all(n: list) -> int:
    return reduce(lambda x, y: x + y, n)  
# Explanation: This solution uses the `reduce` function to repeatedly apply the lambda function to the elements of the list `n`, calculating the sum.
# 3. Using a generator expression:
def sum_all(n: list) -> int:
    return sum(num for num in n)
# Explanation: This solution uses a generator expression to generate each element from the list `n` and then calculates the sum of all the elements using the `sum` function.





# https://www.codingdors.com/problem/270
"""
new_list
Show Solution
Given three individual integers 'a', 'b', and 'c', the task is to formulate a list where each of these integers becomes an element.
new_list(3, 4, 5) -> [3, 4, 5]
new_list(1, 6, 12) -> [1, 6, 12]
new_list(21, 7, 14) -> [21, 7, 14]

Theory
new_list
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5

Hint
new_list
1. Initialize a new list using the list constructor [].
2. Inside this constructor, add your individual elements separated by commas. Your function should return this newly created list.
"""
# My Code
  def new_list(a: int, b: int, c: int) -> list:
      nova_lista = []
      nova_lista = [a, b, c]
      return nova_lista
    
# Solution
  def new_list(a: int, b: int, c: int) -> list:
  	return [a, b, c]

# IA's Solutions
# Solution 1: Using list comprehension
def new_list(a: int, b: int, c: int) -> list:
    return [a, b, c]
# Explanation: This solution directly returns a list containing the three input integers using list comprehension, which is a concise way to create lists in Python.
# Solution 2: Using the append method
def new_list(a: int, b: int, c: int) -> list:
    nova_lista = []
    nova_lista.append(a)
    nova_lista.append(b)
    nova_lista.append(c)
    return nova_lista
# Explanation: This solution initializes an empty list and then appends each input integer to the list using the append method. Finally, it returns the resulting list.





# https://www.codingdors.com/problem/271
"""
rotate_right
Show Solution
Given a list of integers length 3, return a new list with the elements "rotated right" so [1, 2, 3] yields [3, 1, 2].
rotate_right([1, 2, 3]) → [3, 1, 2]
rotate_right([5, 11, 9]) → [9, 5, 11]
rotate_right([7, 0, 0]) → [0, 7, 0]

Theory
rotate_right
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5

Hint
rotate_right
1. Access the last element of the list.
2. Access the first and second elements of the list.
3. Create a new list where you combine the elements from Step 1 and Step 2 in the order: last element, first element, second element.
"""
# My Code
  def rotate_right(n: list) -> list:
      first = n[2]
      middle = n[0]
      last = n[1]
      nova_lista = [first, middle, last]
      return nova_lista
    
# Solution
  def rotate_right(n: list) -> list:
  	first = n[0]
  	second = n[1]
  	last = n[2]
  	return [last, first, second]

# IA's Solutions
# Certainly! Here is an alternative solution in Python using list slicing:
def rotate_right(n: list) -> list:
    return [n[-1], n[0], n[1]]
# Explanation:
# - In this solution, we use list slicing to access the elements from the input list `n`.
# - `n[-1]` gives us the last element of the list `n`.
# - `n[0]` gives us the first element of the list `n`.
# - `n[1]` gives us the second element of the list `n`.
# - We create a new list with these elements in the order "rotated right" and return it.





# https://www.codingdors.com/problem/272
"""
reverse_list
Show Solution
Given a list of integers length 3, return a new list with the elements in reverse order, so [1, 2, 3] becomes [3, 2, 1].
reverse_list([1, 2, 3]) → [3, 2, 1]
reverse_list([5, 11, 9]) → [9, 11, 5]
reverse_list([7, 0, 0]) → [0, 0, 7]

Theory
reverse_list
1. A list is a collection of items in a particular order. It is one of the most common data types in Python. 
my_list = [1, 2, 3, 4, 5]
2. Indexing refers to accessing a specific element within a list by its position. The first element in a list has an index of 0 
my_list[0]
 will return 1.
3. Slicing allows you to create a new list that contains a subset of the elements from the original list. 
my_list[1:3]
 will return 
[2, 3]
4. Reverse is a Python built-in function that reverses the order of elements in a list. 
my_list.reverse()
 will reverse the order of elements in the list, so the output will be 
[5, 4, 3, 2, 1]

Hint
reverse_list
1. You will need to separate each element of the list in a variable
2. Remember that the list contains only 3 elements
3. Create a new list adding the elements in reverse order
"""
# My Code
  def reverse_list(n: list) -> list:
      nova = [n[0], n[1], n[2]]
      nova.reverse()
      return nova
    
# Solution
  def reverse_list(n: list) -> list:
  	first = n[0]
  	second = n[1]
  	last = n[2]
  	return [last, second, first]

# IA's Solutions
# 1. Using list slicing:
def reverse_list(n: list) -> list:
    return n[::-1]
# Explanation: In this solution, we use list slicing with a step size of -1 to reverse the list. By specifying `n[::-1]`, we are creating a new list with all elements from the original list but in reverse order.
# 2. Using the reversed() function:
def reverse_list(n: list) -> list:
    return list(reversed(n))
# Explanation: In this solution, we use the `reversed()` function which returns an iterator that accesses the elements of the list in reverse order. We convert this iterator back to a list using the `list()` constructor, resulting in a new list with elements reversed.





# https://www.codingdors.com/problem/273
"""
min_end
Show Solution
Given a list of integers length 3, figure out which is smaller, the first, second or last element in the list, and set all the other elements to be that value. Return the changed list.
min_end([1, 2, 3]) → [1, 1, 1]
min_end([11, 5, 9]) → [5, 5, 5]
min_end([2, 11, 3]) → [2, 2, 2]

Theory
min_end
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5

Hint
min_end
1. Use the min function to find the smallest element in the list.
2. Create a new list where all the elements are the smallest element from Step 1.
"""
# My Code
  def min_end(n: list) -> list:
      minimo = min(n[0], n[1], n[2])
      return [minimo, minimo, minimo]
    
# Solution
  def min_end(n: list) -> list:
  	if n[0] < n[1] and n[0] < n[2]:
  	  min = n[0]
  	elif n[1] < n[0] and n[1] < n[2]:
  	  min = n[1]
  	else:
  	  min = n[2]
  	return [min, min, min]

# IA's Solutions
# 1. Using list comprehension:
def min_end(n: list) -> list:
    min_val = min(n)  # Find the minimum value in the list
    return [min_val] * 3   # Create a new list with the minimum value repeated three times
# Explanation:
# - The `min_val` variable stores the minimum value of the input list `n` using the `min()` function.
# - We then return a new list `[min_val] * 3` where `[min_val]` creates a list with the minimum value, and `* 3` repeats this list three times, resulting in a list of length 3 with the minimum value.
# 2. Using conditional assignment:
def min_end(n: list) -> list:
    min_val = min(n)  # Find the minimum value in the list
    return [min_val if x != min_val else x for x in n]
# Explanation:
# - We first calculate the minimum value in the input list `n` using the `min()` function and store it in the `min_val` variable.
# - We then use a list comprehension to create a new list where each element is either the minimum value `min_val` if it is not equal to the minimum, or the original value `x` if it matches the minimum value.





# https://www.codingdors.com/problem/274
"""
compare_lists
Show Solution
Given two lists of integers, 'a' and 'b', each consisting of three elements, return the list which has the larger value in the second position.
compare_lists([1, 4, 3], [2, 3, 5]) → [1, 4, 3]
compare_lists([1, 5, 9], [4, 2, 6]) → [1, 5, 9]
compare_lists([6, 3, 1], [2, 7, 0]) → [2, 7, 0]

Theory
compare_lists
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
compare_lists
1. Access the second elements of both lists 'a' and 'b'.
2. Use a conditional statement to compare the second elements of the two lists.
3. If the second element of list 'a' is larger, return list 'a'. If the second element of list 'b' is larger, return list 'b'.
"""
# My Code
  def compare_lists(a: list, b: list) -> list:
      novaLista = max(a[1], b[1])
      if a[1] > b[1]:
          return a
      else:
          return b
          
# Solution
  def compare_lists(a: list, b: list) -> list:
  	if a[1] > b[1]:
  	  return a
  	else:
  	  return b

# IA's Solutions
# Solution 1: Using List Comprehension
def compare_lists(a: list, b: list) -> list:
    return a if a[1] > b[1] else b
# Explanation: This solution uses a conditional expression to check if the second element of list 'a' is greater than the second element of list 'b'. If true, it returns list 'a'; otherwise, it returns list 'b'. This is a more concise way of writing the same logic as the original solution.
# Solution 2: Using the key parameter in the max function
def compare_lists(a: list, b: list) -> list:
    return max([a, b], key=lambda x: x[1])
# Explanation: This solution uses the key parameter in the max function to specify that the maximum value should be determined based on the second element of each list. By providing a lambda function that returns the value at index 1, the max function can compare the lists based on their second elements and return the list with the larger value in the second position.





# https://www.codingdors.com/problem/275
"""
make_ends
Show Solution
Given two lists of integers 'a' and 'b', return a new list length 4 containing the first and last elements from the originals lists. The original list will be length 2 or more.
make_ends([1, 2, 3], [4, 5, 6]) → [1, 3, 4, 6]
make_ends([0, 2, 4], [1, 3, 5]) → [0, 4, 1, 5]
make_ends([7, 4, 6, 2], [-1, 0]) → [7, 2, -1, 0]

Theory
make_ends
1. Lists are ordered collections of items in Python. You can create a list by placing a comma-separated sequence of items inside square brackets []. Example:
list1 = [4, 5]
2. Indexing allows you to access individual elements of a list. In Python, indices start at 0 for the first element. Example:
list1 = [4, 5]
first_element = list1[0]  # 4
second_element = list1[1]  # 5

Hint
make_ends
1. Access the first and last elements of both lists 'a' and 'b'.
2. Create a new list where you combine the elements from Step 1 in the order: first of 'a', last of 'a', first of 'b', last of 'b'.
"""
# My Code
  def make_ends(a: list, b: list) -> list:
      return [a[0], a[-1], b[0], b[-1]]
    
# Solution
  def make_ends(a: list, b: list) -> list:
  	return [a[0], a[-1], b[0], b[-1]]

# IA's Solutions
# 1. Using list unpacking:
def make_ends(a, b):
    return [*a[:1], *a[-1:], *b[:1], *b[-1:]]
# Explanation: This solution uses list unpacking to concatenate the first and last elements of lists \a and \b  into a new list.
# 2. Using list slicing and extend method:
def make_ends(a, b):
    result = []
    result.extend([a[0], a[-1]])
    result.extend([b[0], b[-1]])
    return result
# Explanation: This solution uses list slicing to get the first and last elements of lists 'a' and 'b', then extends the result list with these elements.
# 3. Using list comprehension:
def make_ends(a, b):
    return [x for lst in [a[:1], a[-1:], b[:1], b[-1:]] for x in lst]
# Explanation: This solution uses list comprehension to iterate through sublists containing the first and last elements of lists 'a' and 'b', and flattens them into a single list.





# https://www.codingdors.com/problem/276
"""
even_list
Show Solution
Given a list of integers length 3, return True if all the elements are even.
even_list([2, 5, 6]) → False
even_list([4, 8, 12]) → True
even_list([1, 3, 9]) → False

Theory
even_list
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
even_list
1. Iterate through the list: Since you're given a list of integers, you'll need to check each element individually to see whether it is even or odd. 
2. Check for evenness: For each integer in your list, you can check if it is even by using the modulo operator (%). In Python, n % 2 will return 0 if n is an even number and 1 if n is an odd number. So, you can use an if statement to check if n % 2 == 0 for each element n in your list.
3. Return False immediately if an odd number is found: As you're checking each integer, if you find one that is odd (i.e., n % 2 != 0), you can immediately return False from your function. This is because finding even one odd number means not all elements in the list are even.
4. Return True if the loop completes without finding any odd numbers: If your loop finishes without returning False, that means you never found any odd numbers, so all the elements in your list must be even. At this point, you can return True from your function.
"""
# My Code
  def even_list(n: list) -> bool:
      if n[0] % 2 == 0 and n[1] % 2 == 0 and n[2] % 2 == 0:
          return True
      else:
          return False
    
# Solution
  def even_list(n: list) -> bool:
  	if n[0] % 2 == 0 and n[1] % 2 == 0 and n[2] % 2 == 0:
  	  return True
  	else:
  	  return False

# IA's Solutions
# Certainly! Here is an alternative solution that uses a list comprehension to check if all elements are even:
def even_list(n: list) -> bool:
    return all(num % 2 == 0 for num in n)
# In this solution, the `all()` function is used with a list comprehension to iterate through each element in the input list `n`. The list comprehension checks if each element is even (`num % 2 == 0`). If all elements pass this check, `all()` returns `True`, indicating that all elements are even.




