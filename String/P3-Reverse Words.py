#3. Write a Python program to reverse words in a string String = “Deeptech Python Training”

# Given string
my_string = "Deeptech Python Training"

# Split the string into words
words = my_string.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words back into a string
reversed_string = " ".join(reversed_words)

# Print the reversed string
print(reversed_string)

