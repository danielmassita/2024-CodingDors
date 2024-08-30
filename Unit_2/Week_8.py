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
	    dicionario_nome_idade = {name: age}
	    return dicionario_nome_idade
	def create_dictionary(name, age):
	    return {name: age}
	def create_dictionary(name, age):
	    dicio = {}
	    dicio.update({name: age})
	    return dicio
        
# Solution
        def create_dictionary(name, age):
          new_dict = {name: age}
          return new_dict

# IA's Solutions
# 1. Using the dict() constructor:
def create_dictionary(name, age):
    return dict([(name, age)])
# This solution creates a dictionary by passing a list of key-value pairs to the dict() constructor.
# 2. Using dictionary comprehension:
def create_dictionary(name, age):
    return {name: age}
# This solution uses dictionary comprehension to create the dictionary with the given name and age.
# 3. Using the update() method:
def create_dictionary(name, age):
    dicionario = {}
    dicionario.update({name: age})
    return dicionario
# This solution initializes an empty dictionary and then uses the update() method to add the key-value pair.





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
	def add_element_dictionary(students, name, age):
	    students.update({name: age})
	    return students
# Ou então...	
	def add_element_dictionary(students, name, age):
	    students[name] = age
	    return students
        
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
# 1. Using bracket notation to add the key-value pair to the dictionary:
def add_element_dictionary(students, name, age):
    students[name] = age
    return students
# Explanation: In this solution, we directly assign the value 'age' to the key 'name' in the 'students' dictionary using bracket notation. This modifies the dictionary in place and achieves the desired result.
# 2. Using dictionary unpacking to create a new dictionary with the added key-value pair:
def add_element_dictionary(students, name, age):
    return {**students, name: age}
# Explanation: In this solution, we use dictionary unpacking (**students) to create a new dictionary that includes all the key-value pairs from the 'students' dictionary. We then add the new key-value pair 'name: age' to this new dictionary and return the updated dictionary.




# https://www.codingdors.com/problem/316
"""
return_value
Show Solution
We have a dictionary 'd' that contains as key the fruit and the value its price. Given a string 'fruit', return the price of this fruit in the dictionary.

return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'apple')e -> 0.5
return_value({'apple': 0.5, 'banana': 0.25, 'cherry': 0.75}, 'cherry') -> 0.75
"""
# My Code
        def return_value(d, fruit):
            return d[fruit]

	
	def return_value(d, fruit):
		price = d[fruit]
		return price
		
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
# 4. Using 'in' directly in the return statement:
def find_person(d: dict, name: str) -> bool:
    return name in d




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
	def dictionary_size(d):
	    tamanho_dicionario = len(d)
	    return tamanho_dicionario
        
# Solution
	def dictionary_size(d):
		return len(d)

# IA's Solutions
# 1. Using the `len()` function directly on the dictionary's items:
def dictionary_size(d):
    return len(d.items())
# Explanation: This solution uses the `items()` method of dictionaries to get a view of all key-value pairs and then uses the `len()` function to determine the number of key-value pairs.
# 2. Using a list comprehension:
def dictionary_size(d):
    return len([(k, v) for k, v in d.items()])
# Explanation: This solution uses a list comprehension to generate a list of key-value pairs from the dictionary and then calculates the length of that list to determine the number of key-value pairs.
# 1. Using list comprehension to count key-value pairs:
def dictionary_size(d):
    return sum(1 for _ in d.items())
# Explanation: This solution uses a list comprehension to iterate over the key-value pairs in the dictionary `d` using the `items()` method. The `sum` function is then used to count the number of key-value pairs by summing up 1 for each pair.
# 2. Using a loop to count key-value pairs:
def dictionary_size(d):
    count = 0
    for key in d:
        count += 1
    return count
# Explanation: This solution uses a loop to iterate over the keys in the dictionary `d` and increments the `count` variable for each key, effectively counting the number of key-value pairs in the dictionary.





# https://www.codingdors.com/problem/236
"""
update_value
Show Solution
Given a dictionary, a key, and a value, update the value associated with the key in the dictionary. If the key does not exist, add the key-value pair to the dictionary.

update_value({}, 'name', 'Gi') -> {'name': 'Gi'}
update_value({'name': 'Gi'}, 'name', 'Leo') -> {'name': 'Leo'}
update_value({'name': 'Gi'}, 'age', 25) -> {'name': 'Gi', 'age': 25}

Theory
update_value
1. Dictionary: A dictionary is a collection of key-value pairs enclosed in curly braces 
{}
. Each key is unique and is associated with a value. 
{"name": "John", "age": 25, "city": "New York"}
2. Key: A key is a unique identifier in a dictionary used to access its associated value. Keys must be immutable, meaning they cannot be changed once created. 
"name"
3. Value: A value is a data that is associated with a particular key in a dictionary. Values can be of any data type including strings, numbers, lists, or even another dictionary. 
"John"
4. Update: To update a value in a dictionary, simply access the key and assign it a new value. If the key does not exist, it will add the key-value pair to the dictionary. 
my_dict["name"] = "Jane"
5. Add: To add a new key-value pair to a dictionary, simply assign a value to a new key. 
my_dict["city"] = "Los Angeles"

Hint
update_value
1. You will need to use the dictionary's built-in methods for updating or adding new key-value pairs.
2. Pay attention to the data types of the key and value you are working with.
3. Consider using conditional statements to check if the key already exists in the dictionary.
4. Remember to assign the updated dictionary back to the original variable.
"""
# My Code
	def update_value(d, key, value):
		if key in value:
		  d[key] = value
		  return d
		else:
		  d[key] = value
		  return d
		  
		# Since we'll change the value either way, 
		# you can do only as follow:
		d[key] = value
		return d
        
