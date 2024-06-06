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

Theory
count_lower_letters
Every character in a string corresponds to an index, starting with 0 for the first character. You can access any character in a string by referring to its index.
my_string = "Hello"
first_char = my_string[0]  # This will be 'H'
You can loop through the characters in a string using a for loop. This lets you examine or operate on each character individually.
for char in "Hello":
    print(char)
The islower() method returns True if the character is a lowercase letter, otherwise it returns False.
letter = "a"
result = letter.islower()  # This will be True
While iterating over a sequence, you can maintain a counter that you increment whenever a certain condition is met.
count = 0
for num in [1, 2, 3, 2, 4, 2]:
    if num == 2:
        count += 1
# count will be 3 after this loop

Hint
count_lower_letters
1. For each character, determine if it's lowercase. There's a built-in Python method for strings that helps with this.
2.Consider using a variable (e.g., count) to keep track of the number of lowercase letters you encounter as you iterate through the string.
3. Once you've finished iterating over the entire string, count should hold the total number of lowercase letters. This will be your final answer to return.
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
find_char
Show Solution
Write a function that returns the index of the first occurrence of a specified character in a given string or -1 if the character is not present.
find_char('banana', 'b') -> 0
find_char('hello', 'l') -> 2
find_char('code', 'a') -> -1

Theory
find_char
1. Strings: Strings are a sequence of characters enclosed in single, double, or triple quotes. They are immutable and each character can be accessed by its index. 
'I am a string'
 is an example of a string.
2. Indexing: Indexing is the way we access individual elements in a sequence. It is done using a numeric index inside square brackets. The first element in a sequence has an index of 0. 
'hello'[1]
 will return 'e'.
3. for loop: A for loop is used to iterate over a sequence of elements. It is used to execute a block of code repeatedly. 
for item in sequence:
 is the syntax for a for loop.
4. if statement: An if statement is used to check a condition and execute a block of code if the condition is true. 
if condition:
 is the syntax. 
5. return statement: A return statement is used to exit a function and return a value to the caller. 'return value' is the syntax. Example:
# Example for indexing
word = 'hello'
print(word[1]) # output is 'e'
# Example for for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit) # outputs the fruits in a new line each
# Example for if statement and return statement
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4)) # output is True

Hint
find_char
1. The function should take two arguments: a string and a character to search for.
2. Use a loop to iterate through each character in the string.
3. Check if the current character matches the character being searched for.
4. If there is a match, return the index of that character in the string.
5. If the loop finishes without finding a match, return -1.
"""
# My Code


# Solution
  def find_char(s: str, char_to_find: str) -> int:
    for i in range(len(s)):
    	if char_to_find.lower() in s[i].lower():
    	   return i
    return -1

# IA's Solutions
# Certainly! Here is an alternative solution using the `index` method:
def find_char(s: str, char_to_find: str) -> int:
    try:
        index = s.lower().index(char_to_find.lower())
        return index
    except ValueError:
        return -1
# In this solution, we convert both the input string and the character to find to lowercase using the `lower()` method before searching for the character using the `index` method. If the character is found, the index of the first occurrence is returned. If the character is not found, a `ValueError` is raised, and we return -1.





# https://www.codingdors.com/problem/287
"""
contains_special_chars
Show Solution
Write a function that checks if the string contains either an exclamation mark (!) or a question mark (?). The function should return True if either (or both) of these characters are present, and False otherwise.
contains_special_chars("Hello! Welcome") → True
contains_special_chars("What is your name") → False
contains_special_chars("How are you?") → True

Theory
contains_special_chars
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
For each char, check if it is equals to '!' or '?'.

Hint
contains_special_chars
1. Use Python string methods to check for the presence of characters in a string.
2. You have to check for two characters. Think about how you can efficiently check for both in one pass.
"""
# My Code
  def contains_special_chars(s: str) -> bool:
      especiais = ['!', '?']
      for char in s:
          if char in especiais:
              return True
      return False

# Solution
  def contains_special_chars(s: str) -> bool:
  	for i in s:
  	  if i == '!' or i == '?':
  	    return True
  	return False

# IA's Solutions
# 1. Using the any() function with a generator expression:
def contains_special_chars(s: str) -> bool:
    return any(char in ['!', '?'] for char in s)
# This solution utilizes the any() function along with a generator expression to iterate through the characters in the string and check if any of them are either '!' or '?'. It returns True if any special character is found, and False otherwise.
# 2. Using the set intersection method:
def contains_special_chars(s: str) -> bool:
    return bool(set(s) & set('!?'))
# This solution converts both the string and the special characters '!' and ? into sets and then calculates their intersection. If the intersection is not empty, it means that at least one special character is present in the string, so it returns True.
# 3. Using the any() function with a lambda function:
def contains_special_chars(s: str) -> bool:
    return any(map(lambda x: x in ['!', '?'], s))
# This solution combines the any() function with a lambda function to check if any character in the string is either '!' or '?'. It returns True if any special character is found, and False otherwise.





# https://www.codingdors.com/problem/283
"""
find_uppercase_position
Show Solution
Write a function that returns the position (index) of the first uppercase letter in a given string 's'. If there are no uppercase letters in the string, the function should return -1.
find_uppercase_position("hello World") → 6
find_uppercase_position("nouppercasehere") → -1
find_uppercase_position("CodingDors") → 0

