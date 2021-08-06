# fibonachi series 

def fibonachi(n):
    # n = int(input("enter number: "))
    num1 = 0
    num2 = 1
    if  n == 1:
        print(f"{num1}")
    elif n == 2:

        print(f"{num1, num2}")
    else:
        print(num1, num2, end = " ")
        for i in range(n-2):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            print(num2 , end=" ")

fibonachi(20)