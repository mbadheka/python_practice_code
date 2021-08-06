list1 = ['malhar','badheka']

list2 = []

# for i in list1:
#     list2.append(i[::-1])
# print(list2)

# list2 = [ name[::-1] for name in list1 ]
# print(list2)


def revers(l):
    return[ name[::-1] for name in l ]

print(revers(['malhar','badheka']))