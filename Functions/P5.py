''' 5. Write a lambda function that takes one argument and returns 'Positive' if the number is
greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different
numbers. '''

# Define the lambda function
check_number = lambda num: 'Positive' if num > 0 else 'Negative' if num < 0 else 'Zero'

# Test the lambda function with different numbers
print(check_number(10))   
print(check_number(-5))   
print(check_number(0))    

