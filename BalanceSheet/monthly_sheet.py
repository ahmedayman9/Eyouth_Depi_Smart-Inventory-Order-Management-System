from BalanceSheet.sheet_data import Data


class MonthlySheet:
    def __init__(self):
        self.data = {}
        self.add_initial_data()

    def add_data(self, month, gross_profit, net_profit):
        new_data = Data(gross_profit, net_profit)
        self.data[month] = new_data

    def add_initial_data(self):
        """Initialize with some data for demonstration."""
        self.add_data(1, 5000, 3000)
        self.add_data(2, 6000, 3500)
        self.add_data(3, 7000, 4000)
        self.add_data(4, 8000, 4500)
        self.add_data(5, 9000, 5000)
        self.add_data(6, 10000, 5500)
        self.add_data(7, 11000, 6000)