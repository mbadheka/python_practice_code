# generator funcation

def func1(n):

    return (i for i in range(1,n+1) if i%2 == 0) # generator compresation   
    # for i in range(1,n+1):
    #     if i%2 == 0:
    #         yield i

for i in func1(10):
    print(i)