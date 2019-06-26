ak,bk=map(int,input().split())
s=[]
a=list(map(int,input().split()))
for i in a:
  if(i%2!=0):
    s.append(i)
print(s[bk-1])
