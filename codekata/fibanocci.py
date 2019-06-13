nk=int(input())
aks=1
bks=1
print(aks,bks,end=" ")
while(nk-2):
    ck=aks+bks
    aks=bks
    bks=ck
    print(ck,end=" ")
    nk=nk-1
