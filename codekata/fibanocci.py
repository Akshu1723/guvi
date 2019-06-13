nk=int(input())
ak,bk=1,1
print(ak,bk,end=" ")
while(nk-2):
    ck=ak+bk
    ak=bk
    bk=ck
    print(ck,end=" ")
    nk=nk-1
