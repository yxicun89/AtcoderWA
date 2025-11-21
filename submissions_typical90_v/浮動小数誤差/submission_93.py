import math

a, b, c = map(int,input().split())

x = math.gcd(a,b,c)

ans = int(a/x) + int(b/x) + int(c/x) - 3

print(ans)