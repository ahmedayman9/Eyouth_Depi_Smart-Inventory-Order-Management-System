import csv
from inventory import Inventory

class Customer:
    def __init__(self, name, age, phone_number, customer_id , month):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.customer_id = customer_id
        self.inventory = Inventory()
        self.month = month

    def sell_product(self, product_name, filename="customer.csv"):
        self.inventory.deleteproduct(product_name)
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
                      self.customer_id, self.name, self.age,  self.phone_number,
                    product_name , self.month
                ])
            print("Sale saved successfully.")
        except IOError as e:
            print(f"An error occurred while saving to CSV: {e}")
