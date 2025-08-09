import csv
import os

class customer:
    def __init__(self, Name , Age , PhoneNumber , ID ):
        self.Name = Name
        self.Age = Age
        self.PhoneNumber = PhoneNumber
        self.ID = ID
        self.customerlisthead = ["Name", "Age", "PhoneNumber", "ID","price"]
        self.customerlist = [self.Name, self.Age, self.PhoneNumber, self.ID]
        self.allcustomerslist = []


    def AddCustomer(self):
        file_exists = os.path.isfile("CustomerData.csv")
        with open("CustomerData.csv","a",newline="") as f:
            writer = csv.DictWriter(f, fieldnames = self.customerlisthead)
            if not file_exists:
                writer.writeheader()

            writer.writerow({
                self.customerlisthead[0]: self.customerlist[0], self.customerlisthead[1]: self.customerlist[1],
                self.customerlisthead[2]: self.customerlist[2],
                self.customerlisthead[3]: self.customerlist[3] ,
                self.customerlisthead[4]: self.customerlist[4]
            })
