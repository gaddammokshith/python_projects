import random
user_choice=int(input("enter your choice: 0)rock 1)paper 2)scissor"))
bot_choice=random.randint(0,2)
l=["👊","🖐️","✌️"]
if(user_choice>2): print("invalid choise, you lose...!🤕")
else:
    print("user",l[user_choice])
    print("bot",l[bot_choice])
    if(user_choice==bot_choice): print("draw.......!")
    elif(bot_choice==0 and user_choice==2): print("you lose...!🤕")
    elif(user_choice==0 and bot_choice==2): print("you win....! 🏆")
    elif(user_choice>bot_choice): print("you win....! 🏆")
    else: print("you lose...!🤕")


