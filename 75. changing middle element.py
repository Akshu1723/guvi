akshu=input()
if len(akshu)%2!=0:
    s=int(len(akshu)/2)
    s1=akshu[:s]
    s2=akshu[s+1:len(akshu)]
    print(s1+'*'+s2)
else:
    s=int(len(akshu)/2)
    s1=akshu[:s-1]
    s2=akshu[s+1:len(akshu)]
    print(s1+'**'+s2)
