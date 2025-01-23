'''2. Write a Python program to Return a set of elements present in Set A or B, but
not both.'''

# Defining two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Getting elements present in either set1 or set2, but not in both
unique_elements = set1 ^ set2  # Symmetric difference

# Printing the result
print(unique_elements)  

