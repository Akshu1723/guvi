akshu=int(input())
if akshu>1:
    for ak in range(2,akshu):
        if(akshu%ak==0):
            print('yes')
            break
    else:
        print('no')
else:
    print('yes')
