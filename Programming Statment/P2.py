#2.Using input function take two number and then swap the number

# First number as input 
number1 = input("Enter the first number: ")

# Second number as input 
number2 = input("Enter the second number: ")

# Swap the numbers 
temp = number1
number1 = number2
number2 = temp

# Print the swapped numbers
print(f"After swapping: First number = {number1}, Second number = {number2}")
