class Customer:
    def __init__(self, name, age, phone, product_id=None, product_name=None, price=0, profit=0):
        self.name = name
        self.age = age
        self.phone = phone
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.profit = profit

    def display_info(self):
        print("\nCustomer Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        if self.product_id is not None:
            print("Purchased Product:")
            print(f" - ID: {self.product_id}")
            print(f" - Name: {self.product_name}")
            print(f" - Total Price: ${self.price}")
        else:
            print("No product purchased yet.")
