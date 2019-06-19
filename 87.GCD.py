a,b=map(int,input().split())
def gcd(a,b):
  if b!=0:
    return gcd(b,a%b)
  else:
    return a
print(gcd(a,b))
