# 5. Program to traverse a list in reverse order and print elements with their original index

list = [x for x in input("Enter the list : ").split()]  # Input list
print('List is:', list)

# Traverse list in reverse
for i in range(len(list) - 1, -1, -1):
    print(f'Original index: {i}, Element: {list[i]}')
