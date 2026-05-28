import os
def silent_bidding(bidders):
    winner=""
    max=0
    for name in bidders:
        if bidders[name]>max:
            max=bidders[name]
            winner=name
    print(f"winner is {winner} with bid {max}")

bidders={}
bidders_available=True
while bidders_available:
    name=input("what is your name: ")
    amount=int(input("enter your bid amount: "))
    bidders[name]=amount

    check=input("are there any bidders next..? type 'yes' or 'no' ").lower()
    
    if check=='no':
        bidders_available=False
        os.system('cls')
    else:
        os.system('cls')
print(bidders)
silent_bidding(bidders)

    

