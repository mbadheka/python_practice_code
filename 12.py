#odd even funcation
number = int(input("enter any number: "))

def odd_even(num):
    if num%2 == 0:
        return  "print number is even "
    
    else:
        return " number is odd "

print(odd_even(number))

#shorter from 
# odd_even(num):
    # return num%2 == 0 #True