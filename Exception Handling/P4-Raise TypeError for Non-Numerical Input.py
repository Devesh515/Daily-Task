''' 4. Write a Python program that prompts the user to input two numbers and raises a
   TypeError exception if the inputs are not numerical  '''

# Function to get two numbers and check if they are numbers
def get_numbers():
    try:
        # Ask the user to enter two numbers
        number1 = input("Enter the first number: ")
        number2 = input("Enter the second number: ")

        # Try to convert the inputs to numbers
        number1 = float(number1)
        number2 = float(number2)

        # Return the numbers if successful
        return number1, number2

    except ValueError:
        # If the input is not a number, raise an error
        raise TypeError("Both inputs must be numbers!")

# Main code
try:
    # Get two numbers
    number1, number2 = get_numbers()
    print("The numbers you entered are: ", number1, "and", number2)

except TypeError as e:
    # If there's an error, show the error message
    print("Error: ", e)

