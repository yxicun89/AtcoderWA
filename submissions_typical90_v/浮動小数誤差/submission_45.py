import math
a,b,c = map(int,input().split())
ans = 0
d = math.gcd(a,b)
e = math.gcd(c,d)
ans = (a/e-1)+ (b/e-1) + (c/e-1)
print(int(ans))