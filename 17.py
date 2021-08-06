# define palindrome funcation
name = input("enter your name ")
def palindrome (abc):
    return abc == abc[::-1]
print(palindrome(name))