num,key=map(int,input().split())
lisy=list(map(int,input().split()))
if len(lisy)==num:
  for a in range(len(lisy)+1):
    if (a==key):
      l=lisy[:a] 
  print(sum(l))
