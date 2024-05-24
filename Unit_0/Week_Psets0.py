# https://cs50.harvard.edu/python/2022/psets/0/





# https://cs50.harvard.edu/python/2022/psets/0/indoor/

# Let's ask something to the user...
thoughts = input("Hello, dear! A penny for your thoughts...? ")

# Print in lowercase using the str.lower() method...
print(thoughts.lower())





# https://cs50.harvard.edu/python/2022/psets/0/playback/

# Prompt an input to the user...
thoughts = input("A penny for your thoughts! What would David Malan say? ")

# Change any white space " " for three dots "..."
slowMotion = thoughts.replace(" ", "...")

# Return the input updated to three dots spaces...
print(f"Regular speed: {thoughts}")
print(f"Slow motion: {slowMotion}")





# https://cs50.harvard.edu/python/2022/psets/0/faces/

def main():
    # Input from the usser...
    message = input("Say something using emoticon... ")

    # Call the function to work... REMEMBER TO ALWAYS CALL THE FUNCTION
    resultado = convert(message)

    # Print the output...
    print(resultado)

def convert(message): # TYPE ERROR - I NEED TO USE ANY ARGUMENT PREVIOUSLY ASSIGNED... DDDUUUHHHH from line 6
    # Change :) for slightly smilling face
    messageStep1 = message.replace(":)", '🙂')

    # Change :( for slightly sad face
    messageStep2 = messageStep1.replace(":(", '🙁')

    # Now, we have both textUser > textUser1 > textUser2 chained to avoid overleaping replaces...
    return messageStep2

main()






# https://cs50.harvard.edu/python/2022/psets/0/einstein/

# Let's organize the ideas... E = M.(C^2) or in Python E = M.(C ** 2)

# Ask the user for the mass (kg) aware that the input typeof() is STR...
mass = int(input("Informe a massa (kg): "))
# print(mass * 2) # ERROR - it's gonna assume STR and return "massmass"

lightSpeed = int(300000000)
energy = mass * (lightSpeed ** 2)

print(energy)
print(f"Using E=m.c², given mass ({mass} kg) and c ({lightSpeed:,} m/s), the total Energy is: {energy:,} Joules.")





# https://cs50.harvard.edu/python/2022/psets/0/tip/

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # From the variable "dollars" we assigned d from an input, so it is a STR...
    dolarsNoSymbols = d.replace("$", "") # Let's use the method .replace() to extract the symbol $.
    return float(dolarsNoSymbols) # Inside FLOAT formats to force from STR to FLOAT

def percent_to_float(p):
    # From the variable "percent" we assigned p from an input, so it is a STR...
    percentNoSymbols = p.replace("%", "") # Still a STR type...
    pDecimal = float(percentNoSymbols) / 100 # Still STR, so FLOAT to change types...
    return pDecimal

main()
