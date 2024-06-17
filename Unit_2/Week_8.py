"""
CODING DORS
UNIT 2 - LOOPS - https://cs50.harvard.edu/python/2022/notes/2/
WEEK 8 - Dictionaries - https://www.codingdors.com/week/8
"""





# https://www.codingdors.com/problem/312
"""
create_dictionary
Show Solution
Given a string 'name' and an integer 'age', return a dictionary with the pair of key 'name' and value 'age' added. 
Hint: Dictionaries are used to store data values in key:value pairs.
create_dictionary(gi', 25) -> {'gi': 25}
create_dictionary('leo', 41) -> {'leo': 41}
create_dictionary('rod', 12) -> {'rod': 12}
"""
# My Code
        def create_dictionary(name, age):
            dicionario = {name: age}
            return dicionario
        
# Solution
        def create_dictionary(name, age):
          new_dict = {name: age}
          return new_dict

# IA's Solutions
# Certainly! Here's an alternative solution using dictionary comprehension:
def create_dictionary(name, age):
    return {name: age}
# This solution is more concise and uses dictionary comprehension to directly create and return the dictionary with the key-value pair of 'name' and 'age'. It achieves the same result as the original solution but in a more compact form.






# https://www.codingdors.com/problem/315
"""
add_element_dictionary
Show Solution
Given a dictionary called 'students', a string 'name' and an integer 'age', return the dictionary 'student' with the pair of key 'name' and value 'age' added. 
Hint: Dictionaries are used to store data values in key:value pairs.
add_element_dictionary({'leo': 12}, 'gi', 25) -> {'leo':12, 'gi': 25}
add_element_dictionary({'fe': 27}, 'leo', 41) -> {'fe': 27,'leo': 41}
add_element_dictionary({}, 'rod', 12) -> {'rod': 12}
"""
# My Code

        
# Solution
def add_element_dictionary(students, name, age):
	students[name] = age
	return students

# IA's Solutions
# Sure! Your solution is already quite efficient and straightforward. Another way to achieve the same result is by using the `update` method of the dictionary class. Here's an alternative solution using the `update` method:
def add_element_dictionary(students, name, age):
    students.update({name: age})
    return students
# In this solution, `update` method takes a dictionary with one key-value pair as an argument and updates the original `students` dictionary with the new key-value pair. Finally, it returns the updated dictionary.





# https://www.codingdors.com/problem/316
"""
return_value
Show Solution
We have a dictionary 'd' that contains as key the fruit and the value its price. Given a string 'fruit', return the price of this fruit in the dictionary.

return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'apple') -> 0.5
return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'cherry') -> 0.75
"""
# My Code
        def return_value(d, fruit):
            return d[fruit]
# ou então
        def return_value(d, fruit):
            try:
                price = d[fruit]
                return price
            except:
                return "Fruit not found."
        
# Solution
        def return_value(d, fruit):
        	price = d[fruit]
        	return price

# IA's Solutions
# Certainly! Your solution is concise and correct. Here is an alternative solution using the get() method which allows us to provide a default value in case the fruit is not found in the dictionary:
def return_value(d, fruit):
    return d.get(fruit, "Fruit not found")
# In this solution, if the fruit is not found in the dictionary, it will return the string " Fruit not found " instead of raising a KeyError.
# Another alternative solution would be to use a try-except block to handle the case when the fruit is not found in the dictionary:
def return_value(d, fruit):
    try:
        return d[fruit]
    except KeyError:
        return "Fruit not found"
# This solution is similar to using the get() method but uses a try-except block instead.





# https://www.codingdors.com/problem/30
"""
find_person
Show Solution
Given a dictionary 'd' and a string 'name', return True if the given name exist in our dictionary. Otherwise, False. 
find_person({'Gi': 123, 'Leo': 456}, 'Gi') -> True 
find_person({'Gi': 123, 'Leo': 456}, 'Ana') -> False

Theory
find_person
1. Dictionaries: A dictionary is a collection of key-value pairs. Each key is separated from its value by a colon (:), and the pairs are separated by commas. All keys in a dictionary must be unique. 
{'key1': 'value1', 'key2': 'value2'}
2. Membership operators: 'in' and 'not in' are membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary). 
'hello' in 'hello world'
 returns True.
3. Boolean values: bool is a built-in data type in Python used to represent the truth values True and False. 
x = True
Therefore, in order to solve the problem, we can check whether the given name is a key in our dictionary using the 'in' membership operator. If it is, return True, otherwise, return False.

Hint
find_person
1. You need to check if the given name is a key in the dictionary. 
2. Use the 'in' keyword to check if the name exists in the dictionary. 
3. 'in' keyword returns True if the name exists in the dictionary and False otherwise.
"""
# My Code
	def find_person(d: dict,name: str) -> bool:
	    if name in d: # == True - In Python, the `in` operator already returns a boolean value (True or False) based on whether the specified key exists in the dictionary. So there is no need to compare it explicitly with `True`.
	        return True
	    else:
	        return False
        
# Solution
	def find_person(d: dict,name: str) -> bool:
		if name in d:
		  return True
		else:
		  return False

# IA's Solutions
# 1. Using the `get` method:
def find_person(d: dict, name: str) -> bool:
    return d.get(name) is not None
# Explanation: The `get` method retrieves the value associated with the specified key in a dictionary. If the key is not found, it returns `None`. By checking if the return value is not `None`, we can determine if the key exists in the dictionary.
# 2. Using the `in` keyword with a ternary operator:
def find_person(d: dict, name: str) -> bool:
    return True if name in d else False
# Explanation: This solution uses a ternary operator to achieve the same result as your original solution in a single line. If the name exists in the dictionary, it returns `True`, otherwise it returns `False`.
# 3. Using the `keys` method:
def find_person(d: dict, name: str) -> bool:
    return name in d.keys()
# Explanation: The `keys` method returns a view object that displays a list of all the keys in the dictionary. By checking if the name is in this list of keys, we can determine if the name exists in the dictionary. 





# https://www.codingdors.com/problem/233
"""
dictionary_size
Show Solution
Given a dictionary, return the number of key-value pairs it contains.

dictionary_size({}) -> 0
dictionary_size({'name': 'Gi'}) -> 1
dictionary_size({'a':1, 'b':4, 'c': 7}) -> 3

Theory
dictionary_size
1. Dictionary: A collection of key-value pairs that are unordered, changeable, and indexed.
example_dict = {'a': 1, 'b': 2, 'c': 3}
2. Key: The identifier used to access a value in a dictionary.
example_key = 'a'
3. Value: The data associated with a key in a dictionary.
example_value = 1
4. Length: The number of elements in a collection.
example_len = len(example_dict)

Hint
dictionary_size
Think about how you would count the number of items in a list. 
Can the same approach be applied to a dictionary?
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






