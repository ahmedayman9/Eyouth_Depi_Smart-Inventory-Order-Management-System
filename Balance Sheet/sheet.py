class SheetManager:
    def __init__(self, monthly_sheet):
        self.monthly_sheet = monthly_sheet

    def show_monthly_data(self):
        for month in range(1, 13):
            if month in self.monthly_sheet.data:
                data = self.monthly_sheet.data[month]
                print(f"Month: {month}, Gross Profit: {data.gross_profit}, Net Profit: {data.net_profit}")
            else:
                print(f"Month: {month}, No data available")
        