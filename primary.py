primary=3
tab_primarys=[3]
j=0
#tab_primarys.append(3)
for i in range(100):
    j=0
    primary=primary+2
    while tab_primarys[j]<1/2 * primary:
        if primary%tab_primarys[j]==0:
            primary=primary+2
        else:
            j=j+1
            if j>len(tab_primarys):
                primary=primary+2

    tab_primarys.append(primary)
    print(primary)

#i:                   0 1   
#f:                   0 1
#primary:           3 5
#tab_primary:       3