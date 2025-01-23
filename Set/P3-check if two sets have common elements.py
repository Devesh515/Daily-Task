''' 3. Write a Python program to Check if two sets have any elements in common. If
yes, display the common elements. '''


# Defining two sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Finding the common elements between the two sets
common_elements = set1 & set2  # Intersection of both sets

# Checking if there are any common elements and displaying them
if common_elements:
    print(common_elements)  
else:
    print("No common elements")

