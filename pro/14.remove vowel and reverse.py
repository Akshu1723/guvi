ak=int(input())
akshu=input()
lk=[]
l=['a','A','e','E','i','I','o','O','u','U']
for aks in akshu:
  if aks not  in l:
    lk.append(aks)
print("".join(lk[::-1]))
