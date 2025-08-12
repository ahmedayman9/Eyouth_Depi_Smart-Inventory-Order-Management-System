import pandas as pd
import csv 
class Inventory: 
    def __init__(self):
        self.filePath = r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\inventory.csv"
        
    def show_inventory(self): 
      data = pd.read_csv(self.filePath,index_col=0) 
      print(data.head())

    def add_product(self, product_ID, product_name, product_price, product_quantity, product_profit, category):
        total_price = float(product_price) * int(product_quantity)
        total_profit = float(product_profit) * int(product_quantity)
        product = {
            "product_ID": product_ID,
            "product_name": product_name,
            "product_price": product_price,
            "product_quantity": product_quantity,
            "product_profit": product_profit,
            "product_category": category,
            "total_price": total_price,
            "total_profit": total_profit
        }

        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        for row in reader:
            if row["product_ID"] == product_ID:
                print("Item already exists")
                return

        reader.append(product)

        with open(self.filePath, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["product_ID", "product_name", "product_price", "product_quantity", "product_profit", "product_category", "total_price" , "total_profit"  ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)

        print("Product added successfully!")

    def edit_product_name(self, product_ID, newName):
        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        found = False
        for row in reader:
            if row["product_ID"] == product_ID:
                row["product_name"] = newName
                found = True
                break

        if found:
            fieldnames = ["product_ID", "product_name", "product_price", "product_quantity",
                        "product_profit", "product_category", "total_price", "total_profit"]

            with open(self.filePath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(reader)

            print("Product updated successfully!")
            return True
        else:
            print("Product not found!")
            return False

    def edit_product_price(self, product_ID, newPrice):

        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        found = False
        for row in reader:
            if row["product_ID"] == product_ID:
                row["product_price"] = str(newPrice)  

                row["total_price"] = str(float(newPrice) * int(row["product_quantity"]))
                row["total_profit"] = str(float(row["product_profit"]) * int(row["product_quantity"]))
                found = True
                break

        if found:
            fieldnames = ["product_ID", "product_name", "product_price", "product_quantity",
                        "product_profit", "product_category", "total_price", "total_profit"]

            with open(self.filePath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(reader)

            print("Product price updated successfully!")
            return True
        else:
            print("Product not found!")
            return False

    def edit_product_quantity(self, product_ID, newQuantity):

        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        found = False
        for row in reader:
            if row["product_ID"] == product_ID:
                row["product_quantity"] = str(newQuantity)  

                row["total_price"] = str(float(newQuantity) * int(row["product_price"]))
                row["total_profit"] = str(float(row["product_profit"]) * float(newQuantity))
                found = True
                break

        if found:
            fieldnames = ["product_ID", "product_name", "product_price", "product_quantity",
                        "product_profit", "product_category", "total_price", "total_profit"]

            with open(self.filePath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(reader)

            print("Product quantity updated successfully!")
            return True
        else:
            print("Product not found!")
            return False

    def edit_product_profit(self, product_ID, newProfit):

        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        found = False
        for row in reader:
            if row["product_ID"] == product_ID:
                row["product_profit"] = str(newProfit)  

                row["total_profit"] = str(float(row["product_quantity"]) * float(newProfit))
                found = True
                break

        if found:
            fieldnames = ["product_ID", "product_name", "product_price", "product_quantity",
                        "product_profit", "product_category", "total_price", "total_profit"]

            with open(self.filePath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(reader)

            print("Product profit updated successfully!")
            return True
        else:
            print("Product not found!")
            return False

    def search_product_by_id(self, product_ID):
        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row["product_ID"] == product_ID:
                    print("Product found:")
                    for key, value in row.items():
                        print(f"{key}: {value}")
                    return row  

        print("Product not found")
        return None

    def delete_product(self, product_ID):
        with open(self.filePath, "r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

            new_data = [row for row in reader if row["product_ID"] != product_ID]

            if len(new_data) == len(reader):
                print("Product not found!")
                return False

            fieldnames = ["product_ID", "product_name", "product_price", "product_quantity",
                        "product_profit", "product_category", "total_price", "total_profit"]

            with open(self.filePath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_data)

            print("Product deleted successfully!")
            return True 
