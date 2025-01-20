# 4. Program to count vowels in a string

string = input('Enter your string : ').strip().lower()  # Take input and convert to lowercase
vowels_count = 0  # Initialize vowels counter

# Loop through each character in the string
for char in string:
    if char in 'aeiou':  # Check if character is a vowel
        vowels_count += 1

# Print the results
print('String is:', string)
print('Total number of vowels in the string is:', vowels_count)
