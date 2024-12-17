#Pattern 2
'''
----*
---**
--***
-****
*****
'''

# Ask the user for the number of rows
num_of_rows = int(input("Enter the number of rows: "))

# Loop to generate the pattern
for i in range(1, num_of_rows + 1):
    print(" " * (num_of_rows - i) + "*" * i)


