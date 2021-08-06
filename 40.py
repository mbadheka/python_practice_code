# OOP concept class

class Laptop:
    def __init__(self,brand_name,model_name,price):
        #instances variable 
        print("init method called")
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price


obj1 = Laptop("lenovo","idea pad",1000)
obj2 = Laptop("dell","inspiron",950)

print(obj1.brand_name)
print(obj2.price)