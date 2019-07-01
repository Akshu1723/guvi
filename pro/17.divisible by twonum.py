ak,bk=map(int,input().split())
for aks in range(ak,10000):
    if(aks%ak==0 and aks%bk==0):
        print(aks)
        break
