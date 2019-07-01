ak=int(input())
akshu=list(map(int,input().split()))
c=[]
for aks in akshu:
  if(akshu.count(aks)>1):
    c.append(aks)
  else:
    print(aks)
