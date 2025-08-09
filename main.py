from inventory import Inventory
from customer import Customer
from balanceSheet import balanceSheet

def main():
    role = input("Are you an Admin or User? (Enter 'admin' or 'user'): ").lower()

    if role == "admin":
        print("Welcome Admin! You can manage the inventory and view reports.")
        admin_operations()
    elif role == "user":
        print("Welcome User! You can buy products.")
        user_operations()
    else:
        print("Invalid role entered. Please restart the program and enter 'admin' or 'user'.")
        return

def admin_operations():
    inventory = Inventory()
    balance = balanceSheet()

    while True:
        print("\nAdmin Operations: ")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. View Monthly Report")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")
        
        if choice == '1':
            inventory.showinventory()
        elif choice == '2':
            inventory.additem()
        elif choice == '3':
            product_name = input("Enter the product name to remove: ")
            inventory.deleteproduct(product_name)
        elif choice == '4':
            month = int(input("Enter the month number (1-12): "))
            report = balance.show_monthly_record(month)
        elif choice == '5':
            print("Exiting Admin operations.")
            break
        else:
            print("Invalid choice! Try again.")

def user_operations():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phone_number = input("Enter your phone number: ")
    customer_id = int(input("Enter your customer ID: "))
    month = int(input("Enter the month number (1-12): "))

    customer = Customer(name, age, phone_number, customer_id, month)

    while True:
        print("\nUser Operations:")
        print("1. Buy a Product")
        print("2. Exit")
        
        choice = input("Choose an operation (1-2): ")

        if choice == '1':
            product_name = input("Enter the product name you want to buy: ")
            customer.sell_product(product_name)
        elif choice == '2':
            print("Exiting User operations.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
