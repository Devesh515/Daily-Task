# 2. Program to remove duplicate words from a string

string = input('Enter your string : ').strip().lower()  # Take input and convert to lowercase
words = string.split()  # Split the string into words
exclusive_words = set()  # Create a set to store unique words

# Add words to the set if not already present
for word in words:
    exclusive_words.add(word)

# Join and print unique words as a string
print(" ".join(exclusive_words))

