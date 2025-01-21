# 2.Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary :

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries using the update() method
new_dict = {}
new_dict.update(dic1)  # Add all items from dic1
new_dict.update(dic2)  # Add all items from dic2
new_dict.update(dic3)  # Add all items from dic3

# Print the resulting dictionary
print("Concatenated Dictionary:", new_dict)

