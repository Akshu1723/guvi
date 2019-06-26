akshu,aksh=map(str,input().split())
if(len(akshu)!=len(akshu)):
  print("no")
c=[akshu.count(i) for i in akshu]
d=[aksh.count(i) for i in aksh]
if c==d:
  print("yes")
else:
  print("no")
