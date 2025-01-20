#1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”

# Given sentence
my_string = "To change the overall look of your document. To change the look available in the gallery"

# Convert to lowercase
my_string = my_string.lower()

# Remove punctuation
import string as st
my_string = my_string.translate(str.maketrans("", "", st.punctuation))

# Split into words
words = my_string.split()

# Count occurrences of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print word counts
for word, count in word_count.items():
    print(f"'{word}': {count}")

