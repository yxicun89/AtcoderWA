from math import gcd

a, b, c = map(int, input().split())

x = gcd(a, b, c)

ans = int(a/x + b/x + c/x - 3)

print(ans)
