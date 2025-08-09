import os
class customer(inventory):
    def __init__(self):
        super().__init__()
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.phone = int(input("Enter your phone : "))

        self.buy_product()

        # Only write the header if file does not exist
        file_path = "Customers_Data.csv"
        write_header = not os.path.exists(file_path)

        with open(file_path, "a") as f:
            if write_header:
                f.write("Name,Age,Phone_num,Total_price,Total_profit\n")
            f.write(f"{self.name},{self.age},{self.phone},{self.summ},{self.summ * 0.25}\n")


