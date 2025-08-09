import csv 
import os 

file_name = r'C:\Users\Debi\Desktop\Eyouth_Depi_Smart-Inventory-Order-Management-System\data\customers.csv'

    


class Customer: 
    # def __init__(self):
    row_count = None
    curr_id = None
    
    def login(self, id, password):
        global curr_id
        global row_count
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            # rows = list(reader)   
            # row_count = len(rows) 
            next(reader)
            for row in reader: 
                print(row)
                if row[0] == id: 
                    cnt = 0 
                    while True: 
                        if cnt == 3: 
                            print("You've exceded the number of tries.")
                            break 
                        if row[4] == password: 
                            print("Logged in.....!")
                            curr_id = id 
                            break
                        else : 
                            print("wrong passowrd.")
                else: 
                    print("User doesn't exit!..sign up please.")
                        
    def sign_up(self, name, age, phone, password):
        global row_count
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            global curr_id
            id = row_count
            writer.writerow([id, name, age, phone, password])
            curr_id = id 

    
    def buy():
        pass 



cus = Customer() 
cus.login(1, 'iislamgom3a')