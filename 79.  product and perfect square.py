import math
ak,bk=map(int,input().split())
number=ak*bk
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print('yes')
else:
    print('no')
