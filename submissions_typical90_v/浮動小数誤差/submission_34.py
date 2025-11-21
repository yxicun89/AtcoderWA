import math
a,b,c = map(int,input().split())
gcd = math.gcd(math.gcd(a,b),c) 
a,b,c = int(a/gcd), (b/gcd), (c/gcd)
print(int(a+b+c-3))