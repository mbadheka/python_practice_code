#greater number with funcation 
num_1 = int(input("enter first number "))
num_2 = int(input("enter first number "))
num_3 = int(input("enter first number "))


def greater(a,b,c):
    if a>b and a> c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(f"{greater(num_1,num_2,num_3)} is greater")
