#Create an application for online food ordering system

print("Welcome to My Hotel!")

total_bill = 0
order_summary = []

while True:
    print("\nMenu:")
    print("1: Starters\n   - Fries (30 Rs.)")
    print("2: Main Course\n   - Rice (50 Rs.)")
    print("3: Desserts\n   - Cake (20 Rs.)")
    print("4: Drinks\n   - Water (10 Rs.)")
    print("5: Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            print("\nYou chose Starters:")
            print("1: Fries (30 Rs.)")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                total_bill += 30
                order_summary.append("Fries (30 Rs.)")
                print("Fries added to your order for 30 Rs.")
            else:
                print("Invalid selection, try again.")

        elif choice == 2:
            print("\nYou chose Main Course:")
            print("1: Rice (50 Rs.)")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                total_bill += 50
                order_summary.append("Rice (50 Rs.)")
                print("Rice added to your order for 50 Rs.")
            else:
                print("Invalid selection, try again.")

        elif choice == 3:
            print("\nYou chose Desserts:")
            print("1: Cake (20 Rs.)")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                total_bill += 20
                order_summary.append("Cake (20 Rs.)")
                print("Cake added to your order for 20 Rs.")
            else:
                print("Invalid selection, try again.")

        elif choice == 4:
            print("\nYou chose Drinks:")
            print("1: Water (10 Rs.)")
            sub_choice = int(input("Enter your choice: "))
            if sub_choice == 1:
                total_bill += 10
                order_summary.append("Water (10 Rs.)")
                print("Water added to your order for 10 Rs.")
            else:
                print("Invalid selection, try again.")

        elif choice == 5:
            print("\nThank you for visiting!")
            print("Your order summary:")
            for item in order_summary:
                print("-", item)
            print("Total bill:", total_bill, "Rs.")
            break

        else:
            print("Invalid option. Please select a number between 1 and 5.")

    except ValueError:
        print("Please enter a valid number.")
