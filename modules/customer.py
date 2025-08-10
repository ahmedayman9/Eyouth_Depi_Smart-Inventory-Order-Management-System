import csv
import os

file_name = r"./data/customers.csv"


class Customer:
    curr_id = None

    def login(self, id, password):
        global curr_id
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[0] == str(id):
                    cnt = 0
                    while True:
                        if cnt == 3:
                            print("You've exceeded the number of tries.")
                            break
                        if row[4] == password:
                            print("Logged in.....!")
                            self.curr_id = id
                            return
                        else:
                            print("wrong passowrd.")
                else:
                    print("User doesn't exit!..sign up please.")

    def sign_up(self, name, age, phone, password):
        global row_count
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            rows = list(writer)
            row_count = len(rows)
            global curr_id
            id = row_count
            writer.writerow([id, name, age, phone, password])
            self.curr_id = id

    def buy():
        pass


cus = Customer()
cus.login(1, "iislamgom3a")
