kk=input()
jj=int(kk)
l=list(map(int,kk))
li=[i**3 for i in l]
a=sum(li)
if jj==a:
  print('yes')
else:
  print('no')
