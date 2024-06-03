"""
CODING DORS
UNIT 2 - LOOPS - https://cs50.harvard.edu/python/2022/notes/2/
WEEK 6 - Strings 2 - https://www.codingdors.com/week/6
"""





# https://www.codingdors.com/problem/133
"""
count_char
Show Solution
Write a function that counts the occurrences of a specified character in a given string.
count_char('hello', 'l') -> 2
count_char('code', 'd') -> 1
count_char('banana', 'a') -> 3

Theory
count_char
1. Variables that are passed into a function when calling it. These parameters allow the function to accept different input values for processing. 
def example(parameter1, parameter2):
2. A way of accessing specific characters in a string. Each character in the string has an index position starting from 0 for the first character. For example, in the string "hello", the first (leftmost) letter 'h' has an index position of 0, the second letter 'e' has an index position of 1, and so on. 
string_var[index]
3. Statements that execute different code paths based on a condition being met. In Python, the if, elif, and else keywords are used to create conditional statements. For example: 
if condition1:
  # code block 1
elif condition2:
  # code block 2
else:
  # code block 3
4.  A way of iterating over a sequence of items, such as a string or a list. The 'for' keyword is used, along with a temporary variable to hold each item in the sequence as it's being processed. For example: 
for item in sequence:
  # do something with item
5. The process of combining two or more strings into a single string. In Python, the + operator is used for concatenation. For example: 
"hello" + "world"
 would result in the string "helloworld".

Hint
count_char
1. You will need to use a loop to iterate through each character in the string.
2. You will need to use an if statement to check if the current character is the specified character.
3. You will need to use a counter variable to keep track of how many times the specified character appears in the string.
4. At the end of the loop, you will need to return the counter variable.
"""
# My Code
  def count_char(s: str, char_to_count: str) -> int:
      contagem = 0
      for char in s:
          if char.lower() == char_to_count.lower():
              contagem += 1
          else:
              contagem += 0
      return contagem

# Solution
  def count_char(s: str, char_to_count: str) -> int:
  	count = 0
  	for i in s:
  	  if i.lower() == char_to_count.lower():
  	    count = count + 1
  	return count

# IA's Solutions
# 1. Using the `count()` method:
def count_char(s: str, char_to_count: str) -> int:
    return s.count(char_to_count)
# Explanation: The `count()` method in Python is a built-in method for strings that returns the number of occurrences of a specified substring or character in the given string. This solution simply leverages the `count()` method to directly calculate the count of the specified character in the string `s`.
# 2. Using list comprehension:
def count_char(s: str, char_to_count: str) -> int:
    return sum(1 for char in s if char == char_to_count)
# Explanation: This solution uses a list comprehension to create a list of `1` for each occurrence of the specified character in the string `s`. The `sum()` function then sums up all the `1` values, effectively counting the occurrences of the specified character.





# https://www.codingdors.com/problem/281
"""
count_lower_letters
Show Solution
Write a function that counts the number of lowercase letters present in a given string 's'.
count_lower_letters("Hello World") → 8
count_lower_letters("LOWERCASE") → 0
count_lower_letters("MixedCase123") → 5
"""
# My Code
  def count_lower_letters(s: str) -> int:
      contador_islower = 0
      for char in s:
          if char.islower():
              contador_islower += 1
      return contador_islower

# Solution
  def count_lower_letters(s: str) -> int:
  	count = 0
  	for i in s:
  	  if i.islower() == True:
  	    count = count + 1
  	return count

# IA's Solutions
# Sure! Here's an alternative solution to count the number of lowercase letters in a string in Python:
def count_lower_letters(s: str) -> int:
    return sum(1 for char in s if char.islower())
# In this solution, a generator expression `1 for char in s if char.islower()` is used within the `sum()` function to count the number of occurrences where `char` is a lowercase letter in the string `s`. The `sum()` function then adds up the number of occurrences and returns the total count of lowercase letters in the string.
# This solution leverages the power of generator expressions and the `sum()` function to provide a concise and efficient way to count lowercase letters in a string.





