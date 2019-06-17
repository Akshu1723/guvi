akshu=int(input())
ak,bk=map(int,input().split())
for jk in range(ak+1,bk):
    if(jk==akshu):
        print('yes')
        break
else:
    print('no')
