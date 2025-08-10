from modules import cli_colors
import csv
import os


# CLI Colors
GREEN = cli_colors.COLORS.GREEN
RED = cli_colors.COLORS.RED
RESET = cli_colors.COLORS.RESET

# make file path works on all platforms (linux, windows, macos)
curr_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(curr_dir)
file_name = os.path.join(project_root, "data", "customers.csv")

with open(file_name, "r", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)
    row_count = len(rows)


class Customer:
    # def __init__(self):
    curr_id = None

    def login(self) -> int:
        print(f"{GREEN}-0-0-0-0 login -0-0-0-{RESET}")
        global curr_id
        id = int(input("Enter your ID: "))
        password = input("Enter your password:")
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
                            return 0
                        else:
                            print("wrong passowrd.")
                else:
                    print("User doesn't exit!..sign up please.")
                    self.sign_up()
                    return 1

    def sign_up(self) -> int:
        print(f"{GREEN}-0-0-0-0 sign up -0-0-0-{RESET}")
        name = input("Enter your name : ")
        age = input("Enter your age: ")
        phone = input("Enter your phone number: ")
        pasword = str()
        while True:
            pasword = input("Enter your password: ")
            confirm_pasword = input("Retype your password: ")
            if pasword == confirm_pasword:
                pasword = pasword
                break

        global row_count
        # check if the user exists (check by the phone)
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[3] == phone:
                    print(f"{RED}phone number is already exits!{RESET}")
                    print("Please login please. or choose another one.")
                    self.login()
                    return -1

        with open(file_name, "a", newline="") as file:
            global curr_id
            writer = csv.writer(file)
            id = row_count
            writer.writerow([id, name, age, phone, pasword])
            self.curr_id = id
            return id

    def buy():
        pass


# cus = Customer()
# cus.login(1, "iislamgom3a")
