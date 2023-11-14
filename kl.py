#a = 5.1
#print'%.20f'%a

# suma = 2+2
# roznica = 4-2
# iloczyn = 4*2
# iloraz = 4/2
# potegaa = 3**2
# mosulo = 5%2

# import random
# los=random.randint(1,20)
# print(los)

# import math
# potega=math.pow(2,3)
# print(potega)

# liczba=int(input("podaj liczbe: "))
# if liczba > 0:
#     print("wieksza")
# elif liczba < 0:
#     print("mmniejsza")
# else:
#     print("rowna")

# for i in range(6):
#     print(10975 + i)

# for i in range(1, 21, 2):
#     print(i)

# for litera in "slowo":
#     if litera=="o":
#         continue
#     print(litera)

# liczba=int(input("wpisz: "))
# while liczba<0:
#     liczba=int(input("kolejna: "))
# a = 45
# def bodzio(a):
#     if a==0:
#         return  "nie przez zero"            #break do funkcji

#     print("bum,", a)
    
# bodzio(a = input("liczba: "))

# zbiorek=[5,2,4,8]
# # print(type(zbiorek))                        #typ zmiennej sprawdzamy
# # print(zbiorek)                              #[5,2,4,8]
# # print(*zbiorek)                             #5,2,4,8
# # print(*zbiorek, sep=";")

# zbiorek.sort()
# print(zbiorek)                                #[2,4,5,8]

# zbiorek.reverse()
# print(zbiorek)                                #[8,4,2,5]

# print(zbiorek[1])
# print(len(zbiorek))
# zbiorek[2]=3

# for i in zbiorek:
#     print(i)

# duplo=(3,2,6, "ziuzio")                                 #nie zmieniana tablica
# print(duplo)


#SŁOWNIKI:
kontakty={}
kontakty["miś"] = 34
kontakty["patys"] = 63632

kontakty={
    "hubek": 7463,
    "bedzie": 6261,
    "PC": 62626262
}

print(kontakty["hubek"])

for dff, sa in kontakty.items():
    print("%s ma numer: %d" %(dff,sa))

print(kontakty.keys())                          #wypisze imiona
print(kontakty.values())                        #wypisze wartości

del kontakty["bedzie"]                          #usunięcie