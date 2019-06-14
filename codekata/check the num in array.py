aks,bks=map(int,input().split())
sk=list(map(int,input().split()))
for ak in sk:
  if ak==bks:
    print('yes')
    break
else:
    print('no')
