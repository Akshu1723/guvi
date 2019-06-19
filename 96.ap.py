a,d,n=(map(int,input().split()))
s=0
for ak in range(1,n+1): 
    s=s+(a+(ak-1)*d)
print(s)
