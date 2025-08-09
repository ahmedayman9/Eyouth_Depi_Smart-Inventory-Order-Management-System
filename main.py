import csv
import os

from BalanceSheet.sheet import SheetManager
from Inventory.stock import Stock
from UserCustomer.customer import Customer
from BalanceSheet.monthly_sheet import MonthlySheet

def customer_interface(stock):
    print("\n📦 Available Products for Customers:")
    for product in stock.products:
        print(f"ID: {product.product_id} | Name: {product.name} | Price: ${product.price} | Quantity: {product.quantity}")

    # Customer info (entered once)
    name = input("\nEnter your name: ")
    try:
        age = int(input("Enter your age: "))
        phone = input("Enter your phone number: ")
        customer = Customer(name, age, phone)

        purchases = []  # List to hold multiple purchases

        while True:
            print("\n🛒 New Item")
            product_id = int(input("Enter the product ID to buy (or 0 to finish): "))
            if product_id == 0:
                break

            amount = int(input("Enter the quantity: "))

            for product in stock.products:
                if product.product_id == product_id:
                    if stock.sell_product(product_id, amount):
                        # Store purchase details temporarily
                        purchases.append({
                            "product_id": product.product_id,
                            "product_name": product.name,
                            "price": product.price * amount,
                            "profit": product.unit_profit * amount,
                            "quantity": amount
                        })
                        print(f"✅ Added {amount}x {product.name} to your cart.")
                    else:
                        print("❌ Not enough stock.")
                    break
            else:
                print("❌ Product not found.")

        if purchases:
            print(f"\n🧾 {customer.name}'s Final Receipt:")
            total_price = 0
            total_profit = 0
            for p in purchases:
                print(f"- {p['quantity']}x {p['product_name']} = ${p['price']}")
                total_price += p['price']
                total_profit += p['profit']

            print(f"Total: ${total_price}")
            print("Thank you for your purchase!")

            # Save all purchases to CSV
            save_multiple_purchases_to_csv(customer, purchases)

        else:
            print("🛑 No purchases made.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

def owner_interface(stock, sheet):
    while True:
        print("\n👨‍💼 Owner Menu:")
        print("1. Show all product details")
        print("2. Show total net profit")
        print("3. Show monthly report")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock.show_products()
        elif choice == "2":
            stock.show_total_profit()
        elif choice == "3":
            stock.monthly_sheet.show_monthly_data()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice. Try again.")

def save_multiple_purchases_to_csv(customer, purchase_list, filename="purchases.csv"):
    import csv
    import os
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Customer Name", "Age", "Phone",
                "Product ID", "Product Name",
                "Quantity", "Total Price", "Profit"
            ])

        for p in purchase_list:
            writer.writerow([
                customer.name,
                customer.age,
                customer.phone,
                p["product_id"],
                p["product_name"],
                p["quantity"],
                p["price"],
                p["profit"]
            ])


# ==== Main loop ====
def main():
    sheet = SheetManager()
    stock = Stock(sheet.monthly_sheet)

    while True:
        print("\n📍 Welcome to the Supermarket System")
        print("1. Customer")
        print("2. Owner")
        print("3. Exit")

        choice = input("Choose your role (1, 2, or 3): ")

        if choice == "1":
            customer_interface(stock)
        elif choice == "2":
            owner_interface(stock, sheet)
        elif choice == "3":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
