#1.Using input() function take one number from the user and using ternary operatorscheck whether the number is even or odd

# enter a number
number = int(input("Enter a number: "))

# Check number is even or odd 
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number {number} is {result}.")
