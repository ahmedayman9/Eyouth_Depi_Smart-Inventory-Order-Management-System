import csv 
import datetime
from inventory import Inventory
from balanceSheet import BalanceSheet
class Stock_manager(): 

    def __init__(self, Type = "stockManager"): 
        
        self.type = Type  
        self.filePath = r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\inventory.csv"
        self.inventory = Inventory()
        self.balancesheet = BalanceSheet()

    def show_inventory(self): 
        self.inventory.show_inventory() 

    def add_product(self):
        product_ID = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        product_price = input("Enter Product Price: ")
        product_quantity = input("Enter Product Quantity: ")
        product_profit = input("Enter Product Profit: ") 
        product_category = input("Enter Product Category: ")

        self.inventory.add_product( product_ID, product_name, product_price, product_quantity, product_profit, product_category)
        
    def edit_product_name(self):
        
        product_ID = input("Enter Product ID: ")
        newName = input("Enter a new name: ")
        self.inventory.edit_product_name(product_ID , newName)

    def edit_product_price(self):
        product_ID = input("Enter Product ID: ")
        newPrice = input("Enter new price: ")
        self.inventory.edit_product_price(product_ID , newPrice)

    def edit_product_quantity(self):
        product_ID = input("Enter Product ID: ")
        newQuantity = input("Enter a new Quantity: ")
        self.inventory.edit_product_quantity(product_ID , newQuantity)

    def edit_product_profit(self):
        product_ID = input("Enter Product ID: ")
        newProfit = input("Enter a new Profit: ")
        self.inventory.edit_product_profit(product_ID , newProfit)

    def search_product_by_id(self):
        product_ID = input("Enter Product ID: ")
        self.inventory.search_product_by_id(product_ID)

    def delete_product(self):
        product_ID = input("Enter Product ID: ")
        self.inventory.delete_product(product_ID)

    def balance(self):
        print("1 - See this month's sales report")
        print("2 - See report for another month")
        try:
            choice = int(input("Enter your choice (1 or 2): "))
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")
            return

        if choice == 1:
            current_month = datetime.datetime.now().month
            self.balancesheet.monthly_report(current_month)
        elif choice == 2:
            try:
                month = int(input("Enter month number (1-12): "))
                if 1 <= month <= 12:
                    self.balancesheet.monthly_report(month)
                else:
                    print("Invalid month number! Please enter a number between 1 and 12.")
            except ValueError:
                print("Invalid input! Please enter a valid month number.")
        else:
            print("Wrong choice!")