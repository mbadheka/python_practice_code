l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

z = zip(l1,l2,l3)
 
# for i in z:
#    sum =  (i[0]+i[1]+i[2])/3
# #    avg = sum/3
#    print(sum)

# def average(*args):
#     avg = []
#     for i in zip(*args):
#         avg.append(sum(i)/len(i))
#     return avg

# print(average(l1,l2,l3))

abc = lambda *args : [sum(i)/len(i) for i in zip(*args)]

print(abc(l1,l2,l3))