# Solution
	def update_value(d, key, value):
		if key in value:
		  d[key] = value
		  return d
		else:
		  d[key] = value
		  return d
		  
		# Since we'll change the value either way, 
		# you can do only as follow:
		d[key] = value
		return d

# IA's Solutions
# Solution 1: Using dictionary methods
def update_value(d, key, value):
    d[key] = value
    return d
# Explanation: This solution directly assigns the key-value pair to the dictionary. If the key already exists, it will update the value; otherwise, it will add a new key-value pair to the dictionary.
# Solution 2: Using the setdefault() method
def update_value(d, key, value):
    d.setdefault(key, value)
    return d
# Explanation: The setdefault() method checks if a key exists in the dictionary. If the key is present, it returns the corresponding value. If the key is not found, it adds the key with the specified value to the dictionary and returns the value.
# Solution 3: Using the update() method
def update_value(d, key, value):
    d.update({key: value})
    return d
# Explanation: The update() method adds the key-value pair to the dictionary. If the key already exists, it will update the value; otherwise, it will add a new key-value pair to the dictionary.





# https://www.codingdors.com/problem/230
"""
sum_values_dict
Show Solution
Given a dictionary with integer values, return the sum of all the values.

sum_values_dict({'a': 1}) -> 1
sum_values_dict({'a': 1, 'b': 7}) -> 8
sum_values_dict({'a': 1, 'b': 7, 'c': 9}) -> 17

Theory
sum_values
1. Dictionary: a collection of key-value pairs that are unordered, changeable, and indexed. Backtick example: 
{'apple': 3, 'banana': 5, 'orange': 2}
2. Key: the identifier used to access a value in a dictionary. Backtick example: 
'apple'
3. Value: the actual data that is associated with a key in a dictionary. Backtick example: 
3
4. Summation: the act of adding two or more numbers together to get a total. Backtick example: 
2 + 3 + 5 = 10
5. For loop: a programming construct that allows for iterating over elements in a collection such as a list, tuple, or dictionary. Backtick example: 
fruits = {'apple': 3, 'banana': 5, 'orange': 2}
for fruit in fruits:
    print(fruits[fruit])

Hint
sum_values
- You don't need to iterate over the keys, only over the values.
- You can use the method 
.values()
 to get all the values in the dictionary.
- You can use the built-in function 
sum()
 to add all the values together.
"""
# My Code
	def sum_values_dict(d):
	    somatorio = 0
	    for key in d:
	        somatorio += d[key]
	    return somatorio

        
# Solution
	def sum_values_dict(d):
		sum = 0
		for key in d:
		  sum += d[key]
		return sum

# IA's Solutions
# Certainly! Here is an alternative solution using the `sum()e` function along with a list comprehension:
def sum_values_dict(d):
    return sum([value for value in d.values()])
# Explanation:
# 1. `d.values()` returns a view object that displays a list of all the values in the dictionary `d`.
# 2. The list comprehension `[value for value in d.values()]` iterates over each value in the dictionary and creates a list of all the values.
# 3. `sum()` function is then used to calculate the sum of all the values in the list.
# 4. The total sum is returned as the result.
# 1. Using the `values()` method:
def sum_values_dict(d):
    return sum(d.values())
# Explanation: The `values()` method returns a view object that displays a list of all the values in the dictionary. By using the `sum()` function, we can directly calculate the sum of all values in the dictionary.
# 2. Using a generator expression:
def sum_values_dict(d):
    return sum(d[key] for key in d)
# Explanation: This solution uses a generator expression to iterate over all keys in the dictionary and sum their corresponding values. It calculates the sum using the `sum()` function.
# 3. Using the `reduce()` function from the `functools` module:
from functools import reduce
def sum_values_dict(d):
    return reduce(lambda x, y: x + y, d.values())
# Explanation: The `reduce()` function from the `functools` module is used to reduce the dictionary values to a single value (the sum of all values). It takes a lambda function that adds two values together and reduces the dictionary values to a single sum.





# https://www.codingdors.com/problem/235
"""
square_values
Show Solution
Given a dictionary with integer values, return a new dictionary with the values squared.

square_values({'a':1}) -> {'a': 1}
square_values({'a':1, 'b': 5}) -> {'a': 1, 'b': 25}
square_values({'a':1, 'b': 5, 'c': 9}) -> {'a': 1, 'b': 25, 'c': 9}

Theory
square_values
1. Dictionary: A collection of key-value pairs, where each key is unique and immutable, and its corresponding value can be any type. 
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
2. Looping through a dictionary: We can use a for loop to iterate through the dictionary. By default, the for loop goes through the keys of the dictionary. We can access its value by using the key as an index. 
for key in my_dict: print(key, my_dict[key])
3. Dictionary comprehension: A concise way to create a new dictionary using an existing iterable (e.g., another dictionary, list, or tuple). 
new_dict = {key: value**2 for key, value in my_dict.items()}
. This creates a new dictionary by iterating through the key-value pairs of 
my_dict
, squaring each value, and mapping the original key to the squared value in the new dictionary.

Hint
square_values
1. Use a loop to iterate through the original dictionary. 
2. For each key-value pair, square the value and add the new key-value pair to the new dictionary. 
3. Return the new dictionary.
"""
# My Code
	def square_values(d):
	    squared_dict = {}
	    for key, value in d.items():
	        squared_dict[key] = value ** 2
	    return squared_dict
        