# https://www.codingdors.com/problem/128
"""
count_vowels_str
Show Solution
Write a function that counts the number of vowels in a given string.
count_vowels_str('hello') -> 2
count_vowels_str('codingDORS') -> 3
count_vowels_str('APPLEbanana') -> 5

Theory
count_vowels_str
1. Strings: A sequence of characters 
string = 'hello'
2. Loops: Execute a block of code repeatedly 
for char in string:
3. Conditionals: Execute different code depending on a condition 
if char in vowels:
4. Counters: Keep track of a running total 
count += 1
5. Vowels: Letters A, E, I, O, U (including lowercase) 
vowels = 'aeiouAEIOU'

Hint
count_vowels_str
- The function should take a string as input.
- You will need to define a list of vowels.
- Loop over each character in the input string and check if it's a vowel.
- If the character is a vowel, add 1 to a counter variable.
- Return the counter variable at the end of the loop.
"""
# My Code
  def count_vowels_str(s: str) -> int:
      contador_vogais = 0
      lista_vogais = ['a', 'e', 'i', 'o', 'u']
      for char in s.lower():
          if char in lista_vogais:
              contador_vogais += 1
      return contador_vogais

# Solution
  def count_vowels_str(s: str) -> int:
  	vowels = ['a', 'e', 'i', 'o', 'u']
  	count = 0
  	for i in s:
  	  if i.lower() in vowels:
  	    count = count + 1
  	return count

# IA's Solutions
# 1. Using a dictionary to store the vowels:
def count_vowels_str(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in s.lower() if char in vowels)
# Explanation: In this solution, we use a set to store the vowels. We then use a generator expression inside the sum function to iterate through each character in the string, check if it is a vowel, and count the number of vowels found.
# 2. Using the count method:
def count_vowels_str(s: str) -> int:
    return sum(s.lower().count(v) for v in ['a', 'e', 'i', 'o', 'u'])
# Explanation: This solution takes advantage of the count method available for strings, which returns the number of occurrences of a specific substring in the given string. We use a list comprehension to iterate through each vowel in the list and count the number of occurrences of each vowel in the string 's'. Finally, we sum up the counts for each vowel to get the total number of vowels in the string.
def count_vowels_str(s: str) -> int:
    vowels = "aeiouAEIOU"
    contador_vogais = 0
    for char in s:
        if char in vowels:
            contador_vogais += 1
    return contador_vogais





# https://www.codingdors.com/problem/129
"""
count_consonants_str
Show Solution
Write a function that counts the number of consonants in a given string.
count_consonants_str('hello') -> 3
count_consonants_str('codingDORS') -> 7
count_consonants_str('APPLEbanana') -> 6

Theory
count_consonants_str
1. Strings in Python: A string is a sequence of characters enclosed in quotes. Strings are immutable, meaning that once a string is created, it cannot be modified. 
'hello'
2. For loop: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). 
for char in 'hello':
3. Conditional statements: Conditional statements allow you to execute different code depending on the state of your program at runtime. 
if char not in ['a', 'e', 'i', 'o', 'u']:
4. Counter: A counter is a variable used to keep track of something, typically the number of occurrences of a particular value. 
count = 0

Hint
count_consonants_str
1. Remember that vowels are a, e, i, o, and u. Any letter that is not a vowel is a consonant. 
2. You can use the lower() method to convert all letters in the string to lowercase for easier comparison. 
3. You can initiate a counter variable to keep track of the number of consonants found. 
4. Use a for loop to iterate through each letter in the string. 
5. Use an if statement to check if the letter is a consonant. If so, increment the counter variable.
"""
# My Code
  def count_consonants_str(s: str) -> int:
      nao_consoantes = ['a', 'e', 'i', 'o', 'u']
      contador_consoantes = 0
      for char in s.lower():
          if char not in nao_consoantes:
              contador_consoantes += 1
      return contador_consoantes

# Solution
  def count_consonants_str(s: str) -> int:
  	vowels = ['a', 'e', 'i', 'o', 'u']
  	count = 0
  	for i in s:
  	  if i.lower() not in vowels:
  	    count = count + 1
  	return count

# IA's Solutions
# 1. Using Regular Expressions:
import re
def count_consonants_str(s: str) -> int:
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', s.lower())
    return len(consonants)
# This solution uses the `re.findall()` function from the `re` module to find all consonants in the string using a regular expression pattern. The pattern `[bcdfghjklmnpqrstvwxyz]` matches any lowercase consonant. Then it returns the count of consonants found.
# 2. Using Set Intersection:
def count_consonants_str(s: str) -> int:
    vowels = 'aeiou'
    consonants = set(s.lower()) - set(vowels)
    return len(consonants)
# In this solution, we first define a set of vowels and then create a set of all unique characters in the given string excluding vowels. Finally, it returns the count of consonants in the set.





# https://www.codingdors.com/problem/132
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





# https://www.codingdors.com/problem/
"""

"""
# My Code


# Solution


# IA's Solutions






