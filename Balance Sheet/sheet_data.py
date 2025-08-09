class Data:
    def __init__(self, gross_profit, net_profit):
        self.gross_profit = gross_profit
        self.net_profit = net_profit

class MonthlySheet:
    def __init__(self):
        self.data = {}

    def add_data(self, gross_profit, net_profit):
        new_data = Data(gross_profit, net_profit)
        self.data[self.month] = new_data