# Solution
	def square_values(d):
		for key in d:
		  d[key] = d[key] ** 2
		return d

# IA's Solutions
# Alternative Solution 1:
def square_values(d):
    return {key: value**2 for key, value in d.items()}
# Explanation: This solution uses a dictionary comprehension to iterate through the key-value pairs in the input dictionary `d`. It then creates a new dictionary where the values are squared and mapped to the corresponding keys. This is a more concise and Pythonic way of achieving the same result as the original solution.
# Alternative Solution 2:
def square_values(d):
    quadrado_dict = dict(map(lambda item: (item[0], item[1]**2), d.items()))
    return quadrado_dict
# ou
def square_values(d):
    return dict(map(lambda kv: (kv[0], kv[1]**2), d.items()))
# Explanation: This solution uses the `map` function along with a lambda function to iterate through the key-value pairs in the input dictionary `d`. It squares the values and then creates a new dictionary where the values are squared and mapped to the corresponding keys. This is another way of achieving the desired result with a slightly different approach.





# https://www.codingdors.com/problem/229
"""
common_keys
Show Solution
Given two dictionaries, return True if at least one of the keys that are present in both dictionaries.

common_keys({'a': 1}, {'a': 2}) -> True
common_keys({'a': 1}, {'b': 2}) -> False
common_keys({'a': 1, 'b': 2}, {'c': 3, 'b': 3}) -> True

Theory
common_keys
1. 
dictionaries
: Dictionaries are a collection of key-value pairs. They are unordered and can be changed. To access a value from a dictionary, we use the corresponding key. Example: 
{'apple': 2, 'banana': 3, 'orange': 1}
.
2. 
List
: A list is a collection of elements that are ordered and can be changed. We can access individual elements in a list using their index. Example: 
[1, 2, 3, 4, 5]
.
3. 
keys()
: The keys() method in Python returns a view object that displays a list of all the keys in the dictionary. Example: 
dict_name.keys()
.
4. 
intersection()
: The intersection() method in Python returns a set that contains the intersection of two or more sets. Example: 
set1.intersection(set2)
.
5. 
Iterables
: In Python, an iterable is a collection of elements that can be iterated over, meaning we can go through each element one by one. Example: 
[1, 2, 3, 4]
 is an iterable.
For the given problem, we can use the keys() method to retrieve the keys from both dictionaries and then use the intersection() method to find the common keys. Finally, we can convert the result into a list. Example:
dict1 = {'apple': 2, 'banana': 3, 'orange': 1}
dict2 = {'banana': 4, 'peach': 2, 'orange': 5}
common_keys = list(dict1.keys() & dict2.keys())
print(common_keys) # Output: ['banana', 'orange']

Hint
common_keys
- You will need to use the 
keys()
 method for dictionaries. 
- Think about how to compare the keys in both dictionaries.
"""
# My Code
	def common_keys(d1, d2):
		for chave in dic1:
		    if chave in dic2:
		        return True
	    return False
        
# Solution
	def common_keys(d1, d2):
		for key in d1:
		  if key in d2:
		    return True
		return False

# IA's Solutions
# Certainly! Here is an alternative solution using set intersection:
def common_keys(d1, d2):
    return bool(set(d1.keys()) & set(d2.keys()))
# Explanation:
# 1. `set(d1.keys())` creates a set of keys from the first dictionary `d1`.
# 2. `set(d2.keys())` creates a set of keys from the second dictionary `d2`.
# 3. By using the `&` operator (set intersection), we find the common keys between the two sets.
# 4. If the intersection set is not empty, `bool()` will return True, indicating that there is at least one common key present in both dictionaries.
# This solution provides a concise and efficient way to check for common keys between two dictionaries.





# https://www.codingdors.com/problem/224
"""
capitalize_keys
Show Solution
Given a dictionary with string keys, create a new dictionary with the same key-value pairs, but with the keys capitalized.

capitalize_keys({'name': 'gi'}) -> {'Name': 'gi'}
capitalize_keys({'sport': 'soccer'}) -> {'Sport': 'soccer'}
capitalize_keys({'name': 'gi', 'sport': 'soccer'}) -> {'Name': 'gi', 'Sport': 'soccer'}

Theory
capitalize_keys
1. Dictionary: A collection which is unordered, changeable, and indexed. The elements in a dictionary are written as 
key: value
 pairs.
Example: 
fruits = {
  "apple": 2,
  "banana": 5,
  "orange": 3
}
2. For Loop: A structure in programming used to repeat a block of code for a specified number of times or for iterating over a sequence of data.
Example:
for i in range(5):
  print(i)
3. Dictionary Comprehension: A concise way to create dictionaries in Python, using a single line of code.
Example: 
squares = {x: x**2 for x in range(6)}
4. String Methods: Built-in functions in Python for manipulating strings.
Example:
text = "hello, world"
text_upper = text.upper()
Output: "HELLO, WORLD"
5. Capitalize Method: A string method in Python used to return a copy of the string with only the first character capitalized.
Example:
text = "hello, world"
text_capitalized = text.capitalize()
Output: "Hello, world"

Hint
capitalize_keys
You can use a loop to iterate through the original dictionary and create a new dictionary with capitalized keys.
"""
# My Code
	def capitalize_keys(d):
	    novo_dici = {}
	    
	    for key in d:
		novo_dici[key.title()] = d[key]
	    
	    return novo_dici
        
