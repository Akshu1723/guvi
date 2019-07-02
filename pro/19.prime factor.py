akshu=int(input())
for ak in range(2,akshu+1):
    if akshu>1:
        for i in range(2,ak):
            if(ak%i)==0:
                break
        else:
            if(akshu%ak)==0:
                print(ak,end=" ")
