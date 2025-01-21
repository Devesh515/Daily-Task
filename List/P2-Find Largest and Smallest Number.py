# 2. Write a Python program to get the largest and smallest number from a list without built-in functions

list = [int(x) for x in input("Enter the list : ").split()]  # Input list of integers
print('List is:', list)
temp_large = float('-inf')  # Initialize largest to negative infinity
temp_small = float('inf')  # Initialize smallest to positive infinity

# Traverse the list to find largest and smallest
for i in range(len(list)):
    if list[i] > temp_large:
        temp_large = list[i]
    elif list[i] < temp_small:
        temp_small = list[i]

# Print results
print('Largest number in the list is:', temp_large, '\nSmallest number in the list is:', temp_small)

