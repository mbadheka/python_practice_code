def divide(a,b):
    try :
        return a/b
    except ZeroDivisionError:
        print("please do not divide by zero")
    except:
        print("please only enter number")


# print(divide('aa',5))
# print(divide(10,5))
print(divide(14,0))
