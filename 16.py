# funcation within funcation
# greater number with funcation 
num_1 = int(input("enter first number "))
num_2 = int(input("enter first number "))
num_3 = int(input("enter first number "))

def greater(a,b):
    if a<b :
        return b
    else:
        return a
def new_greater(a,b,c):
    new_var = greater(a,b)
    return greater(new_var,c)
    
print(f"{new_greater(num_1,num_2,num_3)} is greater")