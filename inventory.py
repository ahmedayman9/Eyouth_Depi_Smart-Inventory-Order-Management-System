import csv
import os

products = [
    {"productID": 1, "productName": "Milk", "price": 2.99, "netprofit": 0.50, "no_of_items": 1},
    {"productID": 2, "productName": "Bread", "price": 1.99, "netprofit": 0.40, "no_of_items": 80},
    {"productID": 3, "productName": "Eggs (12-pack)", "price": 3.49, "netprofit": 0.70, "no_of_items": 60},
    {"productID": 4, "productName": "Apples (1kg)", "price": 2.50, "netprofit": 0.60, "no_of_items": 100},
    {"productID": 5, "productName": "Chicken Breast (1kg)", "price": 7.99, "netprofit": 1.50, "no_of_items": 45},
    {"productID": 6, "productName": "Orange Juice (1L)", "price": 3.25, "netprofit": 0.80, "no_of_items": 70},
    {"productID": 7, "productName": "Toilet Paper (6 rolls)", "price": 4.99, "netprofit": 1.20, "no_of_items": 200},
    {"productID": 8, "productName": "Pasta (500g)", "price": 1.50, "netprofit": 0.35, "no_of_items": 150},
    {"productID": 9, "productName": "Tomato Sauce (jar)", "price": 2.75, "netprofit": 0.55, "no_of_items": 90},
    {"productID": 10, "productName": "Cheese (200g)", "price": 4.50, "netprofit": 0.95, "no_of_items": 50}
]

class Inventory:
    def __init__(self):
        self.products = products

    def additem(self):
        try:
            productID = int(input("Enter product ID: "))
            productName = input("Enter product name: ")
            price = float(input("Enter product price: "))
            netprofit = float(input("Enter net profit: "))
            no_of_items = int(input("Enter number of items: "))
            
            new_product = {
                "productID": productID,
                "productName": productName,
                "price": price,
                "netprofit": netprofit,
                "no_of_items": no_of_items
            }
            self.products.append(new_product)
            print("Product added successfully.")
        except ValueError:
            print("Invalid input. Please enter the correct data types.")

    def deleteproduct(self, productname):
        found = False
        for product in self.products:
            if product['productName'].lower() == productname.lower():
                product['no_of_items'] = 0
                found = True
                print(f"Product '{productname}' marked as out of stock.")
                break
        if not found:
            print("There is no product with this name.")

    def showinventory(self):
        print("Current Inventory:")
        for product in self.products:
            if product['no_of_items'] > 0:
                print(product)

