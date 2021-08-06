# scope variable 

x = 5 #global variable

def fun():
    global x 
    x = 8 #local variable
    return x

# print(x)  {Global}
# print(fun(x))     {local}

# print(x)
# print(fun()) # funcation is changing global variable value


