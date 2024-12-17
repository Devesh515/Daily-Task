'''
    1
   01
  101
 0101
10101
'''

# Ask the user for the number of rows
num_of_rows = int(input("Enter the number of rows: "))

# Loop to generate the pattern
for i in range(1, num_of_rows + 1):
    # Create spaces before the stars
    spaces = " " * (num_of_rows - i)
    
    # Create the alternating 1's and 0's for the current row
    current_row = ""
    for j in range(i):
        if j % 2 == 0:
            current_row += "1"
        else:
            current_row += "0"
    
    # Print the spaces followed by the current row pattern
    print(spaces + current_row)
