ak=list(map(int,input().split()))
bk=list(map(int,input().split()))
for i in range(0,ak[1]):
  bk=[bk[-1]] + bk[:-1]
print(*bk,end=' ')
