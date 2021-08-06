# OOP concept class

class Laptop:
    def __init__(self,brand_name,model_name,price):
        #instances variable 
        # print("init method called")
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def applied_discount(self,aa):
        jj = (self.price * aa) /100
        new_price = self.price - jj
        return new_price
    


obj1 = Laptop("lenovo","idea pad",1000)
obj2 = Laptop("dell","inspiron",950)

print(obj1.brand_name)
print(obj1.applied_discount(50))