# main.py
from signup import Signup
import stdiomask
from login import check_type
from stockManager import Stock_manager
from Cashier import cashier



def sign_up_flow():
    print("\n--- Sign Up ---")
    user_name = input("Enter a new user name: ")
    password = stdiomask.getpass(prompt="Enter password: ", mask="*")
    confirm_password = stdiomask.getpass(prompt="Confirm password: ", mask="*")

    if password != confirm_password:
        print("Passwords do not match! Please try again.")
        return

    name = input("Enter your full name: ")
    age = input("Enter your age: ")

    user_type = input("Enter user type (stockManager/cashier): ").strip()
    if user_type not in ["stockManager", "cashier"]:
        print("Invalid user type! Please enter 'stockManager' or 'cashier'.")
        return

    salary = input("Enter salary: ")

    new_user = Signup(user_name, password, name, age, user_type, salary)

    if new_user.check_data():
        new_user.save_user()
    else:
        print("Sign up failed. Try a different user name.")

def stock_manager_menu(manager):
    while True:
        print("\n--- Stock Manager Menu ---")
        print("1- Show Inventory")
        print("2- Add Product")
        print("3- Edit Product Name")
        print("4- Edit Product Price")
        print("5- Edit Product Quantity")
        print("6- Edit Product Profit")
        print("7- Search Product by ID")
        print("8- Delete Product")
        print("9- View Balance Sheet Report")
        print("0- Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            manager.show_inventory()
        elif choice == "2":
            manager.add_product()
        elif choice == "3":
            manager.edit_product_name()
        elif choice == "4":
            manager.edit_product_price()
        elif choice == "5":
            manager.edit_product_quantity()
        elif choice == "6":
            manager.edit_product_profit()
        elif choice == "7":
            manager.search_product_by_id()
        elif choice == "8":
            manager.delete_product()
        elif choice == "9":
            manager.balance()
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice, try again.")

def cashier_menu(cashier_user):
    while True:
        print("\n--- Cashier Menu ---")
        print("1- Make a Sale")
        print("0- Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            cashier_user.sale()
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice, try again.")

def main():
    while True:
        print("\n===============================")
        print(" Welcome to our Market System :) ")
        print("===============================\n")

        print("1- Login")
        print("2- Sign Up")
        print("3- Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_name = input("Enter your user name: ")
            password = stdiomask.getpass(prompt="Enter your password: ", mask="*")
            user_type = check_type(user_name, password)

            if user_type == "stockManager":
                print(f"Welcome Stock Manager {user_name}!")
                manager = Stock_manager()
                stock_manager_menu(manager)

            elif user_type == "cashier":
                print(f"Welcome Cashier {user_name}!")
                cashier_user = cashier(user_name)
                cashier_menu(cashier_user)

            elif user_type:
                print(f"Welcome {user_type}!")
            else:
                print("Login failed. Please try again.")

        elif choice == "2":
            sign_up_flow()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
