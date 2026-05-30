import random
print("---------GUESS A NUMBER---------")
level=input("choose difficulty level 'easy' 'hard' ").lower()
if level=='easy': choices=10
else: choices=5
print(f"you have {choices} choices")
choices=10
guess=False
guess_num=int(input("guess a num 1-50: "))
number=random.randint(1,51)
while not guess and choices>0:
    if guess_num==number:
        print("correct guess...!")
        break
    elif guess_num<number:
        print("guess is too low ")
        choices-=1
    else:
        print("guess is too high ")
        choices-=1
    guess_num=int(input("enter a num 1-50: "))
    