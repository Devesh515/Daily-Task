# 1. Write a Python program to sum all the items in a list.

list = [int(x) for x in input("Enter the list : ").split()]  # Input list of integers
print('List is:', list, '\nSum of all the items in the list is:', sum(list))  # Print sum of list items

