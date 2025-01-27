import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print("\n--- File Content ---")
            print(file.read())
            print("--- End of File ---")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file(file_path):
    try:
        with open(file_path, 'a') as file:  # Append mode
            data = input("Enter the data to write to the file: ")
            file.write(data + '\n')
            print("Data written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_file(file_path):
    try:
        with open(file_path, 'r') as file:
            search_term = input("Enter the term to search for: ")
            lines = file.readlines()
            found = False
            for i, line in enumerate(lines, 1):
                if search_term in line:
                    print(f"Found '{search_term}' on line {i}: {line.strip()}")
                    found = True
            if not found:
                print(f"'{search_term}' not found in the file.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        file_path = input("\nEnter the file path (or type 'done' to stop): ").strip('"')
        
        # Handle "done" input
        if file_path.lower() == 'done':
            continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
            if continue_choice == 'yes':
                continue
            elif continue_choice == 'no':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid input. Exiting program.")
                break

        # Check if the file path is valid
        if not os.path.exists(file_path):
            print("Error: File does not exist. Please provide a valid file path.")
            continue

        # Display options to the user
        print("\nChoose an option:")
        print("1. Read from the file")
        print("2. Write to the file")
        print("3. Search in the file")
        
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice == 1:
                read_file(file_path)
            elif choice == 2:
                write_file(file_path)
            elif choice == 3:
                search_file(file_path)
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        print()

main()
