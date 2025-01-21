# 3. Write a Python program to find duplicate values from a list and display those.

list = [x for x in input("Enter the list : ").split()]  # Input list
duplicate_values = []  # Store duplicates
exclusive_values = []  # Store unique values
print('List is:', list)

# Traverse the list to identify duplicates
for i in range(len(list)):
    if list[i] not in exclusive_values:
        exclusive_values.append(list[i])
    else:
        duplicate_values.append(list[i])

# Print results
print('List without duplicate values is:', exclusive_values)
print('Duplicate values are:', duplicate_values)
