from modules.inventory import Inventory
from modules.balance import Balance
from modules.cli_colors import COLORS
from datetime import datetime
import csv
import os


# make file path works on all platforms (linux, windows, macos)
curr_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(curr_dir)
customers_file = os.path.join(project_root, "data", "customers.csv")
transactions_file = os.path.join(project_root, "data", "transactions_log.csv")


line_sep = str(f"####" + f"{COLORS.GREEN}-{COLORS.RESET}" * 40 + "####")

with open(customers_file, "r", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)
    row_count = len(rows)


class Customer:
    def __init__(self):
        self.curr_id = None
        self.role = None

    def login(self) -> int:
        print(f"{COLORS.GREEN}-0-0-0-0 login -0-0-0-{COLORS.RESET}")
        id = int(input("Enter your ID: "))
        password = input("Enter your password:")

        with open(customers_file, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[0] == str(id):
                    cnt = 0
                    while cnt < 3:
                        if row[4] == password:
                            print("Logged in successfully!")
                            print(line_sep)
                            self.curr_id = id
                            self.role = row[5]
                            return self.create_role_instance()
                        else:
                            print("Wrong password.")
                            password = input("Try again: ")
                            print(line_sep)
                            cnt += 1

                    print("You've exceeded the number of tries.")
                    return None

            print("User doesn't exist! Please sign up.")
            print(line_sep)
            return None

    def create_role_instance(self):
        if self.role == "admin":
            return AdminUser(self.curr_id)
        else:
            return RegularUser(self.curr_id)

    def sign_up(self) -> int:
        print(f"{COLORS.GREEN}-0-0-0-0 sign up -0-0-0-{COLORS.RESET}")
        name = input("Enter your name : ")
        age = input("Enter your age: ")
        phone = input("Enter your phone number: ")
        pasword = str()
        while True:
            pasword = input("Enter your password: ")
            confirm_pasword = input("Retype your password: ")
            if pasword == confirm_pasword:
                pasword = pasword
                break

        global row_count
        # check if the user exists (check by the phone)
        with open(customers_file, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[3] == phone:
                    print(f"{COLORS.RED}phone number is already exits!{COLORS.RESET}")
                    print("Please login please. or choose another one.")
                    print(line_sep)
                    self.login()
                    return -1

        with open(customers_file, "a", newline="") as file:
            global curr_id
            writer = csv.writer(file)
            id = row_count
            role = "user"  # Default role for new users
            writer.writerow([id, name, age, phone, pasword, role])
            self.curr_id = id
            return id


class AdminUser(Customer):
    def __init__(self, user_id):
        super().__init__()
        self.curr_id = user_id
        self.inventory = Inventory()
        self.balance = Balance()

    def show_menu(self):
        print(f"{COLORS.GREEN}-0-0-0-0 Admin Menu -0-0-0-{COLORS.RESET}")
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Update Product")
        print("4. Show Inventory Total Profit")
        print("5. View All Users")
        print("6. Balance Sheet.")
        print("7. Logout")
        print(line_sep)

    def add_product(self):
        self.inventory.add_item()

    def update_product(self):
        item_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        self.inventory.update_item(item_name, quantity)

    def show_profit(self):
        self.inventory.show_total_profit()

    def view_users(self):
        with open(customers_file, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            print("\nRegistered Users:")
            for row in reader:
                if row[5] == "user":
                    print(f"ID: {row[0]}, Name: {row[1]}, Role: {row[5]}")


class RegularUser(Customer):
    def __init__(self, user_id):
        super().__init__()
        self.curr_id = user_id
        self.inventory = Inventory()

    def show_menu(self):
        print(f"{COLORS.GREEN}User Menu:{COLORS.RESET}")
        print("1. View Products")
        print("2. Buy Products")
        print("3. Logout")

    def buy_product(self):
        self.inventory.show_products()
        print(line_sep)
        product_id = input("Enter product ID to buy: ")
        quantity = int(input("Enter quantity: "))
        print(line_sep)

        done, id = self.inventory.update_item(product_id, quantity)

        if done:
            current_time = datetime.now()
            day = current_time.day
            month = current_time.month
            year = current_time.year
            time = current_time.strftime("%H:%M:%S")

            price = self.inventory.get_product_price(id)
            total_price = price * quantity

            transaction = [
                self.curr_id,  # user_id
                id,  # product_id
                quantity,
                total_price,
                day,
                month,
                year,
                time,
            ]

            # Append to transactions file
            with open(transactions_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(transaction)
                print(
                    f"{COLORS.GREEN}Transaction recorded at {time} on {day}/{month}/{year}{COLORS.RESET}"
                )
