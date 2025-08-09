
class Balance_Sheet():
    def __init__(self, item_dict):
        self.items = item_dict 
        self.expenses = 0
        self.monthly_sales = {month: {} for month in range(1, 9)}

    def set_expenses(self, amount):
        self.expenses = amount
    
    def record_sale(self, month, item_id, quantity):
        if month not in self.monthly_sales:
            print("Invalid month. Select from 1 to 8.")
            return
        if item_id not in self.items:
            print("Invalid item.")
            return
        self.monthly_sales[month][item_id] = self.monthly_sales[month].get(item_id, 0) + quantity

    def calculate_monthly_profit(self, month):
        total_revenue = 0
        total_cost = 0
        
        for item_id, qty_sold in self.monthly_sales[month].items(): 
            selling_price = self.items[item_id][1]  
            buying_price = selling_price / 1.25     
            total_revenue += selling_price * qty_sold  
            total_cost += buying_price * qty_sold      

        gross_profit = total_revenue - total_cost
        net_profit = gross_profit - self.expenses

        return gross_profit, net_profit
    
    def calculate_total_profit(self):
        total_gross = 0
        total_net = 0

        for month in range(1, 9):
            gross, net = self.calculate_monthly_profit(month)
            total_gross += gross
            total_net += net

        return total_gross, total_net

    def display_report(self):
        print("\n balance sheet (January to August)")
        print("=" * 50)
        for month in range(1, 9):
            gross, net = self.calculate_monthly_profit(month)
            print(f"month {month}: gross profit = ${gross:.2f}, net profit = ${net:.2f}")
        print("=" * 50)
        gross_total, net_total = self.calculate_total_profit()
        print(f"total gross profit: ${gross_total:.2f}")
        print(f"total net profit:   ${net_total:.2f}")
        print("=" * 50)


items_dict = {
    201: ["milk", 25, 100],
    202: ["bread", 20, 80],
    203: ["eggs", 10, 200],
    204: ["butter", 50, 60],
}


bs = Balance_Sheet(items_dict)


bs.set_expenses(500)

bs.record_sale(1, 201, 50)  # Jan: 50 milk
bs.record_sale(1, 202, 40)  # Jan: 40 bread
bs.record_sale(2, 203, 100) # Feb: 100 eggs
bs.record_sale(8, 204, 20)  # Aug: 20 butter

bs.display_report()
        

   