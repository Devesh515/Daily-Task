''' 3.create a program to accept choice from user and perform the operation according
	a. Try except
	b. try multiple except
	c. try except else
	d. finally
	e. try single except
	f. raising exception '''
	
def menu():
    print("Choose an operation:")
    print("1. Try Except")
    print("2. Try Multiple Except")
    print("3. Try Except Else")
    print("4. Finally")
    print("5. Try Single Except")
    print("6. Raising Exception")
    choice = input("Enter your choice (1-6): ")
    return choice

def try_except():
    try:
        number = int(input("Enter a number: "))
        print("Number entered is:", number)
    except ValueError:
        print("Error: Not a valid number!")

def try_multiple_except():
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print("Result is:", result)
    except ValueError:
        print("Error: Not a valid number!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

def try_except_else():
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print("Result is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print("Operation successful!")

def finally_example():
    try:
        number = int(input("Enter a number: "))
        print("Number entered:", number)
    finally:
        print("This block always runs!")

def try_single_except():
    try:
        number = int(input("Enter a number: "))
        print("Number entered is:", number)
    except ValueError:
        print("Error: Invalid input!")

def raising_exception():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            raise ValueError("Number cannot be negative!")
        print("Number is valid:", number)
    except ValueError as e:
        print(f"Error: {e}")

def main():
    choice = menu()
    
    if choice == '1':
        try_except()
    elif choice == '2':
        try_multiple_except()
    elif choice == '3':
        try_except_else()
    elif choice == '4':
        finally_example()
    elif choice == '5':
        try_single_except()
    elif choice == '6':
        raising_exception()
    else:
        print("Invalid choice!")

# Run the program
main()