# Solution
	def capitalize_keys(d):
	  new_d = {}
	  for key in d:
	    new_d[key.title()] = d[key]
	  return new_d

# IA's Solutions
# Certainly! Your solution is a valid and effective way to capitalize the keys in a dictionary. However, there are alternative ways to achieve the same result. Here are a few additional solutions in Python:
# 1. Using dictionary comprehension:
def capitalize_keys(d):
    return {key.title(): value for key, value in d.items()}
# This solution uses dictionary comprehension to iterate through the key-value pairs in the original dictionary and create a new dictionary with the capitalized keys.
# 2. Using the `map` function:
def capitalize_keys(d):
    return dict(map(lambda kv: (kv[0].title(), kv[1]), d.items()))
# In this solution, the `map` function is used to apply a lambda function to each key-value pair in the original dictionary, where the key is capitalized using the `title()` method.





# https://www.codingdors.com/problem/225
"""
capitalize_values
Show Solution
Given a dictionary with string values, create a new dictionary with the same key-value pairs, but with the values capitalized.

capitalize_values({'name': 'gi'}) -> {'name': 'Gi'}
capitalize_values({'sport': 'soccer'}) -> {'sport': 'Soccer'}
capitalize_values({'name': 'gi', 'sport': 'soccer'}) -> {'name': 'Gi', 'sport': 'Soccer'}

Theory
capitalize_values
1. for loop: A for loop is a construct in Python that is used to iterate over a sequence of elements. 
Example: 
for i in range(10):
    print(i)

2. dictionary: A dictionary is a collection of key-value pairs, where each key maps to a corresponding value.
Example: 
my_dict = {"name": "Alice", "age": 30, "gender": "female"}

3. capitalize: The capitalize() method in Python is used to convert the first character of a string to uppercase.
Example: 
my_string = "hello, world"
capitalized_string = my_string.capitalize()
print(capitalized_string)
Output: Hello, world

4. update: The update() method is used to add key-value pairs to a dictionary.
Example: 
my_dict = {"name": "Alice", "age": 30}
my_dict.update({"gender": "female"})
print(my_dict)
Output: {"name": "Alice", "age": 30, "gender": "female"}

Hint
capitalize_values
1. You will need to loop through the original dictionary to access the string values. 
2. You can use the upper() method to capitalize each string value. 
3. You can use a dictionary comprehension to create the new dictionary with the capitalized values.
"""
# My Code
	def capitalize_values(d):
	    novo_dici = d	    
	    for key in d:
	        novo_dici[key] = novo_dici[key].capitalize()
	    return novo_dici
        
# Solution
	def capitalize_values(d):
		for key in d:
		  d[key] = d[key].title()
		return d

# IA's Solutions
# Sure! Here is an alternative solution using dictionary comprehension:
def capitalize_values(d):
    return {key: value.title() for key, value in d.items()}
# This solution uses dictionary comprehension to iterate over the key-value pairs in the original dictionary `d`. For each key-value pair, it capitalizes the value using the `title()` method and stores the new key-value pair in the new dictionary that is returned. The resulting dictionary has the same key-value pairs as the original dictionary, but with the values capitalized.





# https://www.codingdors.com/problem/226
"""
merge_dictionaries
Show Solution
Given two dictionaries, merge them into a single dictionary. If a key exists in both dictionaries, sum the values.

merge_dictionaries({'a': 5, 'b': 3}, {'a': 2, 'c': 7}) -> {'a': 7, 'b': 3, 'c': 7}
merge_dictionaries({'apple': 10}, {'banana': 5, 'apple': 2}) -> {'apple': 12, 'banana': 5}

Theory
merge_dictionaries
1. Dictionaries: A dictionary is a collection of key-value pairs, where each key is unique. A dictionary is mutable which means its elements can be added, deleted, or modified. 
   Example: 
{'name': 'Bob', 'age': 30, 'country': 'USA'}

2. Merging Dictionaries: Merging two dictionaries means adding all the key-value pairs of one dictionary into another. If both dictionaries have a key in common, the value of that key in the second dictionary will overwrite the value of that key in the first dictionary.
   Example: 
   dict1 = {'a': 1, 'b': 2}
   dict2 = {'c': 3, 'd': 4}
   dict1.update(dict2)
   print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
   
3. Summing Values: To sum the values of two keys that have the same name in two dictionaries, we can simply add the values together.
   Example: 
   dict1 = {'a': 2, 'b': 4}
   dict2 = {'c': 3, 'b': 6}
   dict3 = {}
   for key in dict1:
       if key in dict2:
           dict3[key] = dict1[key] + dict2[key]
       else:
           dict3[key] = dict1[key]
   for key in dict2:
       if key not in dict1:
           dict3[key] = dict2[key]   
   print(dict3)  # Output: {'a': 2, 'b': 10, 'c': 3}

Hint
merge_dictionaries
- Use a loop to iterate over the keys in one dictionary
- Check if the key exists in the other dictionary
- If it does, add the values and store in the merged dictionary with the key
- If it doesn't, simply store the key-value pair in the merged dictionary
- Repeat the process for the keys in the other dictionary that haven't been checked yet
"""
# My Code
	def merge_dictionaries(d1, d2):
	    novo_dicionario = {}
	    
	    for key in d1:
	        if key in d2:
	            novo_dicionario[key] = d1[key] + d2[key]
	        else:
	            novo_dicionario[key] = d1[key]
	
	    for key2 in d2:
	        if key2 not in novo_dicionario:
	            novo_dicionario[key2] = d2[key2]
	
	    return novo_dicionario

	
