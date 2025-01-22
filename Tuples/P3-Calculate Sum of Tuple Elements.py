#3. Write a Python program to calculate the sum of the numbers in a given tuple.


# A list of tuples with numbers
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Calculating the sum of all numbers in the tuples
total_sum = sum(sum(t) for t in tuples_list)

# Print the result
print(total_sum)  

