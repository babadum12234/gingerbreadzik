# print("╔══════════════════════════╗")
# print("║´■▀▀▄´´´´´´´´´´´´´´´´´´´´´║")
# print("║´´▄▀´´´´´´´´´´´´´´´´´´´´´´║")
# print("║´█▄▄▄´´´´´´´´´´´´´´´´´´´´´║")
# print("║´´´´´´´´´´´´´´´´´´´´´´´´´´║")
# print("║´´´´´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´║")
# print("║´´´¶¶¶¶¶¶¶¶▄▄▄▄¶¶¶¶¶¶¶¶´´´║")
# print("║´´¶¶¶¶¶¶¶■▀¶¶¶¶▀▄¶¶¶¶¶¶¶´´║")
# print("║´¶¶¶¶¶¶¶¶¶¶¶¶¶▄▀¶¶¶¶¶¶¶¶¶´║")
# print("║´¶¶¶¶¶¶¶¶¶¶¶▄▀¶¶¶¶¶¶¶¶¶¶¶´║")
# print("║´´´¶¶¶¶¶¶¶▄▀¶¶¶¶¶¶¶¶¶¶¶´´´║")
# print("║´´´´´¶¶¶¶¶▀▀▀▀▀▀▀¶¶¶¶´´´´´║")
# print("║´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶´´´´´´´║")
# print("║´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´║")
# print("║´´´´´´´´´´´´¶¶´´´´´´´´´´´´║")
# print("║´´´´´´´´´´´´´´´´´´´´´▀▀▀█´║")
# print("║´´´´´´´´´´´´´´´´´´´´´´▄▀´´║")
# print("║´´´´´´´´´´´´´´´´´´´´´▀▄▄■´║")
# print("╚══════════════════════════╝")
# ╔═════════╗   
# ║.........║  
# ║...§§§...║  
# ║..§...§..║   
# ║.§.....§.║   
# ║..§...§..║   
# ║...§§§...║   
# ║.........║   
# ╚═════════╝


import random
import math
wsp_cards = []
cards=[]
l_talia=52
rev1 ="true"
rev2 ="true"
rev3 ="true"
rev4="true"
for i in range(l_talia):
    i=i+1
    cards.append(i)
fcards=cards
# print(cards)
def cards_nr_translator(n, m):
    if n == 1:
        x="A"  
    elif n == 11:
        x="J"
    elif n == 12:
        x="Q"
    elif n == 13:
        x="K"
    else:
        x = str(n)
    if m == 1:
        y="♥️"
    elif m==2:
        y="♦️"
    elif m==3:
        y="♠️"
    else:
        y="♣️"
    
    wsp_cards.append(x)
    wsp_cards.append(y)

