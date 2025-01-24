''' 2. Write a Python program that prompts the user to input an integer and raises a
   ValueError exception if the input is not a valid integer. '''

try:
    # Get input from user
    user_input = input("Enter an integer: ")
    
    # Convert input to integer
    number = int(user_input)
    
    # Print the number
    print("You entered:", number)
    
except ValueError:
    # Handle if input is not a valid integer
    print("That's not a valid integer!")


