primary=3
tab_primarys=[3]
f=0
#tab_primarys.append(3)

for i in range (100):
    primary=primary+2
    while tab_primarys[f]<primary/2:
        f=0
        if primary % tab_primarys[f]==0:
            primary=primary+2
        else:
            f=f+1
    tab_primarys.append(primary)
    print(primary)

#i:                   0 1   
#f:                   0 1
#primary:           3 5
#tab_primary:       3