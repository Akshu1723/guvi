nks=int(input())
aks=1
bks=1
print(aks,bks,end=" ")
while(nks-2):
    ck=aks+bks
    aks=bks
    bks=ck
    print(ck,end=" ")
    nks=nks-1
