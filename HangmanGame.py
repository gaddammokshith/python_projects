import random
words_list=['apple','banana','tree']
word=random.choice(words_list)
life=5
display_list=['_']*len(word)

stages = ['''.''',
    r'''+------------+
|            |
o            |
/|\           |
/ \           |
             |
''',
    r'''+------------+
|            |
o            |
/|\           |
/             |
             |
''',
    r'''+------------+
|            |
o            |
/|\           |
             |
             |
''',
    r'''+------------+
|            |
o            |
/|            |
             |
             |
''',
    r'''+------------+
|            |
o            |
|            |
             |
             |
'''
]


print(display_list,"life:",life)
word_list=[]
for i in word:
    word_list.append(i)

gameOver=False 
guess_count=0
while life>0 and not gameOver:
    guess_letter=input("Guess a letter: ");
    if guess_letter[0] in word_list:
        guess_count+=1
        for i in range(len(word)):
            if guess_letter==word_list[i]:
                display_list[i]=guess_letter
                break
    else:
        life-=1
    if guess_count==len(word):
        gameOver=True
    print(display_list,"life:",life)
    print(stages[life])
if life>0:print("you win....!")
else: print("you loose...!")
