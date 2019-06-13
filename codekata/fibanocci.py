nk=int(input())
aks,bk=1,1
print(aks,bk,end=" ")
while(nk-2):
    ck=aks+bk
    aks=bk
    bk=ck
    print(ck,end=" ")
    nk=nk-1
