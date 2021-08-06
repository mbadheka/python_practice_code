class Laptop:
    count_instances = 0 
    def __init__(self,brand_name,model_name,price):
        #instances variable 
        # print("init method called")
        Laptop.count_instances += 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price


obj1 = Laptop("lenovo","idea pad",1000)
obj2 = Laptop("lenovo","idea pad",1000)
obj3 = Laptop("lenovo","idea pad",1000)

print(Laptop.count_instances)