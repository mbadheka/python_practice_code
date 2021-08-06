######  del, pop , and  remove method ####3

list_1 = [1,2,3,4,5,6]

#delete is key word which uses index as a parameter 

del list_1[2]
print(list_1)
# pop method is using index value as a parameter which also return the deleted value
list_1.pop(0)
print(list_1)

## remove() method uses value as a parameter 
list_1.remove(5)
print(list_1)