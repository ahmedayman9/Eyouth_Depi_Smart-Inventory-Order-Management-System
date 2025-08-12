import csv
import datetime
from inventory import Inventory

class marketsells:
    def __init__(self, cashier_name):
        self.salesPath = r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\sales.csv"
        self.inventoryPath = r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\inventory.csv"
        self.inventory = Inventory()
        self.cashier_name = cashier_name

    def sale_product(self):
        with open(self.inventoryPath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        print("In stock products:")
        for row in reader:
            if int(row["product_quantity"]) != 0:
                print(f"Product ID: {row['product_ID']}, Product Name: {row['product_name']}")

        product_id = input("Enter product id: ")
        user_quantity = int(input("Enter quantity: "))

        product = None
        for row in reader:
            if row["product_ID"] == product_id:
                product = row
                break

        if product is None:
            print("Product not found.")
            return

        available_quantity = int(product["product_quantity"])
        if user_quantity > available_quantity:
            print(f"Sorry, we only have {available_quantity} items available.")
            return

        new_quantity = available_quantity - user_quantity
        if not self.inventory.edit_product_quantity(product_id, new_quantity):
            print("Error updating inventory quantity.")
            return

        price = float(product["product_price"])
        profit = float(product["product_profit"])
        total_price = user_quantity * price
        total_profit = user_quantity * profit

        sale_ID = f"{product_id}-{user_quantity}-{self.cashier_name}"
        sale_record = {
            "sale_ID": sale_ID,
            "product_ID": product_id,
            "product_name": product["product_name"],
            "quantity_sold": user_quantity,
            "total_price": total_price,
            "total_profit": total_profit,
            "sale_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "NameCashier": self.cashier_name,
            "Month": datetime.datetime.now().month
        }

        with open(self.salesPath, "a", newline="", encoding="utf-8") as f:
            fieldnames = ["sale_ID", "product_ID", "product_name", "quantity_sold", "total_price",
                          "total_profit", "sale_date", "NameCashier", "Month"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)


            try:
                f.seek(0, 2) 
                if f.tell() == 0:  
                    writer.writeheader()
            except:
                writer.writeheader()

            # writer.writerow("\n")    
            writer.writerow(sale_record)

        print("Sale added successfully!")
