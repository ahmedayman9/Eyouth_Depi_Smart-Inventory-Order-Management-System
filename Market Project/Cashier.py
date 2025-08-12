from MarketSells import marketsells


class cashier(): 
    def __init__(self,  name , Type = "Cashier"): 
       
        self.type = Type  
        self.market = marketsells(name)
    
    def sale(self): 
        self.market.sale_product()

