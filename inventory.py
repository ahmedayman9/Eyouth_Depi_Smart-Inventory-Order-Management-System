from product import ProductCls

class inventoryCls:
    def __init__(self):
        self.products = []
        self.readFromFile()


    def readFromFile(self):
        with open("inventory.csv", "r") as f:
            for line in f.readlines()[1:]:
                id, name, price, profit, quantity = line.strip().split(",")
                self.products.append(ProductCls(int(id), name, float(price), int(quantity)))

    def showProducts(self):
        print("Products in Inventory:")
        print("======================")
        for product in self.products:
            product.showProduct()
            print("--------------------------------------------------")

    def totalProfit(self):
        totalProfit = 0
        for product in self.products:
            totalProfit += product.price * product.quantity
        print(f"Total Profit: {totalProfit}")

    def netProfit(self):
        netProfit = 0
        for product in self.products:
            netProfit += product.price * product.quantity * 0.25
        print(f"Net Profit: {netProfit}")

    def addProduct(self, product):
        for existing_product in self.products:
            if str(existing_product.id) == str(product.id):
                print(f"Product with ID {product.id} already exists.")
                return
        self.products.append(product)
        with open("inventory.csv", "a") as f:
            f.write(f"{product.id},{product.name},{product.price},{product.price * 0.25},{product.quantity}\n")
            print(f"Product {product.name} added successfully.")

    def removeProduct(self, productId):
        for product in self.products:
            if str(product.id) == str(productId):
                self.products.remove(product)
                break
        else:
            print(f"Product with ID {productId} not found.")
            return
        with open("inventory.csv", "r") as f:
            lines = f.readlines()
        with open("inventory.csv", "a") as f:
            for line in lines:
                if line.split(",")[0] == str(productId):
                    # remove row
                    lines.remove(line)
                    break
        with open("inventory.csv", "w") as f:
            f.writelines(lines)
        print(f"Product with ID {productId} removed successfully.")

    def updateProduct(self, productId, updatedProduct):
        for product in self.products:
            if str(product.id) == str(productId):
                product.name = updatedProduct.name
                product.price = updatedProduct.price
                product.quantity = updatedProduct.quantity
                break
        else:
            print(f"Product with ID {productId} not found.")
            return
        with open("inventory.csv", "r") as f:
            lines = f.readlines()

        with open("inventory.csv", "w") as f:
            for line in lines:
                if line.split(",")[0] == str(productId):
                    lines.remove(line)
                    break
            f.writelines(lines)
            f.write(f"{updatedProduct.id},{updatedProduct.name},{updatedProduct.price},{updatedProduct.price * 0.25},{updatedProduct.quantity}\n")
        print(f"Product with ID {productId} updated successfully.")

    def buyProduct(self, productId, quan):
        for product in self.products:
            if str(product.id) == str(productId):
                price = product.buyProduct(quan)
                if price is not None:
                    print(f"Total cost for {quan} of {product.name}: {price}")
                    
                    # product.quantity -= int(quan/2)
                    self.updateProduct(productId, product)
                    return price
                break
        else:
            print(f"Product with ID {productId} not found.")
