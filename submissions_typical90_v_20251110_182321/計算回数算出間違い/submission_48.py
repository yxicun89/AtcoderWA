from math import gcd
a,b,c=map(int,input().split())
x=gcd(a,b,c)
print(a//x+b//x+c//x)