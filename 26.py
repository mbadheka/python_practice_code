# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name,age= input("enter your name and age ").split(",")
age= int(age)
year = 2020 - age + 100
print(f"you will turn 100 year old on {year}")