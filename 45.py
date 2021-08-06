# how to read write file in python 

with open('file1.txt','r') as rf :
    with open('file2.txt','a') as wf:
        # print(rf.read())
        for lines in rf:
            name, salary = lines.split(",")
            wf.write(f"{name} salary is {salary}")
            