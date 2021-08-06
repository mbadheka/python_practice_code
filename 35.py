### IEnumarate Funcation

list1 = ['malhar','badheka','abccc']

def enu_func(l,abc):
    for pos,name in enumerate(l):
        if name == abc:
            return pos
    return -1

print(enu_func(list1,'malhar'))