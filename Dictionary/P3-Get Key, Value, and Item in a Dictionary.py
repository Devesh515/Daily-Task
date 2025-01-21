# 3.Write a Python program to get the key, value and item in a dictionary.

# Create an empty dictionary
employee_details = {}

# Get employee details from the user
employee_details["name"] = input("Enter employee name: ")
employee_details["no"] = input("Enter employee number: ")
employee_details["ID"] = input("Enter employee ID: ")
employee_details["dep"] = input("Enter employee department: ")
employee_details["des"] = input("Enter employee designation: ")
employee_details["DOJ"] = input("Enter employee date of joining (DD/MM/YYYY): ")
employee_details["DOB"] = input("Enter employee date of birth (DD/MM/YYYY): ")
employee_details["salary"] = float(input("Enter employee salary: "))

# Print all details
print("\nEmployee Details:")
for key, value in employee_details.items():
    print(key + ":", value)  # Show key and value


