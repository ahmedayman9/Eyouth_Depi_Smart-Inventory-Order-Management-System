
import csv
import os
from datetime import datetime

from BalanceSheet.sheet import SheetManager
from Inventory.stock import Stock
from UserCustomer.customer import Customer
from BalanceSheet.monthly_sheet import MonthlySheet

# Global variable to track order IDs
current_order_id = 1

def get_next_order_id():
    """Get the next incremental order ID"""
    global current_order_id
    
    # Check if purchases.csv exists and get the last order ID
    if os.path.isfile("purchases.csv"):
        try:
            with open("purchases.csv", mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                last_id = 0
                for row in reader:
                    if row and row[0].isdigit():
                        last_id = int(row[0])
                current_order_id = last_id + 1
        except:
            pass  # If file is empty or corrupted, start from 1
    
    order_id = current_order_id
    current_order_id += 1
    return order_id

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
            # Get order ID and create order
            order_id = get_next_order_id()
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Calculate totals
            total_quantity = sum(p['quantity'] for p in purchases)
            total_price = sum(p['price'] for p in purchases)
            total_profit = sum(p['profit'] for p in purchases)
            
            print(f"\n🧾 {customer.name}'s Final Receipt:")
            print(f"Order ID: {order_id}")
            print(f"Date: {order_date}")
            for p in purchases:
                print(f"- {p['quantity']}x {p['product_name']} = ${p['price']}")

            print(f"Total Items: {total_quantity}")
            print(f"Total: ${total_price}")
            print("Thank you for your purchase!")

            # Save order and items to CSV files
            save_order_to_csv(order_id, customer, order_date, total_quantity, total_price, total_profit)
            save_order_items_to_csv(order_id, purchases)

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
        print("4. View all orders")
        print("5. View specific order")
        print("6. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock.show_products()
        elif choice == "2":
            stock.show_total_profit()
        elif choice == "3":
            sheet.show_monthly_data()
        elif choice == "4":
            view_all_orders()
        elif choice == "5":
            try:
                order_id = int(input("Enter Order ID: "))
                view_order_details(order_id)
            except ValueError:
                print("❌ Invalid Order ID. Please enter a number.")
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice. Try again.")

def save_order_to_csv(order_id, customer, order_date, total_quantity, total_price, total_profit):
    """Save order summary to purchases.csv"""
    file_exists = os.path.isfile("purchases.csv")

    with open("purchases.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Order ID", "Customer Name", "Age", "Phone", 
                "Order Date", "Total Quantity", "Total Amount", "Total Profit"
            ])

        writer.writerow([
            order_id, customer.name, customer.age, customer.phone,
            order_date, total_quantity, total_price, total_profit
        ])

def save_order_items_to_csv(order_id, purchases):
    """Save order items to orders.csv"""
    file_exists = os.path.isfile("orders.csv")

    with open("orders.csv", mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Order ID", "Product ID", "Product Name", 
                "Price Per Unit", "Quantity", "Total Price", "Total Profit"
            ])

        for p in purchases:
            price_per_unit = p['price'] / p['quantity']
            writer.writerow([
                order_id, p["product_id"], p["product_name"],
                price_per_unit, p["quantity"], p["price"], p["profit"]
            ])

def view_all_orders():
    """View all orders from purchases.csv"""
    if not os.path.isfile("purchases.csv"):
        print("No orders found.")
        return

    print(f"\n📋 All Orders:")
    print("-" * 80)
    
    with open("purchases.csv", mode='r') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        
        if not header:
            print("No orders found.")
            return
            
        for row in reader:
            if len(row) >= 8:
                print(f"Order #{row[0]} | Customer: {row[1]} | Date: {row[4]} | "
                      f"Items: {row[5]} | Total: ${row[6]}")

def view_order_details(order_id):
    """View specific order details"""
    # First, get order info from purchases.csv
    order_found = False
    
    if os.path.isfile("purchases.csv"):
        with open("purchases.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            for row in reader:
                if row and row[0] == str(order_id):
                    print(f"\n🧾 Order #{row[0]} Details:")
                    print(f"Customer: {row[1]} (Age: {row[2]}, Phone: {row[3]})")
                    print(f"Date: {row[4]}")
                    print(f"Total Items: {row[5]}")
                    print(f"Total Amount: ${row[6]}")
                    print(f"Total Profit: ${row[7]}")
                    order_found = True
                    break
    
    if not order_found:
        print(f"Order #{order_id} not found.")
        return
    
    # Then, get order items from orders.csv
    if os.path.isfile("orders.csv"):
        print(f"\nOrder Items:")
        with open("orders.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            for row in reader:
                if row and row[0] == str(order_id):
                    print(f"- {row[4]}x {row[2]} @ ${row[3]} = ${row[5]}")

def save_multiple_purchases_to_csv(customer, purchase_list, filename="purchases.csv"):
    # This function is kept for backward compatibility but won't be used
    pass


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
            owner_interface(stock,sheet)
        elif choice == "3":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
