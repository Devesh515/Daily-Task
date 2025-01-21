# 4. Program to split a list into two parts with a specified length for the first part

list = [x for x in input("Enter the list : ").split()]  # Input list
n = int(input('Enter the length of the first part of the list: '))  # Length of the first part
print('List is:', list, '\nLength of list is:', len(list))
print('First part of the list is:', list[:n])  # First part
print('Second part of the list is:', list[n:])  # Second part