# Solution
	def merge_dictionaries(d1, d2):
		new_dict = {}
		for key in d1:
		  if key in d2:
		    new_dict[key] = d1[key] + d2[key]
		  else:
		    new_dict[key] = d1[key]
		for key2 in d2:
		  if key2 not in new_dict:
		    new_dict[key2] = d2[key2]
		return new_dict

# IA's Solutions
# Certainly! Your solution is correct and works as expected. Here is an alternative solution using dictionary comprehension:
def merge_dictionaries(d1, d2):
    new_dict = {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1.keys()).union(d2.keys())}
    return new_dict
# Explanation:
# 1. We use dictionary comprehension to iterate over the union of keys from both dictionaries (d1 and d2).
# 2. For each key, we use the `get` method to retrieve the value for that key from both dictionaries. If the key is not present in a dictionary, we default to 0.
# 3. We sum the values for the key from both dictionaries and store the result in the new dictionary.
# This solution is more concise and achieves the same result as your original solution.





# https://www.codingdors.com/problem/223
"""
invert_dictionary
Show Solution
Given a dictionary, return a new dictionary with keys and values swapped.

invert_dictionary({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}
invert_dictionary({'apple': 'fruit', 'carrot': 'vegetable'}) -> {'fruit': 'apple', 'vegetable': 'carrot'}
invert_dictionary({}) -> {}

Theory
invert_dictionary
1. Dictionary: A collection of key-value pairs, where each key is unique. They are enclosed in curly braces {}.  
'my_dict = {'apple': 2, 'banana': 4}'
2. Looping through a dictionary: You can loop through a dictionary by using a for loop. 
'for key, value in my_dict.items(): print(key, value)'
3. Swapping keys and values: To swap keys and values in a dictionary, you can use a dictionary comprehension. 
'{value: key for key, value in my_dict.items()}'
4. Dictionary comprehension: A shorthand way to create a new dictionary based on an existing dictionary. 
'squared_dict = {num: num*num for num in range(10)}'
5. items() method: A method that returns a list of tuple pairs, where each tuple contains a key-value pair in the dictionary. 
my_dict.items()

Hint
invert_dictionary
- You will need to use a loop to iterate over the key-value pairs in the original dictionary and create a new dictionary where the keys and values are swapped. 
- You can use the dictionary method items()  to get the key-value pairs.
"""
# My Code
	def invert_dictionary(d):
	    novo_dicio = {}
	    
	    for key in d:
		    valor_antigo = d[key]
		    novo_dicio[valor_antigo] = key
	
	    return novo_dicio
		
        
# Solution
	def invert_dictionary(d):
		new_dict = {}
		for key in d:
		  old_value = d[key]
		  new_dict[old_value] = key
		return new_dict

# IA's Solutions
# 1. Using dictionary comprehension:
def invert_dictionary(d):
    return {v: k for k, v in d.items()}
# This solution utilizes dictionary comprehension to create a new dictionary with swapped keys and values. It is concise and efficient.
# 2. Using zip and items method:
def invert_dictionary(d):
    return dict(zip(d.values(), d.keys()))
# This solution uses the zip function to pair values with keys and then converts the pairs into a dictionary. It is a simple and readable approach.
# 3. Using dict.items() and reversed iteration:
def invert_dictionary(d):
    return {v: k for k, v in reversed(list(d.items()))}
# This solution reverses the key-value pairs in the original dictionary by converting them into a list and then using dictionary comprehension to create the inverted dictionary.





# https://www.codingdors.com/problem/227
"""
filter_by_value
Show Solution
Given a dictionary and a value, return a new dictionary containing only the key-value pairs with the given value.

filter_by_value({'a': 1, 'b': 2, 'c': 1}, 1) -> {'a': 1, 'c': 1}
filter_by_value({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}, 'fruit') -> {'apple': 'fruit', 'banana': 'fruit'}

Theory
filter_by_value
1. Dictionary comprehension - It is a concise way to create a new dictionary from an existing iterable where you can specify the key-value pairs. 
Example - 
my_dict = {key: value**2 for key, value in {'a':1, 'b':2, 'c':3}.items()}
2. Dictionary items method - It returns a view object that contains the key-value pairs of the dictionary as tuples.
Example - 
my_dict = {1: 'one', 2: 'two', 3:'two'}
my_items = my_dict.items()
3. Filter function - It returns an iterable that contains only elements that pass the condition specified in the function.
Example - 
my_list = [1, 2, 3, 4]
filtered_list = filter(lambda x: x % 2 == 0, my_list)
4. List comprehension - It is a concise way to create a new list from an existing iterable where you can specify the elements based on condition.
Example - 
my_list = [x for x in range(10) if x % 2 == 0]
5. Lambda function - It is an anonymous function that can take any number of arguments and can have any expression as its body.
Example - 
add = lambda x, y : x + y

Hint
filter_by_value
Use dictionary comprehension to iterate through the original dictionary and filter based on the given value.
"""
# My Code
	def filter_by_value(d, value):
		novo_dicio = {}
		for key in d:
		  if d[key] == value:
		    novo_dicio[key] = value
		return novo_dicio
        
