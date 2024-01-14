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
for i in range(l_talia):
    i=i+1
    cards.append(i)

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


def drawing_cards(l_cards, rev1, rev2, rev3, rev4):
    first_card = random.choice(cards)
    cards.pop(first_card)
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
        cards.pop(second_card)
        a2 = math.ceil(second_card/4)
        b2 = math.floor(second_card/13)
    if l_cards>=3:
        third_card = random.choice(cards)
        cards.pop(third_card)
        a3 = math.ceil(third_card/4)
        b3 = math.floor(third_card/13)
    if l_cards>=4:
        fourth_card = random.choice(cards)
        cards.pop(fourth_card)
        a4 = math.ceil(fourth_card/4)
        b4 = math.floor(fourth_card/13)
    cards_maker(a1, b1, a2, b2, a3, b3, a4, b4, l_cards, rev1, rev2, rev3, rev4)

drawing_cards(3, "false", "true", "false", "true")