def cards_maker(n1, m1, n2, m2, n3, m3, n4, m4, l, rev1, rev2, rev3, rev4):

    cards_nr_translator(n1, m1)
    cards_nr_translator(n2, m2)
    cards_nr_translator(n3, m3)
    cards_nr_translator(n4, m4)
    y1=wsp_cards[1]
    y2=wsp_cards[3]
    y3=wsp_cards[5]
    y4=wsp_cards[7]
    if rev1=="false":
        x1a=".."
        x1b=".."
        y1="."
    else:
        if wsp_cards[0]=="10":
            x1a=wsp_cards[0]
            x1b=wsp_cards[0]
        else:
            x1a=wsp_cards[0]+"."
            x1b="."+wsp_cards[0]

    if rev2=="false":
        x2a=".."
        x2b=".."
        y2="."
    else:
        if wsp_cards[2]=="10":
            x2a=wsp_cards[2]
            x2b=wsp_cards[2]
        else:
            x2a=wsp_cards[2]+"."
            x2b="."+wsp_cards[2]

    if rev3=="false":
        x3a=".."
        x3b=".."
        y3="."
    else:
        if wsp_cards[4]=="10":
            x3a=wsp_cards[4]
            x3b=wsp_cards[4]
        else:
            x3a=wsp_cards[4]+"."
            x3b="."+wsp_cards[4]

    if rev4=="false":
        x4a=".."
        x4b=".."
        y4="."
    else:
        if wsp_cards[6]=="10":
            x4a=wsp_cards[6]
            x4b=wsp_cards[6]
        else:
            x4a=wsp_cards[6]+"."
            x4b="."+wsp_cards[6]

    
    if l==1:
        print(f"╔═════════╗")
        print(f"║{x1a}.......║")
        print(f"║.........║")
        print(f"║.........║")
        print(f"║....{y1}....║")
        print(f"║.........║")
        print(f"║.........║")
        print(f"║.......{x1b}║")
        print(f"╚═════════╝")
    elif l==2:
        print(f"╔═════════╗   ╔═════════╗")
        print(f"║{x1a}.......║   ║{x2a}.......║")
        print(f"║.........║   ║.........║")
        print(f"║.........║   ║.........║")
        print(f"║....{y1}....║   ║....{y2}....║")
        print(f"║.........║   ║.........║")
        print(f"║.........║   ║.........║")
        print(f"║.......{x1b}║   ║.......{x2b}║")
        print(f"╚═════════╝   ╚═════════╝")
    elif l==3:
        print(f"╔═════════╗   ╔═════════╗   ╔═════════╗")
        print(f"║{x1a}.......║   ║{x2a}.......║   ║{x3a}.......║")
        print(f"║.........║   ║.........║   ║.........║")
        print(f"║.........║   ║.........║   ║.........║")
        print(f"║....{y1}....║   ║....{y2}....║   ║....{y3}....║")
        print(f"║.........║   ║.........║   ║.........║")
        print(f"║.........║   ║.........║   ║.........║")
        print(f"║.......{x1b}║   ║.......{x2b}║   ║.......{x3b}║")
        print(f"╚═════════╝   ╚═════════╝   ╚═════════╝")
    elif l==4:
        print(f"╔═════════╗   ╔═════════╗   ╔═════════╗   ╔═════════╗")
        print(f"║{x1a}.......║   ║{x2a}.......║   ║{x3a}.......║   ║{x4a}.......║")
        print(f"║.........║   ║.........║   ║.........║   ║.........║")
        print(f"║.........║   ║.........║   ║.........║   ║.........║")
        print(f"║....{y1}....║   ║....{y2}....║   ║....{y3}....║   ║....{y4}....║")
        print(f"║.........║   ║.........║   ║.........║   ║.........║")
        print(f"║.........║   ║.........║   ║.........║   ║.........║")
        print(f"║.......{x1b}║   ║.......{x2b}║   ║.......{x3b}║   ║.......{x4b}║")
        print(f"╚═════════╝   ╚═════════╝   ╚═════════╝   ╚═════════╝")

hand=0
def drawing_cards(cards, l_cards, rev1, rev2, rev3, rev4):
    first_card = random.choice(cards)
    cards.remove(first_card)
    if len(cards)<1:
        cards=fcards
        cards.remove(bot_hand)
        cards.remove(player_hand)
    a1 = math.ceil(first_card/4)
    b1 = math.floor(first_card/13)
    a2=0
    b2=0
    a3=0
    b3=0
    a4=0
    b4=0
    if l_cards>=2:
        second_card = random.choice(cards)
        cards.remove(second_card)
        if len(cards)<1:
            cards=fcards
            cards.remove(bot_hand)
            cards.remove(player_hand)
        a2 = math.ceil(second_card/4)
        b2 = math.floor(second_card/13)
    if l_cards>=3:
        third_card = random.choice(cards)
        cards.remove(third_card)

        if len(cards)<1:
            cards=fcards
            cards.remove(bot_hand)
            cards.remove(player_hand)
        a3 = math.ceil(third_card/4)
        b3 = math.floor(third_card/13)
    if l_cards>=4:
        fourth_card = random.choice(cards)
        cards.remove(fourth_card)
        if len(cards)<1:
            cards=fcards
            cards.remove(bot_hand)
            cards.remove(player_hand)
        a4 = math.ceil(fourth_card/4)
        b4 = math.floor(fourth_card/13)
    hand=[first_card, second_card, third_card, fourth_card]
    cards_maker(a1, b1, a2, b2, a3, b3, a4, b4, l_cards, rev1, rev2, rev3, rev4)

