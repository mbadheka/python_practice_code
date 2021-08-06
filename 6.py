num = input("Enter number: ")
total= 0 
i = 0
while i<=len(num)-1:
    total = total + int(num[i])
    i = i+1
print(total)