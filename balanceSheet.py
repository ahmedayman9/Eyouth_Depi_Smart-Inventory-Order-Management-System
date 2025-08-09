import csv
from inventory import Inventory

class balanceSheet:
    def __init__(self):
        self.expense_monthly = 0  
        self.net_monthly = 0  
        self.inventory = Inventory()  

    def show_monthly_record(self, monthUser):
        with open("customer.csv", mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_name = row["Name"]
                product_name = row["Product"]
                month = int(row["Month"])
                if  month == monthUser: 
                    product_price = self.inventory.price_of_item(product_name)
                    product_profit = self.inventory.profit_of_item(product_name)

                    quantity = 1

                    self.expense_monthly += product_price
                    self.net_monthly += product_profit 

        print(f"Total price : {self.expense_monthly}")
        print(f"Total price : {self.net_monthly}")

    