# drawing_cards(4, "true", "true", "true", "true")


# input("Hello! Welcome to casino!")
# print("what is your name?")
# name_player=input()
# input("What a cool name! let`s try win some money "+name_player+"!")
# input("in the begining you have 10000$! But you can win more!")
# input("your oponent is Charlie he hast 10000$ to, be careful! He is a tough competitor!")
# input("let's start, there are yours cards:")
# drawing_cards(4, "true", "true", "true", "true")
# input("if you want to win you must pool as many as you can cards with the same sign, the bigger the cards, the greater chance of winning!")
# input("Now give the money on the line!")
# bet=input()
money_player=10000
money_bot=10000
print("             ╔═════════╣CASINO╠═════════╗")
print("             ║´■▀▀▄´´´´´´´´´´´´´´´´´´´´´║")
print("             ║´´▄▀´´´´´´´´´´´´´´´´´´´´´´║")
print("             ║´█▄▄▄´´´´´´´´´´´´´´´´´´´´´║")
print("             ║´´´´´´´´´´´´´´´´´´´´´´´´´´║")
print("             ║´´´´´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´║")
print("             ║´´´¶¶¶¶¶¶¶¶▄▄▄▄¶¶¶¶¶¶¶¶´´´║")
print("             ║´´¶¶¶¶¶¶¶■▀¶¶¶¶▀▄¶¶¶¶¶¶¶´´║")
print("             ║´¶¶¶¶¶¶¶¶¶¶¶¶¶▄▀¶¶¶¶¶¶¶¶¶´║")
print("             ║´¶¶¶¶¶¶¶¶¶¶¶▄▀¶¶¶¶¶¶¶¶¶¶¶´║")
print("             ║´´´¶¶¶¶¶¶¶▄▀¶¶¶¶¶¶¶¶¶¶¶´´´║")
print("             ║´´´´´¶¶¶¶¶▀▀▀▀▀▀▀¶¶¶¶´´´´´║")
print("             ║´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶´´´´´´´║")
print("             ║´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´║")
print("             ║´´´´´´´´´´´´¶¶´´´´´´´´´´´´║")
print("             ║´´´´´´´´´´´´´´´´´´´´´▀▀▀█´║")
print("             ║´´´´´´´´´´´´´´´´´´´´´´▄▀´´║")
print("             ║´´´´´´´´´´´´´´´´´´´´´▀▄▄■´║")
input("             ╚══════╣Las Celejas╠═══════╝")

def beting(bet):
    while int(bet)<100 or int(bet)>money_player:
        if int(bet)<100:
            print("too little, you can least give 100$")
            bet=input()
        if int(bet)>money_player:
            print("too much, please try again:")
            bet=input()
    print(f"your bet: {bet}$                    Charlie bet: {bet}$")

discarding=[]
def decisions(l_disc, discarding):
    while l_disc<=4 or l_disc>=0 or s<=4 or s>=0:
        if l_disc==0:
            print("next")
            break
        elif l_disc==1:
            s=input()
            discarding.append(s)
            break
        elif l_disc==2:
            s=input()
            discarding.append(s)
            s=input()
            discarding.append(s)
            break
        elif l_disc==3:
            s=input()
            discarding.append(s)
            s=input()
            discarding.append(s)
            s=input()
            discarding.append(s)
            break
        elif l_disc==4:
            s=input()
            discarding.append(s)
            s=input()
            discarding.append(s)
            s=input()
            discarding.append(s)
            s=input()
            discarding.append(s)
            break

print(f"Charlie hand:                                  {money_bot}$")
drawing_cards(cards, 4, "false", "false", "false", "false")
bot_hand=hand
print(f"your hand:                                     {money_player}$")
drawing_cards(cards,4, "true", "true", "true", "true")
player_hand=hand
bet=input()
beting(bet)
decision=input()
l_disc=int(input())
decisions(l_disc, discarding)
print(discarding)
