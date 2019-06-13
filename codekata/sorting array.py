ak=int(input())
ak=list(map(int,input().split()))
ak.sort()
for j in range(len(ak)):
    print(ak[j],end=" ")
