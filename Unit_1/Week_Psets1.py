# https://cs50.harvard.edu/python/2022/psets/1/





# https://cs50.harvard.edu/python/2022/psets/1/deep/

# Get the input from the user, handing The Question...
TheAnswer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Print Yes if the answer is 42 realted...
if TheAnswer.strip() == "42": # "42" avoids the input from being an INT, and marks it as STR...
    print("Yes")
elif TheAnswer.lower().strip() == "forty-two": # We use the .lower() method...
    print("Yes")
elif TheAnswer.lower().strip() == "forty two": # Also we use the .strip() to exclude blank spaces before and after...
    print("Yes")

# Print No in elses cases...
else:
    print("No")





# https://cs50.harvard.edu/python/2022/psets/1/bank/

# Ask for the greetings from the user...
greeting = input("Greeting: ").strip().lower()

# Validate the answer without "hello"
if "hello" in greeting: #.strip().lower():
    print("$0")

# Validate the answer if starts with an "h"
elif "h" == greeting[0]:
    print("$20")

# Validate diferent types...
else:
    print("$100")





# https://cs50.harvard.edu/python/2022/psets/1/extensions/

# Input from the user (remove white spaces and case insensitive)...
FileName = input("File name: ").lower().strip()

# If format (gif, jpg, jpeg, png) DOES EXIST, print "image/type"...
if ".gif" in FileName:
    print("image/gif")
elif ".jpg" in FileName:
    print("image/jpeg") # Read documentation Commom MIME types, both uses jpeg...
elif ".jpeg" in FileName:
    print("image/jpeg")
elif ".png" in FileName:
    print("image/png")

# If format pdf/zip DOES EXIST, print "application/type"...
elif ".pdf" in FileName:
    print("application/pdf")
elif ".zip" in FileName:
    print("application/zip")

# If format txt DOES EXIST, print "text/plain"...
elif ".txt" in FileName:
    print("text/plain")

# Any other result by default...
else:
    print("application/octet-stream")





# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

# Get the input from the user
expression = input("Expression: ")

# Convert the input into VAR
x, y, z = expression.split(" ")

# Change the type of the variable x and z to float.
new_x = float(x)
new_z = float(z)

# Calculate!

if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z

print(round(result, 1))





# https://cs50.harvard.edu/python/2022/psets/1/meal/

def main():
    # Get time from user
    answer = input("What time is it? ")

    # Call the convert function
    time = convert(answer)

    # Breakfast (7 - 8)
    if time >= 7 and time <= 8:
        print("breakfast time")

    # Lunch (12 - 13)
    if time >= 12 and time <= 13:
        print("lunch time")

    # Dinner (18-19)
    if time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    # Get hour and minutes
    hours, minutes = time.split(":")

    # Convert time strings into floats
    new_minute = float(minutes) / 60

    # Return the result to main function
    return float(hours) + new_minute

if __name__ == "__main__":
    main()




