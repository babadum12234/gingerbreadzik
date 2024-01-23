print("podaj liczbe i kliknij enter")
a = int(input())
print("wybierz znak z posrod: +,-,x,/; jeeli chcesz wyłaczyć kliknij d i kliknij enter")
z = input()
znaki=["+", "-", "x", "/", "%"]
while z not in znaki:
    print("Padales zly znak, sprobuj jeszcze raz, wybierz znak z posrod: +,-,x,/,% ; i kliknij enter")
    z = input()
print("podaj druga liczbe i kliknij enter")
b = int(input())
while z == "/" and b == 0:
    print("error, nie mozna dzielic przez zero")
    print("podaj druga liczbe i kliknij enter")
    b = int(input())
if z == "+":
    print(a,"+",b,"=",a+b)
    a=a+b
if z == "-":
    print(a,"-",b,"=",a-b)
    a=a+b
if z == "x":
    print(a,"x",b,"=",a*b)
    a=a+b
if z == "/":
    print(a,"/",b,"=",a/b)
    a=a+b
if z == "%":
    print(a,"%",b,"=",a%b)
    a=a+b