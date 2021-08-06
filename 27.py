# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
number= input("enter number , sperated ")
list = number.split(",")
tuple = tuple(list)
print(f"{list}\n{tuple}")