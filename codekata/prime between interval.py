o,p= map(int,input().split())
for gk in range(o+1,p):
  if gk>1:
    for ik in range(2,gk):
      if(gk%ik==0):
        break
    else:
      print(gk,end=" ")
