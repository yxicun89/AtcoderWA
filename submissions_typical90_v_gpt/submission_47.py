import math
a,b,c=map(int,input().split())
print(a*b*c/(math.gcd(c,math.gcd(a,b)))**3)