from math import gcd

a = [*map(int, input().split())]
g = gcd(gcd(a[0], a[1]), a[2])

a, b, c = a

print((a//g-1)*(b//g-1)*(c//g-1))