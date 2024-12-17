'''
1
10
101
1010
10101
'''

# Ask the user for the number of rows
num_of_rows = int(input("Enter the number of rows: "))

# Loop through each row to generate the pattern
for i in range(1, num_of_rows + 1):
    # Initialize an empty string for the current row
    current_row = ""
    
    # Loop through each position in the current row
    for j in range(i):
        # Add '1' or '0' depending on the position
        if j % 2 == 0:
            current_row += "1"
        else:
            current_row += "0"
    
    # Print the generated row
    print(current_row)
