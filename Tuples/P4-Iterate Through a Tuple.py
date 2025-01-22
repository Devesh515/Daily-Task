#4.Write a python program and iterate the given tuples

# Tuples for employees
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Creating a list of employee tuples
employees = [employee1, employee2, employee3]

# Iterating through the list of tuples
for employee in employees:
    # Printing each element in the tuple
    print("Name:", employee[0])
    print("Employee ID:", employee[1])
    print("Department:", employee[2])
    print("Salary:", employee[3])
    print()  
