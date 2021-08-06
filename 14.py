#greater number with funcation 
num_1 = int(input("enter first number "))
num_2 = int(input("enter first number "))

def greater(a,b):
    if a<b :
        return b
    else:
        return a
print(f"{greater(num_1,num_2)} is greater")