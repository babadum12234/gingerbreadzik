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

ofbet=0
hand=[]
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
    global cards
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

def drawing_cards(cards, l_cards, rev1, rev2, rev3, rev4,fi_card,s_cards,th_card,fo_card):
    global s1,s2,s3,s4, first_card, second_card, third_card, fourth_card, ofbet
    s1=0
    s2=0
    s3=0
    s4=0
    if fi_card==0:
        first_card = random.choice(cards)
    else:
        first_card = fi_card
    if cards == first_card:
        if first_card==cards:
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
        if s_cards==0:
            second_card = random.choice(cards)
        else:
            second_card = s_cards
        if cards == second_card:
            if second_card==cards:
                cards.remove(second_card)
        if len(cards)<1:
            cards=fcards
            cards.remove(bot_hand)
            cards.remove(player_hand)
        a2 = math.ceil(second_card/4)
        b2 = math.floor(second_card/13)
    if l_cards>=3:
        if th_card==0:
            third_card = random.choice(cards)
        else:
            third_card = th_card
        if first_card==cards:
            cards.remove(third_card)

        if len(cards)<1:
            cards=fcards
            cards.remove(bot_hand)
            cards.remove(player_hand)
        a3 = math.ceil(third_card/4)
        b3 = math.floor(third_card/13)
    if l_cards>=4:
        if fo_card==0:
            fourth_card = random.choice(cards)
        else:
            fourth_card = fo_card
        if first_card==cards:
            cards.remove(fourth_card)
        if len(cards)<1:
            cards=fcards
            cards.remove(bot_hand)
            cards.remove(player_hand)
        a4 = math.ceil(fourth_card/4)
        b4 = math.floor(fourth_card/13)
    global hand
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
    

def stop():
    global ofbet
    print(hand)
    print(f"Charlie hand:                                  {money_bot}$")
    drawing_cards(cards, 4, "true", "true", "true", "true",0,0,0,0)
    print(f"your hand:                                     {money_player}$")
    drawing_cards(cards,4, "true", "true", "true", "true",0,0,0,0)
    print(f"your bet: {ofbet}$                    Charlie bet: {ofbet}$")
    points=0
    group=0
    for il in range(2):
        for ig in range(3):
            if hand[ig+1]==hand[il]:
                group=+1
                for im in range(3):
                    if ig+1!=im:
                        if hand[ig+1]==hand[im]:
                            group=+1
                points=points+(group+1)*math.ceil(hand[ig]/4)
                print(points)
    input()
    ofbet=0




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
    global money_player, money_bot, ofbet
    while int(bet)<100 or int(bet)>money_player:
        if int(bet)<100:
            print("too little, you can least give 100$")
            bet=input()
            bet=int(bet)
        if int(bet)>money_player:
            print("too much, please try again:")
            bet=input()
            bet=int(bet)
        money_player=-bet
        money_bot=-bet
        ofbet=ofbet+bet
    print(f"your bet: {ofbet}$                    Charlie bet: {ofbet}$")


def decicion(l_disc):
    s=0
    while l_disc<=4 or l_disc>=0 or s<=4 or s>=0 or l_disc==100:
        if l_disc==0:
            print("next")
            break
        elif l_disc==1:
            s=input()
            s=int(s)
            player_hand[s-1]=0
            break
        elif l_disc==2:
            s=input()
            s=int(s)
            player_hand[s-1]=0
            s=input()
            s=int(s)
            player_hand[s-1]=0
        elif l_disc==3:
            s=input()
            s=int(s)
            player_hand[s-1]=0
            s=input()
            s=int(s)
            player_hand[s-1]=0
            s=input()
            s=int(s)
            player_hand[s-1]=0
            break
        elif l_disc==4:
            s=input()
            s=int(s)
            player_hand[s-1]=0
            s=input()
            s=int(s)
            player_hand[s-1]=0
            s=input()
            s=int(s)
            player_hand[s-1]=0
            s=input()
            s=int(s)
            player_hand[s-1]=0
            break
        elif l_disc==100:
            stop()
            break
        elif l_disc==10:
            bet=input()
            beting(bet)
            break




# def cards_play(bot_hand,player_hand,money_bot,money_player):
print(f"Charlie hand:                                  {money_bot}$")
drawing_cards(cards, 4, "false", "false", "false", "false",0,0,0,0)
bot_hand=hand
print(f"your hand:                                     {money_player}$")
drawing_cards(cards,4, "true", "true", "true", "true",0,0,0,0)

player_hand=hand
bet=input()
beting(bet)
print("co chcesz zrobić:")
l_disc=int(input())
decicion(l_disc)

print(f"Charlie hand:                                  {money_bot}$")
drawing_cards(cards, 4, "false", "false", "false", "false",bot_hand[0],bot_hand[1],bot_hand[2],bot_hand[3])
bot_hand=hand
print(f"your hand:                                     {money_player}$")
drawing_cards(cards,4, "true", "true", "true", "true",player_hand[0],player_hand[1],player_hand[2],player_hand[3])

player_hand=hand
bet=input()
beting(bet) 
