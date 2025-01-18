''' 3. Using max() and min() functions display the maximum and minimum of 5 random
numbers. '''

import random  # Import the random module

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Find the maximum and minimum numbers
maximum = max(numbers)
minimum = min(numbers)

# Show the random numbers, maximum, and minimum
print("The random numbers are:", numbers)
print("The maximum number is:", maximum)
print("The minimum number is:", minimum)

