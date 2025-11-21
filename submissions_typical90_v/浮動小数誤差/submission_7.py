import math

a,b,c=map(int,input().split())
gcd1=math.gcd(a,b,c)

print(a/gcd1 + b/gcd1 + c/gcd1 -3)
