1. Write a Python program to handle a ZeroDivisionError exception when dividing a
   number by zero.

try:
    # Take user input for division
    number1 = float(input("Enter the numerator: "))
    number2 = float(input("Enter the denominator: "))
    
    # Perform the division
    result = number1 / number2
    print("The result of division is:", result)

except ZeroDivisionError:
    # Handle division by zero error
    print("Error: You cannot divide by zero!")



