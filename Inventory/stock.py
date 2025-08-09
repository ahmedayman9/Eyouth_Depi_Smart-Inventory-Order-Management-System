from Inventory.product import Product
from BalanceSheet.sheet import SheetManager
from BalanceSheet.monthly_sheet import MonthlySheet
from datetime import datetime

class Stock:
    def __init__(self, monthly_sheet):
        self.products = []
        self.monthly_sheet = monthly_sheet
        self._load_initial_products()

    def _load_initial_products(self):
        """stock"""
        self.products.append(Product("Laptop", 1000, 10, 150))
        self.products.append(Product("Smartphone", 600, 20, 80))
        self.products.append(Product("Headphones", 80, 50, 20))
        self.products.append(Product("Monitor", 200, 15, 40))

    def show_products(self):
        print("\nInventory:")
        for product in self.products:
            print(
                f"ID: {product.product_id} | Name: {product.name} | Price: ${product.price} | "
                f"Quantity: {product.quantity} | Unit Profit: ${product.unit_profit} | "
                f"Sold: {product.sold_quantity}"
            )

    def show_total_profit(self):
        total_profit = sum(p.total_profit() for p in self.products)
        print(f"\nNet Profit: {total_profit}")

    def sell_product(self, product_id, amount):
        """Sell a product by its ID."""
        current_month = datetime.now().month  # Get current month (1-12)
        
        for product in self.products:
            if product.product_id == product_id:
                self.monthly_sheet.add_data(
                    month=current_month,
                    gross_profit=product.price * amount,
                    net_profit=product.unit_profit * amount
                )
                return product.sell(amount)
        print("Product not found.")
        return False
