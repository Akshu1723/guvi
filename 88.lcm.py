ak,bk=map(int,input().split())
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
print(int((ak*bk)/gcd(ak,bk)))
