winning_number = 23
guess_number = int(input("enter guessing number: "))

if winning_number==guess_number:
    print("your win !!")
elif winning_number > guess_number:
    print("too low !")
else :
    print("too high !")