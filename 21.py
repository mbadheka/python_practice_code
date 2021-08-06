# adding item in list

empty_list = []

empty_list.append("mango") 
empty_list.append("banana")
empty_list.append("orange")
#remember append method adds item at last

print(empty_list)

# more methods to add items inside list
######### Insert methods ##########

list_1 = ['mango','bananna','grape']
list_1.insert(1,'orange')
print(list_1)

############### adding 2 list together (concatenate)###########

list_2 = ['num1', 'num2 ', 'num 3']

list_3 = list_1+list_2
print(list_3)

list_1.extend(list_2)
print(list_1)

######## List within list using append ########

list_1.append(list_2)
print(list_1)