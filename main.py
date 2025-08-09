from balancesheet import balanceSheet
from inventory import inventoryCls
from inventory import ProductCls
from customer import customer
from datetime import datetime



print("Welcome to the Market Management System")
print("=======================================")
print("Enter as user 'user' or as admin 'admin'")

user_type = input("Enter your user type: ")

while user_type not in ["admin", "user"]:
    print("Invalid user type. Please enter 'user' or 'admin'.")
    user_type = input("Enter your user type: ")

inventory = inventoryCls()



if user_type == "admin":
    print("Admin access granted.")
    # Admin functionalities
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. Show Products")
        print("5. Show Total Profit")
        print("6. Show Net Profit")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Product
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = ProductCls(id, name, price, quantity)
            inventory.addProduct(product)
        elif choice == "2":
            # Remove Product
            id = input("Enter product ID to remove: ")
            inventory.removeProduct(id)
        elif choice == "3":
            # Update Product
            id = input("Enter product ID to update: ")
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            quantity = int(input("Enter new product quantity: "))
            updated_product = ProductCls(id, name, price, quantity)
            inventory.updateProduct(id, updated_product)
        elif choice == "4":
            # Show Products
            inventory.showProducts()
        elif choice == "5":
            # Show Total Profit
            inventory.totalProfit()
        elif choice == "6":
            # Show Net Profit
            inventory.netProfit()
        elif choice == "7":
            # Exit
            break
        else:
            print("Invalid choice. Please try again.")
elif user_type == "user":
    print("User access granted.")
    username= input("Enter your username: ")
    userage = int(input("Enter your age: "))
    userPhone = input("Enter your phone number: ")
    userID = int(input("Enter your ID: "))
    customer_instance = customer(username, userage, userPhone, userID)
    print("Customer created successfully.")
    while True:
        print("1.show products")
        print("2.buy product")
        print("3.exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            inventory.showProducts()
        elif choice == "2":
            product_id = input("Enter product ID to buy: ")
            quantity = int(input("Enter quantity to buy: "))

            price = inventory.buyProduct(product_id, quantity)
            if price is not None:
                customer_instance.customerlist.append(price)
                customer_instance.AddCustomer()
                month = datetime.now().strftime("%m")
                balance_sheet = balanceSheet(month[1])
                balance_sheet.add_product(price)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
