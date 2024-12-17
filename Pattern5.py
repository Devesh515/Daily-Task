#Pattern 5
'''
*********
 *******
  *****
   ***
    *
'''

# Ask the user for the number of rows
num_of_rows = int(input("Enter the number of rows: "))

# Loop to generate the pattern
for i in range(num_of_rows, 0, -1):
    print(" " * (num_of_rows - i) + "*" * (2 * i - 1))

