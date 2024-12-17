#Pattern 1
'''
*****
****
***
**
*
'''

# Ask the user for the number of rows
num_of_rows = int(input("Enter the number of rows: "))

# Loop to print the pattern
for row in range(num_of_rows, 0, -1):
    # Print stars for the current row
    print("*" * row)  
