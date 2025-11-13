import math
a,b,c=map(int,input().split())
g=math.gcd(a,b,c)
k=a//g+b//g+c//g
print(k)

