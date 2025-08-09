class ProductCls:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print(f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buyProduct(self, amount):
        if amount <= 0:
            print("Invalid amount to buy.")
            return
        if amount > self.quantity:
            print("Not enough stock available.")
            return
        self.quantity -= amount
        print(f"Purchased {amount} of {self.name}. Remaining stock: {self.quantity}")
        return self.price * amount