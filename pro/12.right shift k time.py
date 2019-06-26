ak,bk=map(int,input().split())
lk=list(input().split())
lk=lk[-bk:]+lk[:-bk]
print(" ".join(lk))