# Solution
	def filter_by_value(d, value):
		new_d = {}
		for key in d:
		  if d[key] == value:
		    new_d[key] = value
		return new_d

# IA's Solutions
# 1. Using dictionary comprehension:
def filter_by_value(d, value):
    return {key: val for key, val in d.items() if val == value}
# With this solution, we use a dictionary comprehension to iterate over the key-value pairs in the input dictionary `d`, and only include those pairs where the value matches the specified `value`.
# 2. Using the filter() function:
def filter_by_value(d, value):
    return dict(filter(lambda item: item[1] == value, d.items()))
# In this solution, we use the `filter()` function to filter the items of the dictionary `d` based on the condition that the value of each item equals the specified `value`. We then convert the filtered items back into a dictionary using the `dict()` function.
# Both of these alternative solutions achieve the same result as the original solution you provided, but in a more concise manner using Python's language features.





# https://www.codingdors.com/problem/228
"""
keys_of_max_value
Show Solution
Given a dictionary with integer values, return a list of keys with the maximum value.

keys_of_max_value({'a': 1, 'b': 2, 'c': 1}) -> ['b']
keys_of_max_value({'apple': 3, 'banana': 5, 'cherry': 5}) -> ['banana', 'cherry']

Theory
keys_of_max_value
1. Dictionary: A collection of key-value pairs that are unordered, changeable and indexed. 
{"apple": 5, "banana": 2, "cherry": 3}
2. Keys: The unique identifiers in a dictionary that helps to associate the values with that particular key. 
"apple"
3. Values: The data or information associated with a key in a dictionary. 
5
4. Maximum Value: The highest value in a collection of values. Example: In 
[3, 5, 7, 2, 8], the maximum value is 8.
5. List: An ordered collection of elements that are changeable and indexed. 
[1, 2, 3, 4]

Hint
keys_of_max_value
- You will need to iterate through the dictionary to find the maximum value.
- You may need to keep track of the current maximum value and update it as you iterate.
- You will also need to keep track of the keys that correspond to the maximum value.
- Consider using a loop and conditionals to accomplish this task.
"""
# My Code
	...
	...
	def keys_of_max_value(d):
		keys_list = []
		max_value = max(d.values())
		for key in d:
		  if d[key] == max_value:
		    keys_list.append(key)
		return keys_list

        
# Solution
	def keys_of_max_value(d):
		keys_list = []
		max_value = max(d.values())
		for key in d:
		  if d[key] == max_value:
		    keys_list.append(key)
		return keys_list

# IA's Solutions
# Certainly! Your solution is already quite efficient and straightforward. However, I can provide an alternative solution using list comprehension, which is a more concise way to achieve the same result:
def keys_of_max_value(d):
    max_value = max(d.values())
    return [key for key, value in d.items() if value == max_value]
# In this alternative solution, a list comprehension is used to iterate through the key-value pairs in the dictionary `d`. For each pair, the key is added to the list if its corresponding value matches the maximum value found in the dictionary. The final list of keys with the maximum value is then returned.





# https://www.codingdors.com/problem/231
"""
sorted_keys
Show Solution
Given a dictionary, return a list of its keys sorted in ascending order.

sorted_keys({'c': 1, 'a': 2, 'b': 1}) -> ['a', 'b', 'c']
sorted_keys({'banana': 5, 'apple': 3, 'cherry': 7}) -> ['apple', 'banana', 'cherry']

Theory
sorted_keys
1. Dictionary - a collection of key:value pairs enclosed in curly braces 
{}
. Keys must be unique and immutable while values can be of any data type. If a key is repeated, the later value replaces the former.
Example: 
{'apple': 3, 'banana': 2, 'cherry': 4}
2. List - an ordered collection of elements enclosed in square brackets 
[]
. Each element is separated by a comma. Lists are mutable, meaning that their elements can be changed.
Example: 
[10, 20, 30, 40]
3. Sorted - a built-in Python function that sorts a collection in ascending order. It can be used with both lists and dictionaries. It takes an iterable as an argument but returns a list.
Example: 
sorted([3, 1, 4, 2])
 returns 
[1, 2, 3, 4]
4. Keys - the first part of a key:value pair in a dictionary. They serve as unique identifiers for each value in the dictionary. Keys must be immutable and unique.
Example: In 
{'apple': 3, 'banana': 2}
, 'apple' and 'banana' are the keys.
5. Ascending Order - a sorting order in which elements are arranged from smallest to largest. 
Example: When sorting 
[3, 1, 4, 2]
 in ascending order, the result is 
[1, 2, 3, 4]

Hint
sorted_keys
- You need to iterate through all the keys in the dictionary
- You can use the keys() method to get a list of all the keys in the dictionary
- Consider using the sorted() function to order the keys in ascending order.
"""
# My Code
	...
	def sorted_keys(d):
		lista_chaves = sorted(d.keys())
		return lista_chaves
        
# Solution
	def sorted_keys(d):
		keys_list = sorted(d.keys())
		return keys_list

