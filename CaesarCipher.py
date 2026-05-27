def encrypt(word,key):
    newWord=""
    for i in word:
        idx=letters.index(i)
        newWord+=letters[(idx+key)%26]
    print(newWord)
    
def decrypt(word,key):
    newWord=""
    for i in word:
        idx=letters.index(i)
        newWord+=letters[(idx-key)%26]
    print(newWord)
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
choice=int(input("choose 1)encrypt 2)decrypt"))
word=input("enter a word: ").upper()
key=int(input("enter key num: "))
key=key%26
if choice==1:
    encrypt(word,key)
elif choice==2:
    decrypt(word,key)
else:
    print("invalid choice....!")


