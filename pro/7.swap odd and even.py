akshu=input()
l=[akshu[i] for i in range(len(akshu)) if i%2==0]
l1=[akshu[i] for i in range(len(akshu)) if i%2!=0]
for j in range(len(akshu)//2):
  print(l1[j]+l[j],end="")
