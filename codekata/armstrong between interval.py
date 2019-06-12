a,b=map(int,input().split())
for f in range(a+1,b):
    o=len(str(f))
    a=str(f)
    l=list(map(int,a))
    li=[i**o for i in l]
    k=sum(li)
    if(k==f):
        print(k)
