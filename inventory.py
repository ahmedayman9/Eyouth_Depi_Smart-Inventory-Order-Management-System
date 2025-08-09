class inventory:
    def __init__(self):
        self.items = {
            201: ["milk", 25, 100],
            202: ["bread", 20, 80],
            203: ["eggs", 10, 200],
            204: ["butter", 50, 60],
            205: ["cheese", 70, 40],
            206: ["sugar", 30, 100],
            207: ["salt", 15, 150],
            208: ["rice", 40, 120],
            209: ["flour", 35, 90],
            210: ["oil", 100, 50],
            211: ["soap", 25, 110],
            212: ["shampoo", 75, 45],
            213: ["toothpaste", 40, 70],
            214: ["brush", 15, 100],
            215: ["detergent", 90, 55],
            216: ["tea", 45, 85],
            217: ["coffee", 60, 65],
            218: ["biscuits", 20, 150],
            219: ["chocolate", 35, 95],
            220: ["noodles", 30, 130],
            221: ["juice", 50, 70],
            222: ["water", 10, 200],
            223: ["soda", 20, 150],
            224: ["ketchup", 35, 60],
            225: ["mayonnaise", 45, 40],
            226: ["cornflakes", 60, 55],
            227: ["oats", 50, 65],
            228: ["pasta", 40, 90],
            229: ["tomato", 25, 100],
            230: ["potato", 20, 120],
            231: ["onion", 18, 110],
            232: ["carrot", 22, 100],
            233: ["apple", 60, 80],
            234: ["banana", 30, 95],
            235: ["grapes", 55, 85],
            236: ["orange", 50, 75],
            237: ["lemon", 15, 150],
            238: ["chicken", 150, 40],
            239: ["mutton", 300, 20],
            240: ["fish", 200, 35],
            241: ["paneer", 90, 60],
            242: ["curd", 35, 100],
            243: ["icecream", 60, 70],
            244: ["buttermilk", 20, 90],
            245: ["pickles", 40, 50],
            246: ["jam", 55, 45],
            247: ["honey", 80, 40],
            248: ["coconut oil", 120, 30],
            249: ["ghee", 150, 25],
            250: ["turmeric", 35, 75]
        }
    def show_products(self):
        for i in self.items:
            print(f"Product Name:{self.items[i][0]}\nProduct Price:{self.items[i][1]}\nProduct Quantity:{self.items[i][2]}")
            print("------------------------------------")
    def show_profit(self):
        for i in self.items:
            print(f"product {i} profit ={self.items[i][1]*self.items[i][2]*0.25}")
            print("------------------------------------")

    def buy_product(self):
        self.summ = 0
        my_prouduct = {}
        while True:
            x=int(input("enter product id : "))
            y=int(input("enter quantiy you want : "))
            self.items[x][2]-=y
            self.summ+=self.items[x][1]*y

            my_prouduct[x] = [y,self.summ]
    
            z=input("you want another items").lower()
            if z=="no":
                    print(f"you should pay : {self.summ}")
                    return self.summ
             
