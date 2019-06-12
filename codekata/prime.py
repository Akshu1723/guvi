po=int(input())
if po>1:
  for ke in range(2,po//2):
    if(po%ke)==0:
      print('no')
      break
  else:
    print('yes')
else:
  print('yes')
