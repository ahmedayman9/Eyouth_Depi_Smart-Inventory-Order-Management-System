from datetime import datetime
from modules.cli_colors import COLORS
import os
import csv

line_sep = str(f"####" + f"{COLORS.GREEN}-{COLORS.RESET}" * 40 + "####")

curr_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(curr_dir)
transactions_file = os.path.join(project_root, "data", "transactions_log.csv")


class Balance:

    def calculate_balance(slef, transaction):
        total_sales = sum(float(t[3]) for t in transaction)
        total_items = sum(float(t[2]) for t in transaction)
        return total_sales, total_items

    def show_sales(self, choice):
        with open(transactions_file, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            transactions = list(reader)
        if not transactions:
            print(f"{COLORS.RED}No transactions found!{COLORS.RESET}")
            return

        current_date = datetime.now()

        # daily
        if choice == 1:
            daily_transactoins = [
                t
                for t in transactions
                if int(t[4]) == current_date.day
                and int(t[5]) == current_date.month
                and int(t[6]) == current_date.year
            ]

            total_sales, total_items = self.calculate_balance(daily_transactoins)
            print(
                f"\n{COLORS.GREEN}Daily Balance Sheet - {current_date.strftime('%d/%m/%Y')}{COLORS.RESET}"
            )
            print(f"Total Sales: ${total_sales:.2f}")
            print(f"Total Profit: ${total_sales * .25:.2f}")
            print(f"Total Items Sold: {total_items}")

        # mothly
        elif choice == 2:
            monthly_transactoins = [
                t
                for t in transactions
                if int(t[5]) == current_date.month and int(t[6]) == current_date.year
            ]

            total_sales, total_items = self.calculate_balance(monthly_transactoins)
            print(
                f"\n{COLORS.GREEN}Monthly Balance Sheet - {current_date.strftime('%m/%Y')}{COLORS.RESET}"
            )
            print(f"Total Sales: ${total_sales:.2f}")
            print(f"Total Profit: ${total_sales * .25:.2f}")
            print(f"Total Items Sold: {total_items}")

        # annually
        elif choice == 3:
            yearly_transactoins = [
                t for t in transactions if int(t[6]) == current_date.year
            ]

            total_sales, total_items = self.calculate_balance(yearly_transactoins)
            print(
                f"\n{COLORS.GREEN}Annual Balance Sheet - {current_date.strftime('%Y')}{COLORS.RESET}"
            )
            print(f"Total Sales: ${total_sales:.2f}")
            print(f"Total Profit: ${total_sales * .25:.2f}")
            print(f"Total Items Sold: {total_items}")

        print(line_sep)

    def show_menu(self) -> int:
        print(f"{COLORS.GREEN}-0-0-0-0 Balance Sheet -0-0-0-{COLORS.RESET}")
        print("1. Daily balance sheet")
        print("2. Mothly balance sheet")
        print("3. Annually balance sheet")
        print(line_sep)
        while True:
            try:
                ch = int(input("Enter your Choice: "))
                if ch > 3 or ch < 1:
                    print(f"{COLORS.RED} please enter a valid choice!{COLORS.RESET}")
                else:
                    return ch
            except ValueError:
                print(f"{COLORS.RED}Please enter a number!{COLORS.RESET}")
