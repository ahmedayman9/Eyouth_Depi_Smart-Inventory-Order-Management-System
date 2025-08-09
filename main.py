from Inventory.stock import Stock
from UserCustomer.customer import Customer

def customer_interface(stock):
    print("\n📦 Available Products for Customers:")
    for product in stock.products:
        print(f"ID: {product.product_id} | Name: {product.name} | Price: ${product.price} | Quantity: {product.quantity}")

    # Customer details
    name = input("\nEnter your name: ")
    try:
        age = int(input("Enter your age: "))
        phone = input("Enter your phone number: ")

        customer = Customer(name, age, phone)

        product_id = int(input("\nEnter the ID of the product you want to buy: "))
        amount = int(input("Enter the quantity: "))

        for product in stock.products:
            if product.product_id == product_id:
                if stock.sell_product(product_id, amount):
                    customer.product_id = product.product_id
                    customer.product_name = product.name
                    customer.price = product.price * amount
                    print(f"\n{customer.name} bought {amount}x {product.name}")
                else:
                    print("❌ Purchase failed due to insufficient stock.")
                break
        else:
            print("❌ Product ID not found.")

        customer.display_info()

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

def owner_interface(stock):
    while True:
        print("\n👨‍💼 Owner Menu:")
        print("1. Show all product details")
        print("2. Show total net profit")
        print("3. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock.show_products()
        elif choice == "2":
            stock.show_total_profit()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Try again.")

# ==== Main loop ====
def main():
    stock = Stock()

    while True:
        print("\n📍 Welcome to the Supermarket System")
        print("1. Customer")
        print("2. Owner")
        print("3. Exit")

        choice = input("Choose your role (1, 2, or 3): ")

        if choice == "1":
            customer_interface(stock)
        elif choice == "2":
            owner_interface(stock)
        elif choice == "3":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
