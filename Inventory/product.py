class Product:
    _id_counter = 1 

    def __init__(self, name, price, quantity, unit_profit):
        self.product_id = Product._id_counter
        Product._id_counter += 1

        self.name = name
        self.price = price
        self.quantity = quantity  
        self.unit_profit = unit_profit 
        self.sold_quantity = 0

    def sell(self, amount):
        """Sell"""
        if amount <= 0:
            return False
        if amount > self.quantity:
            print(f"Not enough stock for {self.name}. Available: {self.quantity}")
            return False

        self.quantity -= amount
        self.sold_quantity += amount
        return True

    def total_profit(self):
        """total profit for product."""
        return self.unit_profit * self.sold_quantity