# IA's Solutions
# 1. Using sorted() function directly on the dictionary:
def sorted_keys(d):
    keys_list = sorted(d)
    return keys_list
# Explanation: In this solution, we directly pass the dictionary `d` to the sorted() function without calling the keys() method. The sorted() function automatically sorts the keys of the dictionary and returns them as a list in ascending order.
# 2. Using list comprehension to sort keys:
def sorted_keys(d):
    keys_list = [key for key in sorted(d.keys())]
    return keys_list
# Explanation: In this solution, we use list comprehension to iterate over the sorted keys of the dictionary. By calling sorted(d.keys()), we obtain a sorted list of keys, and then we iterate over this sorted list to create a new list (keys_list) containing the keys in ascending order.
# Both of these alternative solutions achieve the same result as the original solution provided.





# https://www.codingdors.com/problem/234
"""
remove_key
Show Solution
Given a dictionary and a key, return a new dictionary with the specified key removed.

remove_key({'a': 1, 'b': 2, 'c': 3}, 'a') -> {'b': 2, 'c': 3}
remove_key({'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}, 'banana') -> {'apple': 'fruit', 'carrot': 'vegetable'}

Theory
remove_key
1. Dictionaries: A dictionary is a collection of key-value pairs. It is similar to a list or an array, but the items are accessed by their key rather than their position. 
{"apple": 2, "banana": 5, "orange": 3}
 is an example of a dictionary where "apple", "banana", and "orange" are the keys, and 2, 5, and 3 are their respective values.

2. Keys and Values: In a dictionary, a key is a unique identifier for a value. Keys can be of any immutable data type such as strings, integers, or tuples. A value is the data associated with a given key in a dictionary. A key and its value are separated by a colon and each key-value pair is separated by a comma. For example, in 
{"apple": 2, "banana": 5, "orange": 3}
, "apple", "banana", and "orange" are the keys, and 2, 5, and 3 are the values.

3. Dictionary Comprehension: It is a concise way to create a new dictionary from an iterable by specifying the key-value pairs in a single expression. The general syntax is {key: value for (key, value) in iterable}. For example, 
{x: x**2 for x in range(5)}
 would result in 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
.

4. The 
dict.pop()
 Method: It is used to remove and return an element from a dictionary for a given key. The syntax is 
dict.pop(key[, default])
. If the key is present in the dictionary, the method removes and returns the value for that key. If the key is not found, it returns the default value, or raises a 
KeyError
 if no default was given. For example, 
fruit_counts = {"apple": 2, "banana": 5, "orange": 3}
, 
fruit_counts.pop("banana")
 would return 
5
 and 
fruit_counts
 would now be 
{"apple": 2, "orange": 3}
 without the "banana" key-value pair.

Hint
remove_key
1. You will need to use the 'del' keyword to remove the key-value pair from the dictionary.
2. You can create a new dictionary to store the remaining key-value pairs.
3. Remember to properly format your function definition, including specifying the parameter types and return type.
"""
# My Code

        
# Solution
	def remove_key(d, key):
		d.pop(key)
		return d

# IA's Solutions
# Sure! Here are two alternative solutions in Python:
# Solution 1: Using dict comprehension
def remove_key(d, key):
    return {k: v for k, v in d.items() if k != key}
# In this solution, we create a new dictionary using dict comprehension.
# We iterate over the items in the original dictionary and only include items where the key is not equal to the specified key.
# Solution 2: Using copy and del
def remove_key(d, key):
    new_dict = d.copy()
    del new_dict[key]
    return new_dict
# In this solution, we first make a shallow copy of the original dictionary using the copy() method.
# Then we use the del statement to remove the specified key from the new dictionary.





# https://www.codingdors.com/problem/237
"""
dict_intersection
Show Solution
Given two dictionaries, return a new dictionary containing the key-value pairs that are present in both dictionaries.

dict_intersection({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 4}) -> {'a': 1, 'b': 2}
dict_intersection({'apple': 'fruit', 'carrot': 'vegetable'}, {'banana': 'fruit', 'apple': 'fruit'}) -> {'apple': 'fruit'}

Theory
dict_intersection
1. Dictionaries: A dictionary is an unordered collection of key-value pairs, where each key must be unique. 
{1: 'one', 2: 'two', 3: 'three'}
2. Key-Value Pairs: A key-value pair is a set of two objects, one representing the key and the other representing the value. 
{'name': 'John', 'age': 30, 'city': 'New York'}
3. Intersection: The intersection of two sets is the set of elements which are common to both sets. In the context of dictionaries, the intersection of two dictionaries is the set of key-value pairs that are present in both dictionaries. 
{1, 2, 3} ∩ {2, 3, 4} = {2, 3}
4. New dictionary: A new dictionary is a dictionary that is created by taking elements from one or more existing dictionaries and adding or modifying elements as needed.
new_dict = {}
5. Iterating through a dictionary: To iterate through a dictionary means to loop over all the keys or key-value pairs of the dictionary and perform some operation on each one. 
for key in my_dict:
    value = my_dict[key]
    print(key, value)

Hint
dict_intersection
- You need to create a new empty dictionary to start.
- You can use a loop to iterate over one of the dictionaries.
- Use the 'in' keyword to check if the current key is present in both dictionaries.
- If the key is present in both dictionaries, add the key-value pair to the new dictionary.
"""
# My Code

        
# Solution
	def dict_intersection(d1, d2):
		new_d = {}
		for key in d1:
		  if key in d2 and d1[key] == d2[key]:
		    new_d[key] = d1[key]
		return new_d

