j=int(input())
if (j%4)==0 and (j%100)!=0:
  print('yes')
elif(j%400)==0:
  print('yes')
else:
  print('no')
