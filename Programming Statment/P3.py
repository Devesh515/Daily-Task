#3.Write a Program to Convert Kilometers to Miles

# Take input in kilometers from the user
kilometers = input("Enter distance in kilometers: ")

# Conversion factor from kilometers to miles
conversion_factor = 0.621371

# Convert kilometers to miles
miles = int(kilometers) * conversion_factor

# Print the result
print(kilometers + " kilometers is equal to " + str(miles) + " miles.")
