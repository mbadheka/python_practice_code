# try and except

while True:
    try :
        age = int(input('please enter your age : '))
        break
    except ValueError:
        print ("Please enter number ")
    except :
        print("unexpected error")

if age > 18 :
    print('you can play this game ')
else :
    print("you can't play this game ") 