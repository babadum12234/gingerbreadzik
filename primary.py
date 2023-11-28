primary=3
tab_primarys=[3]
j=0
print("co ktora liczbe pierwsza chcesz dostac:")
a=int(input())
def wypisanie(h, a):
    if h%a == 0:
        print(primary)
h=0
print("2")
if a == 1:
    print("3")
while h==h:
    h+=1
    j=0
    primary=primary+2
    while tab_primarys[j]<1/2 * primary:
        if primary%tab_primarys[j]==0:
            primary=primary+2
            j=0
        else:
            j=j+1
            if j+1>len(tab_primarys):
                primary=primary+2
                j=0

    tab_primarys.append(primary)
    # print(primary)
    wypisanie(h,a)