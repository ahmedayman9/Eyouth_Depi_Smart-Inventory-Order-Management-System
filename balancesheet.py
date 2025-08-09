
class balanceSheet:
    def __init__(self, month):
        self.month = month
        self.total = 0
        self.profit = 0
        self.read_past_data()


    # Save the current month's data to the CSV file with removing past data with the same month
    def save_to_csv(self):
        with open('balancesheet.csv', 'r') as file:
            lines = file.readlines()
        with open('balancesheet.csv', 'w') as file:
            for line in lines:
                if not line.startswith(self.month):
                    file.write(line)
            file.write(f'{self.month}, {self.total}, {self.profit}\n')

    def read_past_data(self):
        with open('balancesheet.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                month, total, profit = line.strip().split(', ')

                if month == self.month:
                    self.total = float(total)
                    self.profit = float(profit)
                    return

    def add_product(self, price):
        new_entry = balanceSheet(self.month)
        new_entry.total += price
        new_entry.profit += price * 0.25
        new_entry.save_to_csv()

