import csv

class BalanceSheet:
    def __init__(self):
        self.salesPath = r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\sales.csv"

    def monthly_report(self, month):
        total_sales = 0.0
        total_profit = 0.0
        sales_found = False

        with open(self.salesPath, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            
            print(f"--- Sales Report for Month: {month} ---")
            print(f"{'Sale ID':<20} {'Product Name':<20} {'Quantity':<10} {'Total Price':<15} {'Total Profit':<15}")
            
            for row in reader:
                if int(row["Month"]) == month:
                    sales_found = True
                    sale_id = row["sale_ID"]
                    product_name = row["product_name"]
                    quantity = int(row["quantit_sold"])
                    total_price = float(row["total_price"])
                    total_profit_sale = float(row["total_profit"])

                    total_sales += total_price
                    total_profit += total_profit_sale

                    print(f"{sale_id:<20} {product_name:<20} {quantity:<10} {total_price:<15.2f} {total_profit_sale:<15.2f}")

        if not sales_found:
            print("No sales found for this month.")
            return

        profit_percentage = (total_profit / total_sales) * 100 if total_sales > 0 else 0

        print("\n--- Summary ---")
        print(f"Total Sales: {total_sales:.2f}")
        print(f"Total Profit: {total_profit:.2f}")
        print(f"Profit Percentage: {profit_percentage:.2f}%")
