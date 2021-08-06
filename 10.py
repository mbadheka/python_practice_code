#guessing random numbers 
# DRY principal
import random
var_1 = random.randint(0,101)
guess_number = int(input("enter number from 1 to 100: "))
guess = 1
game_over = False 

while not game_over:
    if guess_number == var_1: 
        print(f"you have guessed right number: {guess_number} in {guess} times")
        break
    else:
        if guess_number < var_1:
            print("too low !")
            
        else:
            print("too high")
        
        guess_number = int(input("try again "))
        guess+=1
    