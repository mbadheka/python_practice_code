def number(num,*args):
    if args == ():
        return "you did not pass any args"
    else :
        return [i**num for i in args]
print(number(2,2,3,3,3,5,3))


