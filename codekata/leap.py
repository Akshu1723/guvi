v=int(input())
if (v%4)==0 and (v%100)!=0:
  print('yes')
elif(v%400)==0:
  print('yes')
else:
  print('no')
