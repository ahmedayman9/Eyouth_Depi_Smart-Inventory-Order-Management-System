import os
import csv


# make file path works on all platforms (linux, windows, macos)
curr_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(curr_dir)
inventory_file_name = os.path.join(project_root, "data", "supermarket_inventory.csv")


class Inventory:
    # def __init__(self):
    #     self.inventory = {}

    def show_products(
        self,
        file_name=inventory_file_name,
    ):
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            print("\nproducts available in inventory are:")
            next(reader)
            for row in reader:
                print(
                    f"product id:{row[0]}, product:{row[1]}, price:{row[2]},  stock:{row[3]} ,categoty:{row[4]}"
                )

    def add_item(
        self,
        file_name=inventory_file_name,
    ):
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            last_id = 0
            for row in reader:
                last_id = int(row[0])

            new_id = last_id + 1
            product_name = input("enter product name:")
            product_price = input("enter product price:")
            product_stock = input("enter product stock:")
            product_category = input("enter product category:")

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [new_id, product_name, product_price, product_stock, product_category]
            )
            print("/nproduct added successfully to the inventory ...")

    def show_total_profit(
        self,
        file_name=inventory_file_name,
    ):
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            total_profit = 0
            for row in reader:
                product_price = float(row[2])
                product_stock = int(row[3])
                total_profit += product_price * product_stock

            total_profit *= 0.25
            print(f"your total profit in  25 percentage is:{total_profit}")

    def update_item(
        self,
        item_name,
        quantity,
        file_name=inventory_file_name,
    ):
        updated_rows = []
        item_found = False
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            updated_rows.append(header)
            for row in reader:
                if not row:
                    continue
                if row[1] == item_name and not item_found:
                    if int(row[3]) >= quantity:
                        row[3] = str(int(row[3]) - quantity)
                        print(
                            f"{quantity} {item_name} removed successfully from the inventory and the current stock is {row[3]}"
                        )
                        item_found = True
                    else:
                        print(f"Sorry, we only have {row[3]} in stock.")
                updated_rows.append(row)
        if updated_rows[1]:
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)


inv = Inventory()
# inv.show_products()
# inv.add_item()
# inv.show_total_profit()
inv.update_item("Cake", 4)
