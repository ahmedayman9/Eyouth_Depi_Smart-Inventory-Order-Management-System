class ProductCls:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print(f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


class inventoryCls:
    def __init__(self, products):
        self.products = products
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
            if existing_product.id == product.id:
                print(f"Product with ID {product.id} already exists.")
                return
        self.products.append(product)
        with open("inventory.csv", "a") as f:
            f.write(f"{product.id},{product.name},{product.price},{product.price * 0.25},{product.quantity}\n")

    def removeProduct(self, productId):
        for product in self.products:
            if product.id == productId:
                self.products.remove(product)
                break
        else:
            print(f"Product with ID {productId} not found.")
            return
        with open("inventory.csv", "a") as f:
            for line in f.readlines()[1:]:
                if line.split(",")[0] == str(productId):
                    f.remove(line)
                    break


    def updateProduct(self, productId, updatedProduct):
        for product in self.products:
            if product.id == productId:
                product.name = updatedProduct.name
                product.price = updatedProduct.price
                product.quantity = updatedProduct.quantity
                break
        else:
            print(f"Product with ID {productId} not found.")
            return
        with open("inventory.csv", "a") as f:
            for line in f.readlines()[1:]:
                if line.split(",")[0] == str(productId):
                    f.remove(line)
                    break
            f.write(f"{updatedProduct.id},{updatedProduct.name},{updatedProduct.price},{updatedProduct.price * 0.25},{updatedProduct.quantity}\n")