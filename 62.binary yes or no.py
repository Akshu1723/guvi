akshu=input()
one=0
zer=0
for ak in akshu:
  if(ak=='1'):
    one=one+1
  if(ak=='0'):
    zer=zer+1
if(len(akshu)==zer+one):
  print('yes')
else:
  print('no')
