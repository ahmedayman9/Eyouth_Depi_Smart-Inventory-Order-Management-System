class Product:
    product_id = 1
    def __init__(self, name, price, quantity, net_profit):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.net_profit = net_profit
        self.product_id = Product.product_id
        Product.product_id += 1

        self.sold_quantity = 0

class Stock:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        product.sold_quantity += 1
        product.quantity -= 1

    def show_products(self):
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Net Profit: {product.net_profit}")

    def show_total_profit(self):
        total_profit = sum((product.net_profit * product.sold_quantity) for product in self.products)
        print(f"Total Net Profit: {total_profit}")