Theory
find_uppercase_position
Every character in a string corresponds to an index, starting with 0 for the first character. You can access any character in a string by referring to its index.
my_string = "Hello"
first_char = my_string[0]  # This will be 'H'
You can loop through the characters in a string using a for loop. This lets you examine or operate on each character individually.
for char in "Hello":
    print(char)
The islower() method returns True if the character is a lowercase letter, otherwise it returns False.
letter = "a"
result = letter.islower()  # This will be True
While iterating over a sequence, you can maintain a counter that you increment whenever a certain condition is met.
count = 0
for num in [1, 2, 3, 2, 4, 2]:
    if num == 2:
        count += 1
# count will be 3 after this loop

Hint
find_uppercase_position
1. For each character in the string, use a Python string method to check if it is uppercase.
2. If you find an uppercase letter, immediately return its position (index).
3. If the loop completes without finding an uppercase letter, return -1.
"""
# My Code
  def find_uppercase_position(s: str) -> int:
      for i in range(len(s)):
          if s[i].isupper():
              return i
      return -1

  def find_uppercase_position(s: str) -> int:
      for i, char in enumerate(s):
          if char.isupper():
              return i
      return -1

# Solution
  def find_uppercase_position(s: str) -> int:
      for i in range(len(s)):
          if s[i].isupper():
              return 1
      else:
          return -1

# IA's Solutions
# Alternative Solution 0:
def find_uppercase_position(s: str) -> int:
    for i, char in enumerate(s):
        if char.isupper():
            return i
    return -1
# Alternative Solution 1:
def find_uppercase_position(s: str) -> int:
    return next((i for i, char in enumerate(s) if char.isupper()), -1)
# Explanation: This solution uses a generator expression inside the next function to iterate over the characters in the string and return the index of the first uppercase letter found. If no uppercase letter is found, it returns -1 using the default argument of next.
# Alternative Solution 2:
def find_uppercase_position(s: str) -> int:
    return s.index(next((char for char in s if char.isupper()), None))
# Explanation: This solution also uses a generator expression to find the first uppercase letter in the string, and then uses the index method to get the index of that letter in the original string. If no uppercase letter is found, it returns None which will raise a ValueError, hence it's important to handle this exception if using this approach.





# https://www.codingdors.com/problem/282
"""
extract_uppercase
Show Solution
Write a function that extracts all the uppercase letters from the given string 's' and return them as a new string in the order they appear.
extract_uppercase("Hello World") → "HW"
extract_uppercase("nouppercasehere") → ""
extract_uppercase("CODINGDORS") → "CODINGDORS"

Theory
extract_uppercase
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
isupper() method returns True if a character is uppercase and False otherwise.
letter = "A"
result = letter.isupper()  # This will yield True
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
extract_uppercase
1. For each character, check if it's an uppercase letter using a Python string method.
2. If the character is uppercase, append it to your initialized string or list.
3. After iterating over all characters, your string or list should contain all the uppercase letters from s.
4. Convert the list to a string if you used a list, and return the result. If you used a string, simply return it.
"""
# My Code
  def extract_uppercase(s: str) -> str:
      resultado = ""
      for char in s:
          if char.isupper() == True:
              resultado += char
      return resultado
          
# Solution
  def extract_uppercase(s: str) -> str:
      word = ''
      for i in s:
        if i.isupper():
          word = word + i
      return word

# IA's Solutions
# 1. Using list comprehension:
def extract_uppercase(s: str) -> str:
    return ''.join([char for char in s if char.isupper()])
# In this solution, a list comprehension is used to iterate over each character in the string 's' and only append the character to the list if it is uppercase. The list is then joined back together to form a new string containing only the uppercase letters.
# 2. Using filter and lambda function:
def extract_uppercase(s: str) -> str:
    return ''.join(filter(lambda char: char.isupper(), s))
# In this solution, the filter function is used along with a lambda function to filter out only the uppercase letters from the string 's'. The filtered characters are then joined back together to form a new string.





# https://www.codingdors.com/problem/284
"""
replace_a_with_four
Show Solution
Write a function that returns a new string where every instance of the letter 'a' (both uppercase and lowercase) in the given string 's' is replaced with the number '4'.
replace_a_with_four("Banana") → "B4n4n4"
replace_a_with_four("Apples are Amazing!") → "4pples 4re 4m4zing!"
replace_a_with_four("CodingDors") → "CodingDors"

