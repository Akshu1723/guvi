aks,bks=map(int,input().split())
sk=list(map(int,input().split()))
count=0
for ak in sk:
  if ak==bks:
    count=count+1
print(count)
