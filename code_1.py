import math
print("wpisz liczbe:")
a=int(input())
while a>3999:
    print("wpisz mniejsza liczbe:")
    a=int(input())
dlugosc = len(str(a))
if dlugosc == 4:
    z= math.floor(a/1000)
    romanumber1=z * "M"
    z=math.floor(a/100)
    if z <4:
        romanumber2=z*"C"
    
astring=str(a)
