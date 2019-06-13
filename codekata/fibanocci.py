number=int(input())
ak,bk=1,1
print(ak,bk,end=" ")
while(number-2):
    ck=ak+bk
    ak=bk
    bk=ck
    print(ck,end=" ")
    number=number-1
