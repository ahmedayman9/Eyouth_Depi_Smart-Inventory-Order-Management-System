import os
import csv

class Inventory:
    # def __init__(self):
    #     self.inventory = {}

    def show_products(self,file_name=r"C:\Users\DEBI\Desktop\shop_system\Eyouth_Depi_Smart-Inventory-Order-Management-System\data\supermarket_inventory.csv"):
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            print("\nproducts available in inventory are:")
            next(reader)
            for row in reader:
                print(f"product id:{row[0]}, product:{row[1]}, price:{row[2]},  stock:{row[3]} ,categoty:{row[4]}")

    def add_item(self, file_name=r"C:\Users\DEBI\Desktop\shop_system\Eyouth_Depi_Smart-Inventory-Order-Management-System\data\supermarket_inventory.csv"):
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            last_id=0
            for row in reader:
                last_id=int(row[0])

            new_id=last_id+1
            product_name=input("enter product name:")
            product_price=input("enter product price:")
            product_stock=input("enter product stock:")
            product_category=input("enter product category:")

        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, product_name, product_price, product_stock, product_category])

    # def remove_item(self, item_name, quantity):
    #     if item_name in self.inventory:


inv=Inventory()
# inv.show_products()
inv.add_item()