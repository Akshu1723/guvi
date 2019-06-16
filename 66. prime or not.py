akshu=int(input())
if akshu>1:
    for ak in range(2,akshu):
        if(akshu%ak==0):
            print('no')
            break
    else:
        print('yes')
else:
    print('yes')
