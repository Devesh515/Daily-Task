''' 4. Write a Python program to Remove items from set1 that are not common to
both set1 and set2. '''

# Defining two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Removing items from set1 that are not in set2
set1 &= set2  # This keeps only the common elements in set1

# Printing the updated set1
print(set1)  
