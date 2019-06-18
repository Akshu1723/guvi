ak=input()
l1=[]
l2=[]
for a in range(0,len(ak)):
    if (a%2==0):
        l1.append(ak[a])
    else:
        l2.append(ak[a])
print("".join(l1),"".join(l2))
