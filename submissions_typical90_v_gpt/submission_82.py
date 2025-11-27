from math import gcd

n = list(map(int, input().split()))
n = sorted(n)
a, b, c = n

ippen = min(gcd(a, b), gcd(a, c))
print((a//ippen)-1 + (b//ippen)-1 + (c//ippen)-1)