Theory
replace_a_with_four
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
isupper() method returns True if a character is uppercase and False otherwise.
letter = "A"
result = letter.isupper()  # This will yield True
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
replace_a_with_four
1. Remember the problem requires you to replace both uppercase 'A' and lowercase 'a'. Consider converting the string to a uniform case before replacing, or use a method that can replace both cases simultaneously.
2. For each instance of 'a' or 'A' found, replace it with '4'.
3. After processing the entire string, return the modified string.
"""
# My Code
  def replace_a_with_four(s: str) -> str:
      p4l4vr4s = ""
      for char in s:
          if char == 'a' or char == 'A':
              char = '4'
              p4l4vr4s += char
          else:
              p4l4vr4s += char
      return p4l4vr4s
          
# Solution
  def replace_a_with_four(s: str) -> str:
  	word = ''
  	for i in s:
  	  if i.lower() == 'a':
  	    word = word + '4'
  	  else:
  	    word = word + i
  	return word

# IA's Solutions
# Sure! Here is an alternative solution using list comprehension:
def replace_a_with_four(s: str) -> str:
    return ''.join(['4' if char.lower() == 'a' else char for char in s])
# In this solution, we use list comprehension to iterate over each character in the input string `s`. We check if the lowercase version of the character is equal to 'a', and if it is, we replace it with '4'. Otherwise, we keep the character as is. Finally, we use `join()` to convert the list of characters back into a string.





# https://www.codingdors.com/problem/286
"""
replace_upper
Show Solution
Write a function that returns a new string where every uppercase letter from the given string 's' is replaced with an underscore (_).
replace_upper("helloWorld") → "hello_orld"
replace_upper("replaceUppeR") → "replace_ppe_"
replace_upper("cOdInG") → "c_d_n_"

Theory
replace_upper
A for loop can be employed to traverse through each character in a string, facilitating individual examination or manipulation.
for char in "Hello":
    print(char)
isupper() method returns True if a character is uppercase and False otherwise.
letter = "A"
result = letter.isupper()  # This will yield True
You can combine strings using the + operator. This action doesn't alter the original strings but yields a new string.
word1 = "Open"
word2 = "AI"
combined = word1 + word2  # "OpenAI"

Hint
replace_upper
1. Utilize Python string methods to identify uppercase letters.
2. For each uppercase letter found, replace it with an underscore.
3. Consider iterating over the string and building a new string based on the conditions mentioned.
"""
# My Code
  def replace_upper(s: str) -> str:
      replaced_uppers = ""
      for char in s:
          if char.isupper() == True:
              replaced_uppers += "_"
          else:
              replaced_uppers += char
      return replaced_uppers

# Solution
  def replace_upper(s: str) -> str:
  	word = ''
  	for i in s:
  	  if i.isupper():
  	    word = word + '_'
  	  else:
  	    word = word + i
  	return word

# IA's Solutions
# 1. Using list comprehension:
def replace_upper(s: str) -> str:
    return ''.join(['_' if char.isupper() else char for char in s])
# This solution uses list comprehension to iterate over each character in the input string 's'. If the character is uppercase, it replaces it with an underscore ('_'), otherwise, it keeps the character as it is. Finally, it joins all the characters back together to form the final replaced string.
# 2. Using a generator expression:
def replace_upper(s: str) -> str:
    return ''.join('_' if char.isupper() else char for char in s)
# This solution is similar to the previous one but uses a generator expression instead of a list comprehension. The main advantage of using a generator expression is that it is more memory efficient as it generates the values on-the-fly without creating a list in memory.
# 3. Using a regular expression:
import re
def replace_upper(s: str) -> str:
    return re.sub(r'[A-Z]', '_', s)
# This solution uses the `re.sub()` function from the `re` module to replace all uppercase letters (A-Z) in the input string 's' with an underscore ('_'). This is a more concise and efficient way to achieve the desired result using regular expressions.





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






