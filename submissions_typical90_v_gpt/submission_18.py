import math
a,b,c = map(int,input().split())
X = math.gcd(a,b,c)

print((a+b+c)//X)