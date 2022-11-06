import random
from art import logo
def select_card(cards,players):
    n=random.randint(0,12)
    players.append(cards[n])
    return
def sumlist(x):
    sum=0
    for i in x:
        sum=sum+i
    return sum;
def dealers_check():
    n2 = sumlist(dealers_card)
    while (n2 < 17):
        select_card(card, dealers_card)
        n2=sumlist(dealers_card)


def gameovercheck():
    n=sumlist(players_card)
    if(n>21):
        dealers_check()
        n2=sumlist(dealers_card)
        if(n2>21):
            print(dealers_card)
            print("draw both are mmore than 21")
            exit()
        print("BUST , ppoint > 21 , you loose")
        print("yoour point = {} \n".format(n))
        exit()




yes_no = input("Do you want play black jack (yes/no)")
if(yes_no == "no"):
    exit()
print(logo)
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
players_card = []
dealers_card = []

select_card(card,dealers_card)
select_card(card,dealers_card)

select_card(card,players_card)
select_card(card,players_card)

print("DEalers card is {}".format(dealers_card[0]))
print("YOOUR CARDS {}".format(players_card))
hit=input("do you want to take another card ? (yes/no)")
while(hit != "no"):
    select_card(card,players_card)
    print("your cards are {}".format(players_card))
    gameovercheck()
    hit = input("do you want to take another card ? (yes/no)")

sum1 = sumlist(players_card)
dealers_check()
sum2 = sumlist((dealers_card))
print("dealers card is : {}".format(dealers_card))
gameovercheck()

if (sum1>sum2):
    print("you win !!")
    exit()
elif (sum1<sum2):
    if(sum2>21):
        print("you win, dealer is a bust > 21 points")
        exit()
    print("you loose")
else:
    print("drw")