a=list(input())
s=[]
for ak in a:
  if ak not in s:
    s.append(ak)
if a==s:
  print('yes')
else:
  print('no')
