import math,bisect

A,B,C = map(int, input().split())
GCD = math.gcd(A,B,C)

ans = (A-GCD) + (B-GCD) + (C-GCD) 
print(ans)