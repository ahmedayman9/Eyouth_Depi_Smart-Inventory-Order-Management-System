from BalanceSheet.sheet_data import Data


class MonthlySheet:
    def __init__(self):
        self.data = {}
        self.add_initial_data()

    def add_data(self, month, gross_profit, net_profit):
        if month in self.data:
            # Update existing data by adding to it
            self.data[month].gross_profit += gross_profit
            self.data[month].net_profit += net_profit
        else:
            # Create new data entry for the month
            new_data = Data(gross_profit, net_profit)
            self.data[month] = new_data

    def get_monthly_data(self, month):
        """Get data for a specific month."""
        return self.data.get(month, None)

    def show_current_month_summary(self, month):
        """Show summary for the current month."""
        if month in self.data:
            data = self.data[month]
            print(f"\n--- Month {month} Summary ---")
            print(f"Gross Profit: ${data.gross_profit}")
            print(f"Net Profit: ${data.net_profit}")
        else:
            print(f"\n--- Month {month} Summary ---")
            print("No sales data available for this month.")

    def add_initial_data(self):
        """Initialize with some data for demonstration."""
        self.add_data(1, 5000, 3000)
        self.add_data(2, 6000, 3500)
        self.add_data(3, 7000, 4000)
        self.add_data(4, 8000, 4500)
        self.add_data(5, 9000, 5000)
        self.add_data(6, 10000, 5500)
        self.add_data(7, 11000, 6000)