# IA's Solutions
# Certainly! Here's an alternative solution using dictionary comprehension:
def dict_intersection(d1, d2):
    return {key: d1[key] for key in d1 if key in d2 and d1[key] == d2[key]}
# This solution is more concise as it uses dictionary comprehension to create the new dictionary in one line. The dictionary comprehension iterates over the keys in `d1`, checks if the key is present in `d2` and if the values associated with the keys are the same in both dictionaries. If both conditions are met, the key-value pair is added to the new dictionary.





# https://www.codingdors.com/problem/238
"""
count_values
Show Solution
Given a dictionary, return a new dictionary where the keys are the unique values from the input dictionary and the values are the number of occurrences of each unique value.

count_values({'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}) -> 1: 2, 2: 2, 3: 1}
count_values({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}) -> {'fruit': 2, 'vegetable': 1}

Theory
count_values
1. Dictionary data structure - A dictionary is an unordered collection of key-value pairs. Each key-value pair is separated by a colon, and individual key-value pairs are separated by commas. 
{'apple': 3, 'banana': 2, 'grape': 4}

2. Looping through dictionaries - You can loop through all the key-value pairs in a dictionary by using a for loop. 
for key, value in my_dict.items():

3. If-else statements - If-else statements allow you to check if a condition is true or false, and execute different code depending on the result. 
if n % 2 == 0: result = "even" else: result = "odd"

4. Counting occurrences - You can count the number of occurrences of a value in a list by using the count() method. 
fruits_list.count('apple')

5. Creating a new dictionary - You can create a new dictionary by using a dictionary comprehension. 
{key: value for key, value in my_list}

Hint
count_values
- You will need to use a loop to iterate over the key-value pairs in the input dictionary
- To check if a value is unique or not, you can use a conditional statement and a membership test to check if the value is already in the new dictionary as a key
- If a value is not in the new dictionary, add it as a key with a value of 1
- If a value is already in the new dictionary, increment the value of the key by 1 each time it is found in the input dictionary
- Finally, return the new dictionary that you have created
"""
# My Code

        
# Solution
	def count_values(d):
		result = {}
		for value in d.values():
		  if value in result:
		    result[value] += 1
		  else:
		    result[value] = 1
		return result

# IA's Solutions
# Certainly! Here is an alternative solution to the problem in Python using the Counter class from the collections module:
from collections import Counter
def count_values(d):
    return dict(Counter(d.values()))
# Test the function with the provided examples
print(count_values({'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}))  # Output: {1: 2, 2: 2, 3: 1}
print(count_values({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}))  # Output: {'fruit': 2, 'vegetable': 1}
# Explanation:
# 1. We import the Counter class from the collections module, which provides a convenient way to count the occurrences of elements in a list (or in this case, values in a dictionary).
# 2. Inside the `count_values` function, we create a Counter object using `Counter(d.values())`, which counts the occurrences of each unique value in the input dictionary `d`.
# 3. The result of the Counter is then converted back to a regular dictionary using the dict() constructor, which gives us the desired output format where keys are unique values and values are the counts of their occurrences.





# https://www.codingdors.com/problem/239
"""
nested_value
Show Solution
Given a nested dictionary and a list of keys, return the value at the specified depth in the nested dictionary. If any key is not present, return False.

nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']) -> 1
nested_value({'key': 'value'}, ['key', 'missing']) -> False
nested_value({'fruit': {'apple': {'color': 'red'}}}, ['fruit', 'apple', 'color']) -> 'red'

Theory
nested_value
1. Recursion - A function calling itself during its execution. 
Example: 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

2. Dictionary - A collection of key:value pairs enclosed in curly braces {}.
Example:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

3. Nested Dictionary - A dictionary within a dictionary.
Example:
my_dict = {'person':{'name': 'John', 'age': 25, 'city': 'New York'}, 'job':{'title': 'Software Engineer', 'experience': 2}}

4. List - A collection of elements enclosed in square brackets [].
Example:
my_list = [1,2,3,4,5]

5. Key - An identifier that is used to access the value in a dictionary.
Example:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name']) #Output: John

6. Value - Data associated with a key in a dictionary.
Example:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['age']) #Output: 25

Hint
nested_value
1. Identify the depth of the required value in the nested dictionary.
2. Traverse the dictionary using the list of keys provided.
3. Check if each key exists in the dictionary at each level.
4. If any key is not present, return None.
5. If all keys are present, return the value at the specified depth in the nested dictionary.
"""
# My Code

        
# Solution
	def nested_value(d, keys):
		for key in keys:
		  if key in d:
		    d = d[key]
		  else:
		    return False
		return d

# IA's Solutions
# Sure! Here is an alternative solution using recursion:
def nested_value(d, keys):
    if not keys:
        return False
    if len(keys) == 1:
        return d.get(keys[0], False)
    if keys[0] not in d:
        return False
    return nested_value(d[keys[0]], keys[1:])
# In this alternative solution, the function `nested_value` recursively calls itself with the nested dictionary and the remaining keys in the list. This solution also handles cases where the list of keys is empty or has only one key. If the key is not present in the dictionary, it returns False. Otherwise, it continues to the next level of nesting until the specified depth is reached or a key is missing.




