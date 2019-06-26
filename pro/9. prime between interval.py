ak,bk=map(int,input().split())
l=[]
for i in range(ak+1,bk+1):
  if i>1:
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      l.append(j)
print(len(l)+1)
