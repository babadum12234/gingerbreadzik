import math
print("wpisz licbe:")
a=int(input())
while a>3999:
    print("Liczba jest za wielka, wpistyz niejsza liczbe:")
    a=int(input())

romanumber1=" "
romanumber2=" "
romanumber3=" "
romanumber4=" "
ltysioki= math.floor(a/1000)
setki=math.floor((a-ltysioki*1000)/100)
dziesiatki=math.floor((a-ltysioki*1000-setki*100)/10)
cyfry=math.floor(a-ltysioki*1000-setki*100-dziesiatki*10)

romanumber1=ltysioki * "M"
if setki <4:
    romanumber2=setki*"C"
elif setki==4:
    romanumber2="CD"
elif setki <9:
    romanumber2 = "D" + (setki-5) * "C"
else:
    romanumber2="CM"

if dziesiatki<4:
    romanumber3=dziesiatki*"X"
elif dziesiatki==4:
    romanumber3="XL"
elif dziesiatki<9:
    romanumber3="L"+(dziesiatki-5)*"X"
else:
    romanumber3="XC"

if cyfry<4:
    romanumber4="I"*cyfry
elif cyfry==4:
    romanumber4="IV"
elif cyfry<9:
    romanumber4="V"+(cyfry-5)*"I"
else:
    romanumber4="IX"
print(romanumber1+romanumber2+romanumber3+romanumber4)
