list1 = [1, 2.3, ' absvs', [1,'cd','23'],7.9]

list2 = [i for i in list1 if type(i) == float or type(i) == int]

# for i in list1: 
#     if type(i) == float or type(i) == int:
#         list2.append(i)

print(list2)

