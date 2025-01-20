#4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training”
# Given string
my_string = "Welcome to python Training"

# Define vowels
vowels = "aeiou"

# Initialize a dictionary to count vowels
vowel_count = {v: 0 for v in vowels}

# Loop through each character in the string
for char in my_string.lower():  # Convert to lowercase for case-insensitive matching
    if char in vowels:
        vowel_count[char] += 1

# Display the vowel counts
for vowel, count in vowel_count.items():
    print(f"'{vowel}': {count}")

