import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special_chars=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|','}', '~']

print("this is a password generator....!")
l=int(input("enter no of letters: "))
sc=int(input("enter no of special characters: "))
n=int(input("enter how many numbers: "))
password_list=[]
for i in range(l):
    password_list.append(random.choice(letters))
for i in range(sc):
    password_list.append(random.choice(special_chars))
for i in range(n):
    password_list.append(random.randint(0,9))
 
random.shuffle(password_list)
password=""

for i in password_list:
    password+=str(i)
print(password)