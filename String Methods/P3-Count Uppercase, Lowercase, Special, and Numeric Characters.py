# 3. Program to count uppercase, lowercase, special, and numeric characters in a string

string = input('Enter your string : ').strip()  # Take input and strip whitespace
upper_count, lower_count, special_count, numeric_count = 0, 0, 0, 0  # Initialize counters

# Loop through each character in the string
for char in string:
    if char.isupper():  # Check if character is uppercase
        upper_count += 1
    elif char.islower():  # Check if character is lowercase
        lower_count += 1
    elif not char.isalnum() and not char.isspace():  # Check for special character
        special_count += 1
    elif char.isdigit():  # Check if character is a digit
        numeric_count += 1

# Print the results
print('Total uppercase characters are:', upper_count)
print('Total lowercase characters are:', lower_count)
print('Total special characters are:', special_count)
print('Total numeric characters are:', numeric_count)

