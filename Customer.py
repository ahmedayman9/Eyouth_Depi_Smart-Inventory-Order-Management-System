import csv
class customer:
    def __init__(self, Name , Age , PhoneNumber , ID , Product_ID , Price , Profit):
        self.Name = Name
        self.Age = Age
        self.PhoneNumber = PhoneNumber
        self.ID = ID
        self.Price = Price
        self.Product_ID = Product_ID
        self.Profit = Profit
        self.customerlisthead = ["Name", "Age", "PhoneNumber", "ID", "Product_ID", "Price", "Profit"]
        self.customerlist = [self.Name, self.Age, self.PhoneNumber, self.ID, self.Product_ID, self.Price, self.Profit]
        self.allcustomerslist = []


    def createfile(self):
        with open("CustomerData.csv","",newline="") as f:
            self.writer = csv.DictWriter(f, fieldnames = self.customerlisthead)
            self.writer.writeheader()

    def Addcustomer(self):
        with open("CustomerData.csv","a",newline="") as f:

            self.writer.writerow({
                self.customerlisthead[0]:self.customerlist[0], self.customerlisthead[1]:self.customerlist[1] ,self.customerlisthead[2]:self.customerlist[2],
                self.customerlisthead[3]: self.customerlist[3] ,self.customerlisthead[4]:self.customerlist[4] , self.customerlisthead[5]:self.customerlist[5],
                self.customerlisthead[6]: self.customerlist[6]
            })









