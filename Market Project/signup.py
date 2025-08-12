import csv
from Cashier import *
from stockManager import *

class Signup(): 
    def __init__(self, user_name, Password, Name, Age, Type, Salary):
        self.user_name = user_name
        self.Password = Password
        self.Name = Name
        self.Age = Age
        self.Type = Type
        self.Salary = Salary

    def check_data(self): 
        with open(r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\users.csv", "r", encoding="utf-8") as f: 
            reader = csv.DictReader(f)
            for row in reader:
                if row["user_name"] == self.user_name: 
                    print("This user already exists")
                    return False
        return True

    def save_user(self):
        file_exists = False
        try:
            with open(r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\users.csv", "r", encoding="utf-8") as f:
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open(r"c:\Users\ahmed\Desktop\Projects in python\Market Project\Data Base\users.csv", "a", newline="", encoding="utf-8") as f:
            fieldnames = ["user_name", "Password", "Name", "Age", "Type", "Salary"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "user_name": self.user_name,
                "Password": self.Password,
                "Name": self.Name,
                "Age": self.Age,
                "Type": self.Type,
                "Salary": self.Salary
            })
            print("User saved successfully!")
