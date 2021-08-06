#dictionary exercise 

def number_cube(n):
    dic1 = {}
    for i in range(1,n+1):
        dic1[i]=i**3
    return dic1
print(number_cube(10))

## dictionary Comprehension 

number = {num : num**2 for num in range(1,11)}
print(number)


odd_even = {i:('even'if i%2 == 0 else 'odd') for i in range(1,11)}
print(odd_even)