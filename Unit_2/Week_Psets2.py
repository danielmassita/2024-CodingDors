# https://cs50.harvard.edu/python/2022/psets/2/





# https://cs50.harvard.edu/python/2022/psets/2/camel/

	# Get the input from the user
	camelCase = input("camelCase: ")
	
	# Print "snake_case: "
	print("snake_case: ", end="")
	
	# Loop through every letter
	for letter in camelCase:
	
		# Check if letter is upper case
	    if letter.isupper():
	      # Print underscores and the letter in lowercase
	      print('_' + letter.lower(), end="")
	
	    # Otherwise, print letter
	    else:
	      print(letter, end="")
	
	# Print space in the end to next line
	print()





# https://cs50.harvard.edu/python/2022/psets/2/coke/

	# Variable to keep track of the amount...
	amount_due = 50
	
	# Loop until the amount_due is greater than 0...
	while amount_due > 0:
	  # Print the amount due
	  print("Amount Due:",amount_due)
	  # Ask user to insert a coin
	  coin = int(input("Insert Coin: "))
	  # Check if the coin is acceptable (25, 10, 5)...
	  if coin in [25, 10, 5]:
	    # Substract value from amount_due...
	    amount_due -= coin
	
	# Calculate change_owed ...
	change_owed = abs(amount_due)
	# Print the result
	print("Change Owed:",change_owed)





# https://cs50.harvard.edu/python/2022/psets/2/twttr/

	# Get the input from the user
	message = input("Input: ")
	
	# Print the "Output: "
	return_message = print("Output: ", end="")
	
	# Loop through every single char/letter
	for letter in message:
	#    print(letter)
	
	    # Check if it is a vowel or not, also in lower and upper cases
	    if not letter.lower() in ["a", "e", "i", "o", "u"]:
	        # Print the letter (if not vowel)
	        print(letter, end="")
	# Print the new line
	print()





# https://cs50.harvard.edu/python/2022/psets/2/plates/

	def main():
	    plate = input("Plate: ")
	    if is_valid(plate):
	        print("Valid")
	    else:
	        print("Invalid")
	
	def is_valid(s):
	    # Max of 6 chars (int's or str's)
	    # Min of 2 chars
	    if len(s) < 2 or len(s) > 6:
	        return False
	
	    # All must start with at least two letters - s[0:2] + .isalpha()
	    if s[0].isalpha() == False or s[1].isalpha() == False:
	        return False
	
	    # Numbers can't be in the middle, only in the end
	    for i in range (len(s)):
	        if s[i].isdigit():
	            if not s[i:].isdigit():
	                return False
	    # E.g.: AAA222 is Valid, AAA22A is Invalid
	    # First number of numbers can't be 0
	    i = 0
	    while i < len(s):
	        if s[i].isalpha() == False:
	            if s[i] == '0':
	                return False
	            else:
	                break
	        i += 1
	
	    # No periods, spaces, punctuations ! ?
	    for char in s:
	        if char in ['.', ' ', '!', '?']:
	            return False
	
	    # If OK for all tests, return True
	    return True
	
	main()





# https://cs50.harvard.edu/python/2022/psets/2/nutrition/

	# Dict with all fruits and calories
	fruits = {
	    "apple": 130,
	    "avocado": 50,
	    "banana": 110,
	    "cantaloupe": 50,
	    "grapefruit": 60,
	    "grapes": 90,
	    "honeydew melon": 50,
	    "kiwifruit": 90,
	    "lemon": 15,
	    "lime": 20,
	    "nectarine": 60,
	    "orange": 80,
	    "peach": 60,
	    "pear": 100,
	    "pineapple": 50,
	    "plums": 70,
	    "strawberries": 50,
	    "sweet cherries": 100,
	    "tangerine": 50,
	    "watermelon": 80,
	}
	
	# Get user's input, case insensitive
	fruit_asked = input("Item: ").lower()
	# print(fruit_asked)
	
	# Loop through fruits dictionary
	for key in fruits:
	#    print(key)
	#    print(fruits[key])
	
	    # Find the fruit asked (remember lowercase)
	    if key  == fruit_asked:
	        # Print calories
	        print("Calories:", fruits[key])




