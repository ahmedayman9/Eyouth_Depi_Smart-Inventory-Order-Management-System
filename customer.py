import csv
from Inventory import Inventory

class Customer:
    def __init__(self, name, age, phone_number, customer_id):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.customer_id = customer_id
        self.inventory = Inventory()

    def sell_product(self, product_name, filename="customer.csv"):
        self.inventory.buy(product_name)
        price = self.inventory.price_of_item(product_name)
        profit = self.inventory.profit_of_item(product_name)

        if price is None or profit is None:
            print(f"Could not find product '{product_name}' for sale.")
            return

        try:
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)

                file.seek(0)
                if file.tell() == 0:
                    writer.writerow([
                        "Name", "Age", "PhoneNumber", "CustomerID",
                        "Product", "Price", "Profit"
                    ])

                writer.writerow([
                    self.name, self.age, self.phone_number, self.customer_id,
                    product_name, price, profit
                ])
            print("Sale saved successfully.")
        except IOError as e:
            print(f"An error occurred while saving to CSV: {e}")
