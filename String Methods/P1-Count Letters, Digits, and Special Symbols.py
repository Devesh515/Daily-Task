# 1. Program to count letters, digits, and special symbols in a string

string = input('Enter your string : ').strip().lower()  # Take input and convert to lowercase
char_count, digits_count, symbols_count = 0, 0, 0  # Initialize counters

# Loop through each character in the string
for char in string:
    if char.isalpha():  # Check if character is a letter
        char_count += 1
    elif char.isdigit():  # Check if character is a digit
        digits_count += 1
    elif not char.isspace():  # Check if character is a special symbol
        symbols_count += 1

# Print the results
print('Total number of characters in the string is:', char_count)
print('Total number of digits in the string is:', digits_count)
print('Total number of symbols in the string is:', symbols_count)

