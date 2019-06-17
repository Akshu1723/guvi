n=int(input())
akshu = (n // 10) * 10
bk = akshu + 10
print(bk if n - akshu < bk - n else akshu) 
