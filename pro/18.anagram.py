ak=int(input())
bk=0
ck=[]
for aks in range(ak):
  ck.append(input())
for aks in range(ak):
  if(sorted(ck[aks])==sorted('kabali')):
    bk=bk+1
print(bk)
